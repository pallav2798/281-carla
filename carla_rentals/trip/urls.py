from django.urls import path
from .views import CurrentTripView, EndTripView, SellerCarTrips

urlpatterns = [
    path('seller-car-trips/<int:pk>', SellerCarTrips.as_view(), name='seller_car_trips'),
    path('current-trip/<int:pk>',CurrentTripView.as_view(),name="current-trip"),
    path('end-trip/<int:pk>' , EndTripView.as_view(),name="end-trip" )
]