from email import contentmanager
from itertools import count
from queue import PriorityQueue
# import urlparse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
# from requests import session
from car.forms import CreateCarEntity
from .models import Car
from users.models import User, Users
from trip.models import Trips,Transaction

class CarEntity(View):
    
    def get(self, request):
        return render(request, 'webapp/car-asset.html')

    def post(self, request):
        # form = request.POST
        car_type = request.POST.get('car_type')
        car_number = request.POST.get('car_number')
        car_company = request.POST.get('company')
        car_model = request.POST.get('car_model')
        price = request.POST.get('price')

        car = Car(owner = Users.objects.get(user = request.user), car_type = car_type, price = price, 
                car_number=car_number, car_model= car_model, company = car_company)
        car.save()

        return redirect('home-view')

class SellerCarList(View):
    
    def get(self, request):
        
        cars = Car.objects.filter(owner = Users.objects.get(user = request.user))
        print(request.user)
        return render(request, template_name='webapp/seller-car-list.html', context={'cars':cars})

class UsersCarsList(View):

    def get(self,request):
        cars = Car.objects.all()
        return render(request, 'webapp/users-available-cars.html', context={"cars":cars} )

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
        context = {
            'car':car,
            "source":request.session['source'],
            "destination":request.session['destination'],
            "start_date":request.session['pickup-date'],
            "end_date":request.session['dropoff-date'],
            "time":request.session['time'],
            "price":request.GET['price']
        }
        
        return render(request,"webapp/book-car-payment.html",context)


class BookCarView(View):
    def post(self,request,pk,**kwargs):
        users = Users.objects.get(user=request.user)

        trip = Trips.objects.filter(user=users).filter(status=True)
        car = Car.objects.get(id=pk)
        if trip.count()>0:
            context = {
            'car':car,
            "source":request.session['source'],
            "destination":request.session['destination'],
            "start_date":request.session['pickup-date'],
            "end_date":request.session['dropoff-date'],
            "time":request.session['time'],
            "price":request.GET['price'],
            "error":"You already have an on going trip. End that trip to book a new one"
            }
            return render(request,"webapp/book-car-payment.html",context)

        
        trip=Trips(car=car,user=users)
        transaction = Transaction(trip=trip)

        car.availability = False

        trip.status = True
        trip.source=request.session['source']
        trip.destination=request.session['destination']
        trip.start_time=request.session['pickup-date']
        trip.end_time=request.session['dropoff-date']
        trip.time=request.session['time']

        car_owner=Users.objects.get(id=car.owner_id)
        transaction.payee=car_owner
        transaction.payer=Users.objects.get(user=request.user) 
        
        transaction.amount=(int)(request.build_absolute_uri().split("=")[1])
        transaction.card_number=request.POST['card_number']
        transaction.card_name=request.POST['card_name']
        transaction.cvv = request.POST['cvv']

        trip.save()
        transaction.save()
        car.save()
        

        return redirect("home-page")


class UpdateCarDetails(View):

    def get(self,request, pk):
        car = Car.objects.get(id=pk)

        return render(request, 'webapp/update-car.html', context={'car':car})
    
    def post(self, request, pk):
        car = Car.objects.get(id=pk)
        car.car_type = request.POST.get('car_type')
        car.car_number = request.POST.get('car_number')
        car.car_company = request.POST.get('company')
        car.car_model = request.POST.get('car_model')
        car.price = request.POST.get('price')        
        car.save()
        
        return render(request, 'webapp/update-car.html', context={'car':car})


        