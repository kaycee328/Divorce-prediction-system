from django.urls import path
from .controller import SignupView

urlpatterns = [
    path("api/signup/", SignupView.as_view(), name="signup"),
    # No need for a specific login endpoint, as DRF handles it via BasicAuthentication.
]
