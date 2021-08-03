# PWM2-LED.py
import ipstw
import time

w = ipstw.IPSTW()

pwmLED1 = 19  # Pin 19
pwmLED2 = 23  # Pin 23

while True:
    for x in range (0, 1024, 33):
        w.pwm(pwmLED1, x)
        w.pwm(pwmLED2, 1023 - x)
        print("Duty x = %4d" %(x))
        w.fill(0)
        w.text("Duty x = %4d" %(x), 0, 4*8)
        w.show()
        time.sleep(0.05) 
