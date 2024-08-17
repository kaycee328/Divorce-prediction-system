from rest_framework import serializers
from .models import DPS
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd


class DpsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    divorced = serializers.BooleanField(source="divorce_status", read_only=True)

    class Meta:
        model = DPS
        fields = ["pk", "username", "divorced"] + [f"n{i}" for i in range(1, 53)]

    # def create(self, validated_data):
    #     # Automatically set the 'user' field to the currently logged-in user
    #     user = self.context["request"].user
    #     validated_data["user"] = user
    #     return super(DpsSerializer, self).create(validated_data)
