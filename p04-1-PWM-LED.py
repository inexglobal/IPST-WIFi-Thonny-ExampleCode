# PWM-LED.py
import ipstw
import time

w = ipstw.IPSTW()

pwmLED = 19  # Pin 19

while True:
    for x in range (0, 1024, 33):
        w.pwm(pwmLED, x)
        print("Duty = %4d" %(x))
        w.fill(0)
        w.text("Duty = %4d" %(x), 0, 4*8)
        w.show()
        time.sleep(0.05) 
