import requests

from .models import City
class Message:
    """Class for messages to user"""
    unauthorized = \
        'Only registered users can use service. Please register or login.'

    success_register = 'You have successfully registered'
    error_register = 'Registration error'
    city_does_not_exist = 'Such city does not exist!'
    city_alredy_added = 'City has already added recently!'
    city_successfully_added = 'City has already added!'
    city_removed = 'City has already removed!'


class WeatherInfo:
    """Class for weather details"""
    @staticmethod
    def weather_detail(url, current_user):
        """
        generates weather details for your city
        """
        all_cities = []
        cities = City.objects.filter(members=current_user)
        for city in cities:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
                'humidity': res['main']['humidity'],
                'pressure': res['main']['pressure'] / 10
            }
            all_cities.append(city_info)
        return all_cities