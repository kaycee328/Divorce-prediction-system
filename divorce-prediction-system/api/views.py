from django.forms import ValidationError
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import generics, status
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from .serializers import DpsSerializer
import pandas as pd
from rest_framework import permissions
from .models import DPS
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.views import APIView
from rest_framework import authentication


def perform_prediction(values):
    pd.set_option("display.max_columns", None)
    dps_dataset = pd.read_csv("dps.csv")

    x = dps_dataset.drop(columns="Divorce")
    y = dps_dataset["Divorce"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    # y = dps_dataset.drop(dps_dataset.iloc[:, 0:-1], axis=1)

    decision_tree_model = DecisionTreeClassifier()
    decision_tree_model.fit(x_train, y_train)
    predictions = decision_tree_model.predict([values])
    return predictions == 1


class DpsView(permissions.IsAuthenticated, APIView):
    def get(self, request, format=None):
        qs = DPS.objects.all()
        serializer = DpsSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        # Check if DPS entry for the user already exists
        try:
            dps = DPS.objects.get(user=user)
            serializer = DpsSerializer(dps, data=data, partial=True)  # Partial update
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # If no DPS entry exists, create a new one
        except DPS.DoesNotExist:
            serializer = DpsSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DpsView2(generics.ListCreateAPIView):
    serializer_class = DpsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            # Admins see all objects
            return DPS.objects.all()
        return DPS.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        # Use get_queryset() to get the filtered queryset
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        divorced = 1
        vals = [serializer.validated_data[f"n{i}"] for i in range(1, 53)]
        predictions = perform_prediction(vals)
        # Admins can create for any user; regular users can only create for themselves
        if not self.request.user.is_staff:
            queryset = DPS.objects.filter(
                user=self.request.user, divorce_status=divorced
            )
            if queryset.exists():
                raise ValidationError("You have filled this form")
        serializer.save(user=self.request.user)


class DpsUpdateView(generics.UpdateAPIView):
    serializer_class = DpsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            # Admins see all objects
            return DPS.objects.all()
        return DPS.objects.filter(user=user)

    def perform_update(self, serializer):
        # Custom logic can be added here if needed
        serializer.save()
