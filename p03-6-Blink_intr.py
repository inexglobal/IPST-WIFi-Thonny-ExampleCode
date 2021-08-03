# Blink_intr.py : By Opas Sirikunchittavorn
import time
import ipstw

w=ipstw.IPSTW()

button = 35
led = 18
counter = 0

def intr_func(e):
    time.sleep_ms(10)
    if w.input(button) == 0:
        global counter
        counter += 1
        print( counter )

w.exti(button,intr_func)

while True:
    w.output(led,1)
    time.sleep(0.5)
    w.output(led,0)
    time.sleep(0.5)
