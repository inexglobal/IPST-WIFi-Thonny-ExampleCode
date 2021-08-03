# Blink2LED.py : By Opas Sirikunchittavorn

import time
from machine import Pin
led1 = Pin(19, Pin.OUT)
led2 = Pin(23, Pin.OUT)

while True:
    led1.value(1)
    print("led1 on")
    time.sleep(0.5)
    led1.value(0)

    led2.value(1)
    print("led2 on")
    time.sleep(0.5)
    led2.value(0)
    