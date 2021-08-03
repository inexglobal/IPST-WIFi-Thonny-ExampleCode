# ADC-PWM.py
import ipstw
import time

w = ipstw.IPSTW()

pwmLED = 19  # Pin 19
adcPin = 34

while True:
    value = w.analog(adcPin)
    value = int(value / 4)
    w.pwm(pwmLED,value)
    print("PWM = ", value) 
    time.sleep(0.1)