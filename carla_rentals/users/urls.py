from django.urls import path
from .views import  AdminAnalysis, AdminCustomersList, AdminHomeView, AdminLoginView, AdminSellerCarList, AdminSellerList, HomeView, LoginView, ProfileView, RegisterView, LogoutView
from trip.views import AdminCustomerTripsList

urlpatterns = [
    path('home', HomeView.as_view(), name='home-page'),
    path('login', LoginView.as_view(), name="login-page"),
    path('register', RegisterView.as_view(), name="register"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('profile/<int:pk>', ProfileView.as_view(), name="profile"),
    path('admin/login', AdminLoginView.as_view(), name="admin_login"),
    path('admin/home', AdminHomeView.as_view(), name="admin_home"),

    path('admin/sellers-list', AdminSellerList.as_view(), name="admin_sellerslist"),
    path('admin/customer-list', AdminCustomersList.as_view(), name="admin_customerslist"),
    path('admin/customer-trips-list/<int:pk>', AdminCustomerTripsList.as_view(), name="admin_customer_tripslist"),
    path('admin/seller-cars-list/<int:pk>', AdminSellerCarList.as_view(), name="admin_seller_carslist"),
    path('admin/analysis', AdminAnalysis.as_view(), name="admin_analysis"),



]

