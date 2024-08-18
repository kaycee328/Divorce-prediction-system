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


class DpsView(generics.ListCreateAPIView):
    serializer_class = DpsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"

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
        print(serializer.data)
        return Response(serializer.data)

    def perform_prediction(self, values):
        pd.set_option("display.max_columns", None)
        dps_dataset = pd.read_csv("dps.csv")

        x = dps_dataset.drop(columns="Divorce")
        y = dps_dataset["Divorce"]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

        decision_tree_model = DecisionTreeClassifier()
        decision_tree_model.fit(x_train, y_train)
        predictions = decision_tree_model.predict([values])
        print(f"Prediction: {predictions}")
        return predictions[0] == 1

    def perform_create(self, serializer):
        vals = [serializer.validated_data[f"n{i}"] for i in range(1, 53)]
        prediction = self.perform_prediction(vals)

        queryset = DPS.objects.filter(user=self.request.user)
        if queryset.exists():
            # If an instance exists, update it
            existing_instance = queryset.first()
            # Update with validated data, and avoid serializing user directly
            serializer = self.get_serializer(
                existing_instance, data=serializer.validated_data, partial=True
            )
            if serializer.is_valid():
                serializer.save(divorce_status=prediction)
        else:
            # When creating, only pass user ID or other serializable fields
            serializer.save(user=self.request.user, divorce_status=prediction)
