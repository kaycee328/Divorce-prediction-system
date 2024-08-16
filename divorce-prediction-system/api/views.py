from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import generics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from main.models import Divorce
from .serializers import DpsSerializer
import pandas as pd


class DpsView(generics.ListCreateAPIView):
    serializer_class = DpsSerializer
    queryset = Divorce.objects.all()

    # Specify the renderer classes
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    def perform_prediction(self, serializer):
        pd.set_option("display.max_columns", None)
        dps_dataset = pd.read_csv("dps.csv")

        x = dps_dataset.drop(columns="Divorce")
        y = dps_dataset["Divorce"]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
        # y = dps_dataset.drop(dps_dataset.iloc[:, 0:-1], axis=1)

        decision_tree_model = DecisionTreeClassifier()
        decision_tree_model.fit(x_train, y_train)

    def perform_create(self, serializer):
        # Save the object with the logged-in user
        serializer.save(user=self.request.user)


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


def create_dps_model():
    attrs = {
        "user": models.OneToOneField(User, on_delete=models.CASCADE),
        "date": models.DateTimeField(auto_now_add=True),
        "divorce_status": models.BooleanField(default=False, null=True),
    }

    # Dynamically add n1 to n52 fields
    for i in range(1, 53):
        attrs[f"n{i}"] = models.IntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(4)],
            error_messages={
                "min_value": "The value must be within the range of 0-4",
                "max_value": "The value must be within the range of 0-4",
                "invalid": "Please enter a valid integer.",
            },
        )

    # Use type() to create the model class
    return type("DPS", (models.Model,), attrs)


# Create the DPS model class
DPS = create_dps_model()
