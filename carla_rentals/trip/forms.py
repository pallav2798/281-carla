from django import forms
from .models import Trips

class TripCreate(forms.ModelForm):
    class Meta:
        model = Trips
        