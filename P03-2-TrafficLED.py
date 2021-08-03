# TrafficLED.py : By Opas Sirikunchittavorn
import ipstw
import time
redLED    = 19
yellowLED = 23
greenLED  = 5
w = ipstw.IPSTW()

while True:
    w.output(redLED,1)
    time.sleep(3)
    w.output(redLED,0)
    
    w.output(greenLED,1)
    time.sleep(5)
    w.output(greenLED,0)

    w.output(yellowLED,1)
    time.sleep(1)
    w.output(yellowLED,0)
