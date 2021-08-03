# btn_status.py : By Opas Sirikunchittavorn
import ipstw
import time

button = 0
led = 18
w=ipstw.IPSTW()

while True:
    status = w.input(button)
    if status == 0:
        print("Button pressed")
        w.output(led,1)
    else:
        print("Button not pressed")
        w.output(led,0)
    time.sleep(0.2)
