from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('home/', views.HomePage.as_view(), name='homepage2'),
    path('prediction/', views.predictionpage, name='dps'),
    path('result/', views.ResultView.as_view(), name='result'),
]

