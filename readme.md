Install micropython on esp8266
-------------------
Best way is over Thonny and terminal.

Thonny say the connection on "configure interpreter" --> Port or WebREPL --> if not, try "install or update MicroPython"

Theoretical, you can install a MicroPython image with Thonny, all see very simple, but i confront a problem over Thonny: after flashing, 
the ESP8266 blink forever and nothing more is posible.

I try the flashing again with esptool.py and i have no problem. 


Install micropython Libreries on esp8266
--------------------
Easy copy the desired library on a sheet in Thonny, and with a connected ESP, try to "save as". A dialog ask if you want to save on computer or on device. Sure,
on device. 
After all, on your python program, you import from "machine" for all the include libraries on MicroPython, and from "filename" from some another
extern librery as "hcsr04.py" then we use on program: "from hcsr04 import HCSR04" where "HCSR04" is a class on "hcsr04.py"


First Experiment: ESP8266 + HCSR04 + MicroPython
--------------------
PinOUTs:
HCSR04 => ESP8266 => MiPy

gnd  =>  G

trig =>  D6 ==> 12

echo =>  D5 ==> 14

vcc  =>  Vin


CODE:
---------------------
# hcsr04_examp01.py
from machine import Pin
from machine import Timer
from hcsr04 import HCSR04

ultrasonic = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=1000000)

def timer0_callback(timer):
    print('Distance: {}cm'.format(ultrasonic.distance_cm()))
    
timer0 = Timer(0)
timer0.init(period=500, mode=Timer.PERIODIC, callback=timer0_callback)
