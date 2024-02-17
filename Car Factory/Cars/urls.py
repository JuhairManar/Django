from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='car_display'),
    path('add_cars/', add_cars, name='add_cars'),
    path('signup/',signup,name='signup'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('profile/',profile,name='profile'),
]