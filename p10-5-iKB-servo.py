# iKB-servo.py : Opas Sirikunchittavorn
import ikb
import time

servoPin = 10
sw1Pin = 1
sw2Pin = 2

k = ikb.IKB()
k.begin()

k.servo(servoPin, 5)
while True:
    status = k.input(sw1Pin)
    if status == 0:
        k.servo(servoPin, 100)
        
    status = k.input(sw2Pin)
    if status == 0:
        k.servo(servoPin, 5)
    time.sleep(0.1)
