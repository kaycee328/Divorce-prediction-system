from rest_framework import serializers
from main.models import Divorce
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd


class DpsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name="get_username", read_only=True)
    divorced = serializers.BooleanField(source="divorce_status", read_only=True)

    class Meta:
        model = Divorce
        fields = ["user"] + [f"n{i}" for i in range(1, 53)] + ["divorced"]

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

    def perform_prediction(self, serializer):
        pd.set_option("display.max_columns", None)
        dps_dataset = pd.read_csv("dps.csv")

        x = dps_dataset.drop(columns="Divorce")
        y = dps_dataset["Divorce"]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
        # y = dps_dataset.drop(dps_dataset.iloc[:, 0:-1], axis=1)

        decision_tree_model = DecisionTreeClassifier()
        decision_tree_model.fit(x_train, y_train)

    def create(self, validated_data):
        print(validated_data)
        pass
        # Save the object with the logged-in user
        # serializer.save(user=self.request.user, divorce_stats=divorce)
