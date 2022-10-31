from django.shortcuts import render
from django.http import HttpResponse
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
# Create your views here.
