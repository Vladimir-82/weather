import requests

from .models import City
class Message:
    """Class for messages to user"""
    unauthorized = (
        'Только зарегистрированные пользователи могу использовать '
        'сервис. Пройдите регистрацию или авторизацию.'
    )
    success_register = 'Вы успешно зарегистрировались'
    error_register = 'Ошибка регистрации'
    city_does_not_exist = 'Such city does not exist!'
    city_alredy_added = 'City has alredy added city recently!'
    city_successfully_added = 'You has successfully added new city!'
    city_removed = 'City removed!'


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
                'humidity': res['main']['humidity']
            }
            all_cities.append(city_info)
        return all_cities