from django import forms
from .models import Users
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):   

    password =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    cpassword =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'})) 

    class Meta:
        model = Users
        fields = ["first_name","last_name","user_email","role","user",'street','street_2','city','state','zip','contact_number']

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
        self.fields['contact_number'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder':'Contact Number'}
            )
        self.fields['street'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder':'Street'}
            )
        self.fields['street_2'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder':'Street 2'}
            )
        self.fields['city'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder':'City'}
            )
        self.fields['state'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder':'State'}
            )
        self.fields['zip'].widget.attrs.update(
            {'class': 'form-control',
            'placeholder':'Zip'}
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
        self.fields['password'].required = False
        self.fields['cpassword'].required = False
        self.fields['role'].required = False
        self.fields['street'].required = False
        self.fields['street_2'].required = False
        self.fields['city'].required = False
        self.fields['state'].required = False
        self.fields['zip'].required = False
        self.fields['contact_number'].required = False



