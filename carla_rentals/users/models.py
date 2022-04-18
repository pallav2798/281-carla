import email
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Users(models.Model):
    
    USER_ROLES = (
        ('Seller','seller'),
        ('Owner','owner'),
        ('Admin','admin'),
    )
    user =  models.ForeignKey(User , null= False,on_delete = models.CASCADE)
    first_name = models.CharField('First Name',null=True, max_length=30)
    last_name = models.CharField('Last Name', null=True, max_length=30)
    role = models.CharField('User Role', max_length=20, choices= USER_ROLES)
    user_email = models.EmailField(null = False)
    street = models.CharField('Street', max_length=200)
    street_2 = models.CharField(
        'Second Street', max_length=200, blank=True, null=True)
    city = models.CharField('City', max_length=200)
    state = models.CharField('State', max_length=200)
    zip = models.CharField('Zip code', max_length=30)

    @property
    def full_name(self):
        return "{} {}".format(
            self.first_name.capitalize(),
            self.last_name.capitalize()
        )
    
    @property
    def address(self):
        street = self.street if not self.street_2 else "{}, {}".format(
            self.street, self.street_2
        )

        return "{} {}, {} {}".format(
            street, self.city,
            self.state, self.zip
        )
    def __str__(self):
        return self.full_name
