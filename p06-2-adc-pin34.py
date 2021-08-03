# adc-pin34.py : Opas Sirikunchittavorn
import ipstw
import time

w = ipstw.IPSTW()
adcPin = 34

while True:
    val = w.analog(adcPin)
    volt = val /4095 *3.3
    print("ADC Pin34 = %d = %0.3f V" %(val, volt))
    w.fill(0)
    w.text("adc34 = %d"   %(val), 0, 3*8)
    w.text("      = %0.3f V" %(volt), 0, 4*8)
    w.show()
    time.sleep(0.1)