#dht22.py : Opas Sirikunchittavorn
import time
from machine import Pin
import dht

d = dht.DHT22(Pin(23))
while True:
    d.measure()
    temp=d.temperature()
    hum =d.humidity()
    print("Temperature: %3.1f C" %(temp))
    print("Humidity: %3.1f %%" %(hum))
    time.sleep(2)
    