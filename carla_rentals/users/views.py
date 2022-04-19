from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from .forms import SellerRegisterAuthForm, SellerRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login

class HomeView(View):
    def get(self, request):
        return render(request, 'webapp/base.html')



class LoginView(View):
    template_name = "webapp/login.html"

    def get(self,request):
        return render(request, "webapp/user-home.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
            return render(request, 'webapp/user-home.html')
        except Exception as e:
            return render('404-page.html')


class CustomersRegisterView(View):

    def get(self, request):
        return render(request, 'webapp/customer-register.html')        

class SellerRegisterView(View):

    def get(self,request):
        return render(request, "webapp/seller-register.html")

    def post(self, request):
        form = request.POST.copy()
        form['role'] = ['seller']
        auth_form = SellerRegisterAuthForm(form)

        print(request)
        try:
            if auth_form.is_valid():
                user = auth_form.save()
                login(request, user)
                form = SellerRegisterForm(user= user , data = form)
                form.save()
                print('-----------------------')
                return render(request, 'webapp/user-home.html')
            else:
                print(auth_form.errors)
        except Exception as e:
            return render('404-page.html')




class BookRide(View):

    def post(self, request):
        form = request.POST


    