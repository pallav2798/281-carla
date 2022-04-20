from django.urls import path
from .views import CarEntity

urlpatterns = [
    path('car-asset', CarEntity.as_view(), name='car_asset'),
]