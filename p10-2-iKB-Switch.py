# iKB-Switch : Opas Sirikunchittavorn
import ikb
import time

ledPin = 0
switchPin = 1

k = ikb.IKB()
k.begin()

while True:
    status = k.input(switchPin)
    if status == 0:
        print("Switch press")
        k.output(ledPin, 1)
    else:
        print("Switch not press")
        k.output(ledPin, 0)
    time.sleep(0.2)
