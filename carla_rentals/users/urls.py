from django.urls import path
from .views import HomeView, LoginView,RegisterView

urlpatterns = [
    path('home', HomeView.as_view(), name='home-page'),
    path('login',LoginView.as_view(), name="login-page"),
    path('register',RegisterView.as_view(),name="register")
]