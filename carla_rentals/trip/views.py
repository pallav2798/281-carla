from django.shortcuts import render
from .models import Trips
from django.views import View
from users.models import Users
from car.models import Car

class SellerCarTrips(View):

    def get(self, request, pk):
        user = request.user
        trips = Trips.objects.filter(car__id = pk , user = Users.objects.get(user = user))

        return render(request, 'webapp/seller-car-trips.html')




