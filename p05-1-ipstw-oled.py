# ipstw-oled.py : Opas Sirikunchoittavorn
import ipstw
import time

w = ipstw.IPSTW()

w.fill(0)                #clear screen
w.text("123456789012345678",0,0*8)
w.text("    IPST WiFi",0, 1*8+2)
w.text('MicroPython',20,3*8)
w.text('TEMP: %.2f'%(25.555),20,6*8)
w.show()
time.sleep(2)

w.invert(1)
time.sleep(2)
w.invert(0)

w.fill(0)                         #clear screen
w.text("IPST WiFi",0,0*8)
w.line(0,12,72,12,1)              #draw a line 
w.hline(10,32,108,1)              #draw a horizontal line
w.vline(64,12,64,1)               #draw a vertical line
w.fill_rect(59,27,10,10,1)        #draw a rectangle
w.rect(56,24,16,16,1)             #draw a rectangle frame
w.fill_rect(59,27,10,10,1)
w.fill_rect(88,0,40,20,1)
w.line(88,0,128,20,0)             #draw a line
w.line(88,20,128,0,0)
w.show()
