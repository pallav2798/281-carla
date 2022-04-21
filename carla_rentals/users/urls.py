from django.urls import path
from .views import HomeView, LoginView, ProfileView,RegisterView,LogoutView

urlpatterns = [
    path('home', HomeView.as_view(), name='home-page'),
    path('login',LoginView.as_view(), name="login-page"),
    path('register',RegisterView.as_view(),name="register"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('profile/<int:pk>',ProfileView.as_view(),name="profile")

]