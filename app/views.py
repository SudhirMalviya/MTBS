from django.shortcuts import render,redirect
from django.http import Http404
from cities_light.models import City, Country
from .models import *
from datetime import datetime

def home(req):
    return render(req,'app/navbaar/home.html')

def search(request):
    return render(request,'app/search/search.html')

def city_search(request):
    query = request.GET.get('q', '')

    try: 
        india = Country.objects.get(pk=105)
        # Filter cities by name and country (India), case-insensitive
        cities = City.objects.filter(slug=query, country=india)
    except Country.DoesNotExist:
        raise Http404("Country 'India' not found in the database.")
    except Exception as e:
        # Handle other exceptions if needed
        print(f"An error occurred: {e}")
        raise Http404("An error occurred while processing the request.")

    print(cities) 
    return render(request, 'app/navbaar/home.html', {'cities': cities, 'query': query})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def all_city_data(request):
    india = Country.objects.get(name='India')
    cities = City.objects.filter(country=india)

    # Paginate the cities with 40 cities per page
    paginator = Paginator(cities, 40)
    page = request.GET.get('page', 1)

    try:
        cities = paginator.page(page)
    except PageNotAnInteger:
        cities = paginator.page(1)
    except EmptyPage:
        cities = paginator.page(paginator.num_pages)

    return render(request, 'app/search/search.html', {'cities': cities})


def admindash(requset):
    return render(requset,'app/Admin_content/admindash.html')

def create_movie_page(request):
    if request.method == 'GET':
        return render(request,'app/Admin_content/curd/add_movie.html')

def create_movie(request):
    languages = Language.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        release_date = datetime.strptime(request.POST['release_date'], "%Y-%m-%d").date()
        director = request.POST['director']
        description = request.POST['description']
        poster = request.FILES['poster'] if 'poster' in request.FILES else None
        language_id = request.POST.get('language')

        
        new_movie = Movie.objects.create(
            title=title,
            release_date=release_date,
            director=director,
            description=description,
            poster=poster,
            language_id=language_id
        )

        return render(request, 'app/Admin_content/list_movie.html')

    
    
    return render(request, 'app/Admin_content/list_movie.html', {'languages': languages,'movie_data':new_movie})


     
def update_movie(request):
    
    movie=Movie.objects.all()
    return render(request,'app/Admin_content/curd/update_movie.html',{'movie':movie})




























# def movies(requset):
#     if requset.method=='GET':
       

#        movies=Movie.objects.all()

     
