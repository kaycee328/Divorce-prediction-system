from rest_framework.serializers import ModelSerializer
from main.models import Divorce


class DpsSerializer(ModelSerializer):
    class Meta:
        model = Divorce
        fields = "__all__"
