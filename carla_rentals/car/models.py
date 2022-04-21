from django.db import models
from users.models import Users
# Create your models here.

class Car(models.Model):
    owner = models.ForeignKey(Users, null= False,on_delete = models.CASCADE)
    car_type = models.CharField('Car Type', max_length=30, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    car_number = models.CharField('Car Number', max_length=10,null = False, unique=True , default="")
    company = models.CharField('Car Company', null = False, max_length=30)
    car_model = models.CharField('Car Model', null = True, max_length=30)
    availability = models.BooleanField(default=True)
    price =  models.PositiveIntegerField(default = 0, null=False)



