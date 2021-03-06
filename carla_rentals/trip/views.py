from re import A
from django.shortcuts import render
from .models import Transaction, Trips
from django.views import View
from users.models import Users
from car.models import Car
from carla_rentals.decorators import check_session
from django.shortcuts import redirect, render, get_object_or_404
# from .serializers 

class SellerCarTrips(View):

    @check_session
    def get(self, request, pk):
        trans = Transaction.objects.filter(trip__car__id =pk) 
        car  = Car.objects.get(id = pk)
        car_model  = car.car_model
        car_company  = car.company
        car_price_ph = car.price_ph
        car_price_pd = car.price_pd

        return render(request, 'webapp/seller-car-trips.html', 
            context={'transactions':trans, 'car_model':car_model, 'car_company':car_company,'price_ph':car_price_ph,'price_pd':car_price_pd})
        

class TripHistoryView(View):
    def get(self,request):
        trips =Trips.objects.filter(user=Users.objects.get(user=request.user).id).order_by('-id')
        amount=0
        status=None
        for trip in trips:
            amount+=trip.price
            if trip.status == "True":
                status=trip

        context={
            "trips":trips,
            "amount":amount,
            "status":status
        }
    
        return render(request,"webapp/trip-history.html",context)

class CurrentTripView(View):


    @check_session
    def get(self,request,pk):
        users = Users.objects.get(user=pk)
        trip = Trips.objects.filter(user=users).filter(status=True)

        if trip.count()==0:
            return render(request,"webapp/current-trip.html")   
            
        trip=trip[0]
        car = Car.objects.get(id=trip.car.id)     
        
        context={
            "car":car,
            "trip":trip
        }
        
        return render(request,"webapp/current-trip.html",context)


class TripDetailView(View):
    def get(self,request,pk):
        trip = Trips.objects.get(id=pk)
        car = Car.objects.get(id=trip.car.id)
        transaction = Transaction.objects.get(trip=trip.id)

        context = {
            "transaction":transaction,
            "car":car,
            "trip":trip
        }

        return render(request,"webapp/trip-detail.html",context)


class EndTripView(View):


    @check_session
    def get(self,request,pk):
        trip = Trips.objects.get(id=pk)
        trip.status = False
        car = Car.objects.get(id=trip.car.id)        
        car.availability = True

        car.save()
        trip.save()

        return redirect('current-trip',pk=request.user.id)


class AdminCustomerTripsList(View):

    @check_session
    def get(self, request, pk):
        trans = Transaction.objects.filter(trip__user__id =pk) 
        # car  = Car.objects.get(id = pk)
        # car_model  = car.car_model
        # car_company  = car.company
        # car_price_ph = car.price_ph
        # car_price_pd = car.price_pd

        return render(request, 'webapp/seller-car-trips.html',
            context={'transactions':trans})
        
