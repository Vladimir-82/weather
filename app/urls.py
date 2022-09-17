from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    # path('detail/', name='detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]