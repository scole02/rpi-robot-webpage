from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('motors', views.motors, name='motors'),
    path('sensors', views.sensors, name='sensors'),
    path('ajax/getGps', views.getGps, name='getGps'),
]