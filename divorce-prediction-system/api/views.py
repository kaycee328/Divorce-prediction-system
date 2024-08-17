from django.forms import ValidationError
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import generics, status
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from .serializers import DpsSerializer
import pandas as pd
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import DPS
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.views import APIView


class DpsView(IsAuthenticated, APIView):
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
    queryset = DPS.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        mainqs = super().get_queryset()
        user = self.request.user
        return DPS.objects.filter(user=user)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        query_set = self.get_queryset()
        serializer = DpsSerializer(query_set, many=True)
        Response(serializer.data)

    def perform_create(self, serializer):
        queryset = DPS.objects.filter(
            user=self.request.user,
        )
        if queryset.exists():
            raise ValidationError("You have already signed up")
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        DPS(user=self.request.user, modified=instance)
