from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        return user
