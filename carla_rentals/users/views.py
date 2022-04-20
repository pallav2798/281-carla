
import email
from multiprocessing import context
from django.urls import reverse_lazy,reverse
from re import template
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView,FormView
from django.contrib.auth import authenticate,login
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Users

class HomeView(View):
    def get(self, request):
        if(not request.user.is_authenticated):
            return render(request, "webapp/login.html")    
        return render(request, 'webapp/user-home.html')


class RegisterView(FormView):
    template_name = "webapp/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("login-page")


    def post(self, request, *args, **kwargs) :
        form = self.get_form()
        if form.is_valid():
            pwd = form.cleaned_data.get('password')
            cpwd = form.cleaned_data.get('cpassword')

            if pwd!=cpwd:
                form.add_error('password',"Password and confirm Password does not match")
                return render(request, 'webapp/register.html',{'form':form})

            user = User(username=form.cleaned_data.get('user_email'),
                        first_name=form.cleaned_data.get("first_name"),
                        last_name=form.cleaned_data.get("last_name"),)
                        
            user.set_password(pwd)
            user.save()
            users = Users.objects.create(user=user,
                                        first_name=form.cleaned_data.get("first_name"),
                                        last_name=form.cleaned_data.get("last_name"),
                                        user_email=form.cleaned_data.get("user_email"),
                                        role=form.cleaned_data.get("role"))

            users.save()
            

        else:            
            return render(request, 'webapp/register.html',{'form':form})

        return super().post(request, *args, **kwargs)




class LoginView(TemplateView):
    template_name = "webapp/login.html"


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
            if user:
                # authenticated
                login(request,user)
                users_obj = Users.objects.get(user=user.id)
                # return render(request, 'webapp/user-home.html')
                request.session['role'] = users_obj.role
                if users_obj.role == 'Seller':
                    return redirect('car_asset')
                else:
                    return redirect('home-page' )

            else:
                return render(request, 'webapp/login.html',{"error":"Wrong Credentials"})
        except Exception as e:
            print(e)
            return render(request,'webapp/404-page.html')


      




class BookRide(View):

    def post(self, request):
        form = request.POST


    
