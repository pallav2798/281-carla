from re import template
import re
from tempfile import tempdir
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'webapp/base.html')



class LoginView(View):
    template_name = "webapp/login.html"

    def get(self,request):
        return render(request, "webapp/login.html")