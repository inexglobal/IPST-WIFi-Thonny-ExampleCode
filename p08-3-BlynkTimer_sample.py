# BlynkTimer_sample.py : Opas Sirikunchittavorn
import blynktimer
import random

timer = blynktimer.Timer()

@timer.register(interval=4, run_once=False)
def send_data():
    value = random.randint(0, 10)
    print(value)
        
while True:
    timer.run()
