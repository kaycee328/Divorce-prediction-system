from django.urls import path
from .controller import SignupView, LoginView, Test

urlpatterns = [
    path("api/signup/", SignupView.as_view(), name="signup"),
    path("api/login/", LoginView.as_view(), name="Login"),
    path("test/", Test.as_view(), name="Test"),
    # No need for a specific login endpoint, as DRF handles it via BasicAuthentication.
]
