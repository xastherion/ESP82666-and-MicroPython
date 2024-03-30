# hcsr04_examp01.py
# Connect hcsr04_echo_pin to D5 und _trigger_pin to D6
from machine import Pin
from machine import Timer
from hcsr04 import HCSR04

ultrasonic = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=1000000)

def timer0_callback(timer):
    print('Distance: {}cm'.format(ultrasonic.distance_cm()))
    
timer0 = Timer(0)
timer0.init(period=500, mode=Timer.PERIODIC, callback=timer0_callback)
