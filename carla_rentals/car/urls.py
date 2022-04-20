from django.urls import path
from .views import CarEntity , SellerCarList
urlpatterns = [
    path('car-asset', CarEntity.as_view(), name='car_asset'),
    path('seller-cars', SellerCarList.as_view(), name='seller_cars'),

]