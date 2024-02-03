from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('city_state_search/',city_state_search,name="city_state_search"),
]