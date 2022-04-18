from django.db import models
from users.models import Users
from car.models import Car
# Create your models here.

class Trips(models.Model):
    user = models.ForeignKey(Users,null = False,on_delete = models.CASCADE)
    car = models.ForeignKey(Car,null = False ,on_delete = models.CASCADE)
    source = models.CharField('Source', max_length=100, null=False)
    destination = models.CharField('Source', max_length=100, null=False)
    start_time = models.DateTimeField('Start Time', null = False)
    end_time = models.DateTimeField('End Time', null=False)
    duration = models.TimeField('Duration')

class Transaction(models.Model):
    trip = models.ForeignKey(Trips, null = False,on_delete = models.CASCADE)
    payer = models.ForeignKey(Users,related_name='payer_person', null = False,on_delete = models.CASCADE)
    payee = models.ForeignKey(Users,related_name='payee_person', null = False,on_delete = models.CASCADE)
    amount  = models.IntegerField(null=False, default=0)