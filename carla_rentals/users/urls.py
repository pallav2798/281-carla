from django.urls import path
from .views import HomeView, LoginView,RegisterView,LogoutView

urlpatterns = [
    path('home', HomeView.as_view(), name='home-page'),
    path('login',LoginView.as_view(), name="login-page"),
    path('register',RegisterView.as_view(),name="register"),
    path('logout',LogoutView.as_view(),name="logout")
]