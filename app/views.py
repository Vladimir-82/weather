import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import *
from .utils import Message

def index(request):
    current_user = request.user.id
    cities = City.objects.filter(members=current_user)
    appid = '31bd6b6a3c005a57dc32dbd102f5b6b1'
    url = \
        'https://api.openweathermap.org/data/2.5/weather?q={}&units=' \
        'metric&appid=' + appid

    if request.method == 'POST':
        if request.POST.get('_method') == 'delete':
            city_name = request.POST.get('city_name', False)
            if city_name:
                cities.filter(name=city_name).delete()
        else:
            form = CityForm(request.POST)
            if form.is_valid():
                city = request.POST['name']
                res = requests.get(url.format(city)).json()
                if res == {'cod': '404', 'message': 'city not found'}:
                    messages.add_message(request, messages.INFO,
                                         'Such city does not exist!')
                else:
                    new_city = City.objects.create(name=city)
                    new_city.members.add(current_user)
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
    context = {'all_cities': all_cities, 'form': form}

    return render(request, 'app/index.html', context)


def register(request):
    '''
    Registration of service users
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, Message.success_register)
            return redirect('/')
        else:
            messages.error(request, Message.error_register)
    else:
        form = UserRegisterForm()
    return render(request, 'app/register.html', {"form": form})


def user_login(request):
    '''
    Service user logging
    '''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'app/login.html', {"form": form})


def user_logout(request):
    '''
    Unlogging service users
    '''
    logout(request)
    return redirect('login')