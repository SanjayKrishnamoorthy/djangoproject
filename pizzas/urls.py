
from django.urls import path

from . import views
from django.conf import settings  
from django.urls import path, include 
from django.conf.urls.static import static  

app_name = 'pizzas'



urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
]

