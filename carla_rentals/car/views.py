from queue import PriorityQueue
import re
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from car.forms import CreateCarEntity
from .models import Car
from users.models import User, Users
from trip.models import Trips

class CarEntity(View):
    
    def get(self, request):
        return render(request, 'webapp/car-asset.html')

    def post(self, request):
        # form = request.POST
        car_type = request.POST.get('car_type')
        car_number = request.POST.get('car_number')
        car_company = request.POST.get('company')
        car_model = request.POST.get('car_model')

        car = Car(owner = Users.objects.get(user = request.user), car_type = car_type, 
                car_number=car_number, car_model= car_model, company = car_company)
        car.save()

        return redirect('home-view')

class SellerCarList(View):
    
    def get(self, request):
        
        cars = Car.objects.filter(owner = Users.objects.get(user = request.user))
        return render(request, template_name='webapp/seller-car-list.html', context={'cars':cars})

class UsersCarsList(View):

    def post(self, request):
        user = Users.objects.get(user = request.user)
        cars = Car.objects.all()

        request.session['source']=request.POST['source']
        request.session['destination']=request.POST['destination']
        request.session['pickup-date']=request.POST['pickup-date']
        request.session['dropoff-date']=request.POST['dropoff-date']
        request.session['time']=request.POST['time']

        return render(request, 'webapp/users-available-cars.html', context={"cars":cars} )


class BookCarPaymentView(View):
    def get(self,request,pk):
        car = Car.objects.get(id=pk)
        return render(request,"webapp/book-car-payment.html",{"car":car})


class BookCarView(View):
    def get(self,request,pk):
        users = Users.objects.get(user=request.user)
        car = Car.objects.get(id=pk)
        car.availability = False
        trip=Trips(car=car,user=users)

        trip.status = True
        trip.source=request.session['source']
        trip.destination=request.session['destination']
        trip.start_time=request.session['pickup-date']
        trip.end_time=request.session['dropoff-date']
        trip.time=request.session['time']

        car.save()
        trip.save()

        return redirect("home-page")
