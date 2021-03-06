"""carla_rentals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from users import urls as users_url
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings
from users.views import ServerError


urlpatterns = [
    path("",users_views.HomeView.as_view() , name = "home-view"),
    path('admin/', admin.site.urls),
    path('users/', include(users_url)),
    path('car/', include('car.urls')),
    path('trip/', include('trip.urls')),
    path('404-not-found/', ServerError.as_view(),name= '404_page' )


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)