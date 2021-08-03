import ipstw
import time

w=ipstw.IPSTW()

while True:
    w.fill(0)
    value = w.analog(34)
    volt = value / 4095 *3300
    volt = volt + 130
    temp = (volt-500)/10
    
    w.text("adc34= %4d mV" %volt,0,0)
    w.text("Temp = %0.2f C" %(temp),0,10)
    w.show()
    print("adc34= %4d mV, Temperarure = %0.2f C" %(volt,temp))
    time.sleep(1)
    