from django import forms
from .models import Users

from django.contrib.auth.models import User

class SellerRegisterForm(forms.ModelForm):
   
    class Meta:
        model = Users
        fields = '__all__'

class SellerRegisterAuthForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

        