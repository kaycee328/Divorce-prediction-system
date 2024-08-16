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
        # Print the validated data to the console (for debugging)
        print(serializer.validated_data)

        # Get the title and content from the validated data
        user = serializer.validated_data.get("user")
        print(user)

        # If user is not provided, generate default user
        if user is None:
            user = self.request.user

        # Save the object with the provided or generated user
        serializer.save(user=user)
