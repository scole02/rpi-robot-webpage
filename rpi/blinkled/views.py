from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blinkled.models import GPS
from datetime import datetime
from django.forms.models import model_to_dict
import random
import pigpio
import time
import qwiic_scmd


d1 = qwiic_scmd.QwiicScmd(0x5d)
d2 = qwiic_scmd.QwiicScmd(0x58)
d3 = qwiic_scmd.QwiicScmd(0x5b)
d1.begin()
time.sleep(0.1)
d2.begin()
time.sleep(0.1)
d3.begin()
time.sleep(0.1)
print("Drivers Initalized.")
d1.enable()
time.sleep(0.1)
d2.enable()
time.sleep(0.1)
d3.enable()
time.sleep(0.1)
print("Motors Enabled")
time.sleep(0.1)
# so motors all turn the same direction
d1.inversion_mode(1, 1)
d2.inversion_mode(0, 1)
d3.inversion_mode(1, 1)


pi = pigpio.pi()
led_pin = 14
pi.set_mode(led_pin, pigpio.OUTPUT)
pi.write(led_pin, 0)
LED_STATE = 0 # off



def index(request): # 127.0.0.1:8000/blinkled/

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

def sensors(request): # 127.0.0.1:8000/blinkled/sensors
    return render(request, 'sensors.html')

def getGps(request):
    gps = GPS(datetime=datetime.now().today(), lat=random.random(), long=random.random())
    gps_dict = model_to_dict(gps)
    return JsonResponse(gps_dict)

def motors(request): # 127.0.0.1:8000/blinkled/motors
    if 'DISTANCE' in request.GET:
        dist = int(request.GET['DISTANCE'])
        if dist <= 10 and dist >= 1:
            level =  100
            duration = 0.5 * dist
            for i in range(2):
                d1.set_drive(i, 0, level)
                d2.set_drive(i, 0, level)
                d3.set_drive(i, 0, level)
            
            time.sleep(duration)

            for i in range(2):
                d1.set_drive(i, 0, 0)
                d2.set_drive(i, 0, 0)
                d3.set_drive(i, 0, 0)
        
    elif 'TURN_DEGREES' in request.GET:
        degs = int(request.GET['TURN_DEGREES'])
        duration = 0.00666667 * degs
        level = 100
        
        # left
        d1.set_drive(1, 0, level)
        d2.set_drive(0, 0, level)
        d3.set_drive(0, 0, level)
        
        # right
        d1.set_drive(0, 0, level * -1)
        d2.set_drive(1, 0, level * -1)
        d3.set_drive(1, 0, level * -1)

        time.sleep(duration)

        for i in range(2):
            d1.set_drive(i, 0, 0)
            d2.set_drive(i, 0, 0)
            d3.set_drive(i, 0, 0)
                        

        else : # invalid distance do nothing
            pass            
    return render(request, 'motors.html')

# Create your views here.
