from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blinkled.models import GPS
from datetime import datetime
from django.forms.models import model_to_dict
import random
import pigpio

pi = pigpio.pi()
led_pin = 14
pi.set_mode(led_pin, pigpio.OUTPUT)
pi.write(led_pin, 0)
LED_STATE = 0 # off

def index(request):

    if 'LED_ON' in request.GET:
        pi.write(led_pin, 1)
        LED_STATE = 1
    
    elif 'LED_OFF' in request.GET:
        pi.write(led_pin, 0)
        LED_STATE = 0
    
    elif 'BRIGHTNESS' in request.GET:
        brightness = int(request.GET['BRIGHTNESS'])
        if brightness >= 0 and brightness <= 255:
            pi.set_PWM_dutycycle(led_pin, brightness)

    return render(request, 'buttons.html')

def sensors(request):
    return render(request, 'sensors.html')

def getGps(request):
    gps = GPS(datetime=datetime.now().today(), lat=random.random(), long=random.random())
    gps_dict = model_to_dict(gps)
    return JsonResponse(gps_dict)

# Create your views here.
