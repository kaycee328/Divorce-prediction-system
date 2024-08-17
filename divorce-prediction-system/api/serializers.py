from rest_framework import serializers
from .models import DPS
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd


class DpsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name="get_username", read_only=True)
    divorced = serializers.SerializerMethodField(
        method_name="get_divorce_status", read_only=True
    )

    class Meta:
        model = DPS
        fields = ["user"] + [f"n{i}" for i in range(1, 53)] + ["divorced"]

    def get_username(self, obj):
        if isinstance(obj, DPS):
            user = obj.user
            print(user)
            return obj.user
        return None

    def get_divorce_status(self, obj):
        if isinstance(obj, DPS):
            divorce_status = obj.divorce_status
            print(divorce_status)
            return divorce_status
        return None

    # def create(self, validated_data):
    #     # Automatically set the 'user' field to the currently logged-in user
    #     user = self.context["request"].user
    #     validated_data["user"] = user
    #     return super(DpsSerializer, self).create(validated_data)
