from django.urls import path
from .views import CarEntity , SellerCarList, UsersCarsList,BookCarView,BookCarPaymentView
urlpatterns = [
    path('car-asset', CarEntity.as_view(), name='car_asset'),
    path('seller-cars', SellerCarList.as_view(), name='seller_cars'),
    path('users-cars-availablity-list', UsersCarsList.as_view(), name='users_cars_availablity_list'),
    path("book-car-payment/<int:pk>",BookCarPaymentView.as_view(),name="book-car-payment"),
    path("book-car/<int:pk>",BookCarView.as_view(),name="book-car")


]