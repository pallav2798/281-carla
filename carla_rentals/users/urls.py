from django.urls import path
from .views import HomeView, LoginView

urlpatterns = [
    path('home', HomeView.as_view(), name='home-page'),
    path('login',LoginView.as_view(), name="login-page")
]