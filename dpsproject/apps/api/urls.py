from django.urls import path
from . import views

urlpatterns = [
    path("data/", views.DpsView.as_view(), name="dps_api"),
]
