# iKB-motor.py : Opas Sirikunchittavorn
import ikb
import time

motorPin = 1

k = ikb.IKB()
k.begin()

while True:
    k.motor(motorPin, 0)
    time.sleep(1)
    k.motor(motorPin, 50)
    time.sleep(5)
    k.motor(motorPin, 100)
    time.sleep(5)

    k.motor(motorPin, 0)
    time.sleep(1)
    k.motor(motorPin, -50)
    time.sleep(5)
    k.motor(motorPin, -100)
    time.sleep(5)

