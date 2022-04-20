from django import forms
from .models import Car

class CreateCarEntity(forms.ModelForm):
   
    class Meta:
        model = Car
        exclude = ('owner',)
        