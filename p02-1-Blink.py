#Blink.py : Opas Sirikunchittavorn
import ipstw
import time
w = ipstw.IPSTW()
led = 18

while True:
    w.output(led, 1)
    print("LED on")
    time.sleep(0.5)
    w.output(led, 0)
    print("LED off")
    time.sleep(0.5)
    