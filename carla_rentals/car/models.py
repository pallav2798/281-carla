from django.db import models
from users.models import Users

from django.utils.deconstruct import deconstructible

# Create your models here.


@deconstructible
class file_path(object):
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, instance, filename):
        
        if len(filename.split('.')) > 1:
            print('filename')
            ext = filename.split('.')[-1]
            filename = "{}/{}-{}/{}/{}-{}.{}" .format(
                self.prefix, instance.owner.id, instance.owner.full_name,'images', "car",instance.id, ext)

        return filename

class Car(models.Model):
    owner = models.ForeignKey(Users, null= False,on_delete = models.CASCADE)
    car_type = models.CharField('Car Type', max_length=30, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    car_number = models.CharField('Car Number', max_length=10,null = False, unique=True , default="")
    company = models.CharField('Car Company', null = False, max_length=30)
    car_model = models.CharField('Car Model', null = True, max_length=30)
    availability = models.BooleanField(default=True)    
    price_pd =  models.PositiveIntegerField(default = 0, null=False)
    price_ph = models.PositiveIntegerField(default = 0, null=False)
    car_image = models.FileField('image',null = True, max_length=300, upload_to=file_path('media/'))
    miles = models.CharField('Miles',max_length=8, null = True,default='0')

