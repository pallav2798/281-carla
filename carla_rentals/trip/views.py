from django.shortcuts import render
from .models import Transaction, Trips
from django.views import View
from users.models import Users
from car.models import Car
# from .serializers 

class SellerCarTrips(View):

    def get(self, request, pk):
        user = request.user
        trans = Transaction.objects.filter(trip__car__id =pk) 
        car  = Car.objects.get(id = pk)
        car_model  = car.car_model
        car_company  = car.company
        car_price_ph = car.price_ph
        car_price_pd = car.price_pd

        print(pk)
        return render(request, 'webapp/seller-car-trips.html', 
            context={'transactions':trans, 'car_model':car_model, 'car_company':car_company,'price_ph':car_price_ph,'price_pd':car_price_pd})
        




