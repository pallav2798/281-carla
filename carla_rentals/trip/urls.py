from django.urls import path
from .views import SellerCarTrips

urlpatterns = [
    path('seller-car-trips/<int:pk>', SellerCarTrips.as_view(), name='seller_car_trips'),
]