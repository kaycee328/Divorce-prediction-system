import pandas as pd
import numpy as np
from typing import Any
from django.shortcuts import render, redirect
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from .forms import DivorcePredictionForm
from django.contrib.auth.decorators import login_required
from sklearn.model_selection import train_test_split
from .models import Divorce
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
import os
from django.conf import settings


# HOMEPAGE VIEW
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "main_app/primary/homepage.html"


# This is the view for the page that displays the Form
@login_required
def predictionpage(request):
    pd.set_option("display.max_columns", None)

    # read the dataset and convert it to a dataframe using pandas
    dps_dataset = pd.read_csv(os.path.join(settings.BASE_DIR, "dps.csv"))

    x = dps_dataset.drop(columns="Divorce")
    y = dps_dataset["Divorce"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    # y = dps_dataset.drop(dps_dataset.iloc[:, 0:-1], axis=1)

    decision_tree_model = DecisionTreeClassifier()
    decision_tree_model.fit(x_train, y_train)

    if request.method == "POST":
        # Delete any existing Divorce model associated with the current user
        delete_user_model = Divorce.objects.filter(user=request.user).delete()

        # Initialize a new Divorce model associated with the current user
        user_model = Divorce(user=request.user)

        # If no existing model was deleted, initialize a new one
        if not delete_user_model:
            user_model = Divorce(user=request.user)

        form = DivorcePredictionForm(request.POST)

        if form.is_valid():
            # Get input values from form
            vals = [form.cleaned_data[f"n{i}"] for i in range(1, 53)]

            # Populate Divorce model with input data
            for i, val in enumerate(vals, start=1):
                attribute_name = f"n{i}"
                setattr(user_model, attribute_name, val)

            # Make predictions and update the Divorce object
            predictions = decision_tree_model.predict([vals])
            user_model.divorce_status = predictions == 1
            user_model.save()

            # Redirect user to result page
            return redirect("result")

    else:
        # If request method is not POST, initialize an empty form
        form = DivorcePredictionForm()

    return render(request, "main_app/primary/predictionpage.html", {"form": form})


# this is the view for the page that displays the result
class ResultView(LoginRequiredMixin, TemplateView):
    template_name = "main_app/result/result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = (
            Divorce.objects.select_related("user")
            .filter(user=self.request.user)
            .first()
        )
        return context
