# iKB-analog-in LED : Opas Sirikunchittavorn
import ikb
import time

ledPin = 0
analogPin =2

k = ikb.IKB()
k.begin()

while True:
    ain = k.analog(analogPin)
    print("Analog input = ", ain)
    k.output(ledPin, 1)
    time.sleep_ms(ain)
        
    k.output(ledPin, 0)
    time.sleep_ms(ain)

