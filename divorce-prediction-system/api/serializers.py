from rest_framework import serializers
from main.models import Divorce


class DpsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name="get_username", read_only=True)
    divorce_status = serializers.SerializerMethodField(
        method_name="view_divorce", read_only=True
    )

    class Meta:
        model = Divorce
        fields = ["user"] + [f"n{i}" for i in range(1, 53)] + ["divorce_status"]

    def view_divorce(self, obj):
        request = self.context.get(
            "request"
        )  # Get the request object from the serializer context

        if request is None:  # Check if request is None
            return None  # Return None if there is no request
        return obj.divorce_status

    def get_username(self, obj):
        if isinstance(obj, Divorce):
            user = self.context.get("request").user.username
            # user = obj.user.username
            # print(user)
            return user
        return None

    def validate(self, data):
        for i in range(1, 53):
            field_name = f"n{i}"
            value = data.get(field_name)
            if value is not None and (value < 0 or value > 4):
                raise serializers.ValidationError(
                    {field_name: "The value must be between 0 and 4."}
                )
        return data

    # def create(self, validated_data):
    #     # Automatically assign the logged-in user
    #     validated_data["user"] = self.context["request"].user
    #     # print(validated_data)
    #     return super().create(validated_data)
