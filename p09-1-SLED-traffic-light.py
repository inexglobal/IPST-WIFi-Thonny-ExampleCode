# File: SELD-traffic-light.py,  By. Opas Sirikunchittavorn
from machine import Pin
import time
import NeoPixelLib
np = NeoPixelLib.NeoPixel(Pin(12), 3, brightness=0.3)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)

while True:
    np.clear()
    np[2]=RED
    np.write()
    time.sleep(3)

    np.clear()
    np[0]=GREEN
    np.write()
    time.sleep(5)

    np.clear()
    np[1]=YELLOW
    np.write()
    time.sleep(1)
    