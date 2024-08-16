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
