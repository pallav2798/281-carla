from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from .models import Car
from trip.models import Trips
from users.models import Users

class CarSerializer(serializers.ModelSerializer):
    total_earnings = serializers.SerializerMethodField()
    car_image = serializers.SerializerMethodField()
    timestamp = serializers.DateTimeField(format = "%m/%d/%Y")
    
    def get_total_earnings(self, obj):
        total = sum(Trips.objects.filter(car=obj).values_list('price', flat=True))
        if total is None:
            total = 0
        return total    

    def get_car_image(self, obj):
        if obj.car_image:
            print(obj)
            return obj.car_image.url
        else:
            return '/static/images/car-8.jpg'

    class Meta:
        model = Car
        fields = '__all__'

class SellersListSerializer(serializers.ModelSerializer):
    earnings = serializers.SerializerMethodField()

    def get_earnings(self, obj):
        total = sum(Trips.objects.filter(car__owner=obj).values_list('price', flat=True))
        if total is None:
            total = 0
        return total    
    
    class Meta:
        model = Users
        fields = '__all__'


class CustomerListSerializer(serializers.ModelSerializer):
    spendings = serializers.SerializerMethodField()

    def get_spendings(self, obj):
        total = sum(Trips.objects.filter(user=obj).values_list('price', flat=True))
        if total is None:
            total = 0
        return total    
    
    class Meta:
        model = Users
        fields = '__all__'
