from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signupPage, name='signup'),
    path('signin/', views.UserLogin.as_view(), name='signin'),
    path('logout/', views.Logout_user.as_view(), name='signout'),

]
