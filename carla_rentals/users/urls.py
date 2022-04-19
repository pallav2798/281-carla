from django.urls import path
from .views import HomeView, LoginView, SellerRegisterView

urlpatterns = [
    path('home', HomeView.as_view(), name='home_page'),
    path('login',LoginView.as_view(), name="login_page"),
    path('seller/register/',SellerRegisterView.as_view(), name="seller_register")

]