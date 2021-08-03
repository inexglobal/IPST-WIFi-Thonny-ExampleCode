# adc-knob.py : Opas Sirikunchittavorn
import ipstw
import time

w = ipstw.IPSTW()

while True:
    valKnob = w.knob()
    volt = valKnob /4095 *3.3
    print("Knob = %d = %0.3f V" %(valKnob, volt))
    time.sleep(0.1)