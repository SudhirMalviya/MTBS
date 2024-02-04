from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',home,name="home"),
    path('search/',search,name="search"),
    path('city_search/',city_search,name="city_search"),
    path('all_city_data',all_city_data,name="all_city_data"),
    path('admindash',admindash,name="admindash"),
    path('create_movie_page',create_movie_page,name="create_movie_page"),
    path('create_movie',create_movie,name="create_movie"),
    path('update_movie',update_movie,name="update_movie")
]
if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
