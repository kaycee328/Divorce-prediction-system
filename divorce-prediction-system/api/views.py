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


class DpsView(APIView):
    # def get_queryset(self):
    # user = self.request.user
    # # Assuming you have a method `is_notadmin()` on the user model
    # return DPS.all()

    def get(self, request, format=None):
        # qs = self.get_queryset()
        qs = DPS.objects.all()
        serializer = DpsSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DpsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator


# def create_dps_model():
#     attrs = {
#         "user": models.OneToOneField(User, on_delete=models.CASCADE),
#         "date": models.DateTimeField(auto_now_add=True),
#         "divorce_status": models.BooleanField(default=False, null=True),
#     }

#     # Dynamically add n1 to n52 fields
#     for i in range(1, 53):
#         attrs[f"n{i}"] = models.IntegerField(
#             validators=[MinValueValidator(0), MaxValueValidator(4)],
#             error_messages={
#                 "min_value": "The value must be within the range of 0-4",
#                 "max_value": "The value must be within the range of 0-4",
#                 "invalid": "Please enter a valid integer.",
#             },
#         )

#     # Use type() to create the model class
#     return type("DPS", (models.Model,), attrs)


# # Create the DPS model class
# DPS = create_dps_model()
#     if request.method == 'POST':
#          # Delete any existing Divorce model associated with the current user
#         delete_user_model = Divorce.objects.filter(user=request.user).delete()

#         # Initialize a new Divorce model associated with the current user
#         user_model = Divorce(user=request.user)

#         # If no existing model was deleted, initialize a new one
#         if not delete_user_model:
#             user_model = Divorce(user=request.user)

#         form = DivorcePredictionForm(request.POST)

#         if form.is_valid():
#             # Get input values from form
#             vals = [form.cleaned_data[f'n{i}'] for i in range(1, 53)]

#             # Populate Divorce model with input data
#             for i, val in enumerate(vals, start=1):
#                 attribute_name = f'n{i}'
#                 setattr(user_model, attribute_name, val)

#             # Make predictions and update the Divorce object
#             predictions = decision_tree_model.predict([vals])
#             user_model.divorce_status = predictions == 1
#             user_model.save()

#             # Redirect user to result page
#             return redirect('result')
