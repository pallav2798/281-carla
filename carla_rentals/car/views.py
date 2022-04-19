from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from car.forms import CreateCarEntity
from .models import Car
class CarEntity(View):
    
    def get(self, request):
        return render(request, 'webapp/car-asset.html')

    def post(self, request):
        user = self.request.user
        # form = request.POST
        car = Car(owner = user)
        form = CreateCarEntity(instance=Car, data = request.POST)
        # form.owner  = user
        print(form)
        if form.is_valid():
            # form['owner'] = user
            form = form.cleaned_data

            print('form-------------------------')
            print(form)
            try:

                form = form.save(commit=False)
                form.save()
                return redirect('home-view')
            except Exception as e:
                raise e
    