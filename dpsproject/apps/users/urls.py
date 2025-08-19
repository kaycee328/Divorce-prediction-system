from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.signupPage, name="signup1"),
    path("signin/", views.UserLogin.as_view(), name="signin1"),
    path("logout/", views.logout_view, name="signout1"),
    # path("logout/", views.Logout_user.as_view(), name="signout1"),
]
