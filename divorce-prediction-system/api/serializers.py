from rest_framework import serializers
from .models import DPS


class DpsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    divorced = serializers.BooleanField(source="divorce_status", read_only=True)

    class Meta:
        model = DPS
        fields = ["pk", "username", "divorced"] + [f"n{i}" for i in range(1, 53)]
