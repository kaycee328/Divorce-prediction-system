# from rest_framework import serializers
# from .models import User
# from rest_framework.validators import UniqueValidator


# def validate_username(value):
#     qs = User.objects.filter(title__iexact=value)
#     if qs.exists:
#         raise serializers.ValidationError(f"{value} is already a product title..")
#     return value


# # def validate_title(value):
# #     if "hello" in value.lower():
# #         raise serializers.ValidationError(f"{value} is not allowed as a title..")
# #     return value


# unique_title = UniqueValidator(queryset=ProductApi.objects.all(), lookup="iexact")
