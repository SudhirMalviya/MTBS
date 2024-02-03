from django.shortcuts import render

# Create your views here.



from django.db.models import Q
from .models import Address
from cities_light.models import City, Country



def city_state_search(request):
    form_value = request.POST.get('search', '')
    results = None

    if form_value:
        search_query = form_value
            
        # Search for both city and state
        results = Address.objects.filter(
            Q(city__name__icontains=search_query) | Q(country__name__icontains=search_query)
        )

    return render(request, 'app/navbaar/base.html', {'form_value': form_value, 'results': results})



def home(req):
    return render(req,'app/navbaar/base.html')