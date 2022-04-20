from django.db import models
from users.models import Users
from car.models import Car
# Create your models here.

class Trips(models.Model):
    user = models.ForeignKey(Users,null = False,on_delete = models.CASCADE)
    car = models.ForeignKey(Car,null = False ,on_delete = models.CASCADE)
    status = models.CharField('status',max_length=30, null = True)
    source = models.CharField('Source', max_length=100, null=False)
    destination = models.CharField('Source', max_length=100, null=False)
    start_time = models.CharField('Start Time', max_length=30,null = False,default="")
    end_time = models.CharField('End Time',max_length=30,default="", null=False)
    duration = models.CharField('Duration',max_length=30)

class Transaction(models.Model):
    trip = models.ForeignKey(Trips, null = False,on_delete = models.CASCADE)
    payer = models.ForeignKey(Users,related_name='payer_person', null = False,on_delete = models.CASCADE)
    payee = models.ForeignKey(Users,related_name='payee_person', null = False,on_delete = models.CASCADE)
    amount  = models.IntegerField(null=False, default=0)