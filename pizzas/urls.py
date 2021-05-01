from django.urls import path
from . import views 

app_name = 'pizzas'

url.patterns = [
    path('', views.index, name='index'),
]