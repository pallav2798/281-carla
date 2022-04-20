from django import forms
from .models import Users
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):   

    password =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    cpassword =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'})) 

    class Meta:
        model = Users
        fields = ["first_name","last_name","user_email","role","user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder':'Enter First Name'}
            )
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder':'Enter Last Name'}
            )
        self.fields['user_email'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder':'Enter Email'}
            )
        self.fields['role'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder':'Enter Role'}
            )
        self.fields['user'].widget.attrs.update(
            {
            'tag':forms.HiddenInput()}
            )
        self.fields['user'].required = False