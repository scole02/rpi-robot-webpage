import pigpio
import time

pi = pigpio.pi()
led_pin = 14
pi.set_mode(led_pin, pigpio.OUTPUT)
pi.write(led_pin, 1)  # let there be light
time.sleep(1)
pi.write(led_pin, 0)
