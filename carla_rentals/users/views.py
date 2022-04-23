
import email
from multiprocessing import context
from django.urls import reverse_lazy,reverse
from re import template
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView,FormView, UpdateView
from django.contrib.auth import authenticate,login
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .models import Users
from carla_rentals.decorators import check_session

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



class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("login-page")


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
                request.session['role'] = users_obj.role
                request.session['user_id'] = users_obj.id 

                if users_obj.role == 'Seller':
                    return redirect('car_asset')
                else:
                    return redirect('home-page' )

            else:
                return render(request, 'webapp/login.html',{"error":"Wrong Credentials"})
        except Exception as e:
            return render(request,'webapp/404-page.html')


class ProfileView(UpdateView):
    model = Users
    template_name = 'webapp/profile.html'
    form_class = RegistrationForm
    success_url = '/users/home-page' 


    @check_session
    def post(self, request,pk):

        if self.request.user.is_authenticated:
            user = Users.objects.get(id = pk)
            user.first_name = self.request.POST.get('first_name')
            user.last_name = self.request.POST.get('last_name')
            user.contact_number = self.request.POST.get('contact_number')
            user.street = self.request.POST.get('street')
            user.street_2 = self.request.POST.get('street_2')
            user.city= self.request.POST.get('city')
            user.state = self.request.POST.get('state')
            user.zip = self.request.POST.get('zip')
            user.save()

            return redirect('profile',pk=pk)
        
        else:
            return redirect('login-page')

class ServerError(View):

    def get(self, request):
        print('------------')
        return render(request, 'webapp/404-page.html')
