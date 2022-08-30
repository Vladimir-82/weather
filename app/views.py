import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

from django.contrib import messages



def index(request):
    cities = City.objects.all()
    appid = '31bd6b6a3c005a57dc32dbd102f5b6b1'
    url = \
        'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' \
        + appid

    if (request.method == 'POST'):
        if request.POST.get('_method') == 'delete':
            city_name = request.POST.get('city_name', False)
            if city_name:
                cities.get(name=city_name).delete()
        else:
            form = CityForm(request.POST)
            city = form.name
            res = requests.get(url.format(city)).json()
            if res == {'cod': '404', 'message': 'city not found'}:
                messages.add_message(request, messages.INFO,
                                     'Such city does not exist!')
            else:
                form.save()
    else:
        form = CityForm()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'humidity': res['main']['humidity']
        }
        all_cities.append(city_info)
    context = {'all_cities': all_cities}

    return render(request, 'app/index.html', context)