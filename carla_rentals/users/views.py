from re import template
import re
from tempfile import tempdir
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

class HomeView(View):
    def get(self, request):
        if(not request.user.is_authenticated):
            return render(request, "webapp/login.html")    
        return render(request, 'webapp/base.html')


class RegisterView(View):
    def get(self,request):
        # super.get()
        return render(request,"webapp/register.html")
    
    def post(self,request):
        pass


class LoginView(View):
    template_name = "webapp/login.html"

    def get(self,request):
        return render(request, "webapp/login.html")

    # def post(self,request):
    #     email = 