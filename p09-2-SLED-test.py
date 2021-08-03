# File: SELD-test.py,  By. Opas Sirikunchittavorn
from machine import Pin
import time
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(12), 3, brightness=0.3)

np.clear()
np.brightness=0.3
counter=2
while True:
    print("counter = ",counter)
    r=int(input("Enter red value   :"))
    g=int(input("Enter green value :"))
    b=int(input("Enter blue value  :"))
    print("np[%d] = (%d,%d,%d)" %(counter,r,g,b))
    print("\n")
    np[counter]=(r,g,b)
    np.write()
    counter = counter -1
    if counter < 0 :
        counter = 2
