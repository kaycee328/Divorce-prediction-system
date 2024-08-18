from django.urls import path
from . import views

urlpatterns = [
    path("version/", views.DpsView.as_view(), name="dps_api"),
]
