# ikb-blink LED : Opas Sirikunchittavorn
import ikb
import time

ledPin = 0

k = ikb.IKB()
k.begin()

while True:
    k.output(ledPin, 1)
    print("iKB pin 0 On")
    time.sleep(0.5)
    
    k.output(ledPin, 0)
    print("iKB pin 0 Off")
    time.sleep(0.5)
