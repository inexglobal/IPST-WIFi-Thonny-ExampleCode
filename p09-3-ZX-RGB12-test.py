# File: ZX-RGB12-test.py , By Opas Sirikunchittavorn
import time
from machine import Pin
from NeoPixelLib import NeoPixel
np = NeoPixel(Pin(19),12, brightness=0.1)
RED    = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN  = (0, 255, 0)
CYAN   = (0, 255, 255)
BLUE   = (0, 0, 255)
PURPLE = (180, 0, 255)
while True:
    np.fill(RED)
    np.write()
    time.sleep(1)
    
    np.fill(GREEN)
    np.write()
    time.sleep(1)
    
    np.fill(BLUE)
    np.write()
    time.sleep(1)
    
    np.fadeinout(PURPLE)
    np.cycle(YELLOW,100)
    np.bounce(CYAN,100)
    np.color_chase(YELLOW, 100)
    np.color_chase(CYAN, 100)
    np.color_chase(PURPLE, 100)
    np.rainbow_cycle(25)     