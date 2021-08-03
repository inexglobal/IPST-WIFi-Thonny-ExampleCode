#dht22-new.py : Opas Sirikunchittavorn
import time
from machine import Pin
import dht

d = dht.DHT22(Pin(23))
while True:
    try:
        d.measure()
        temp=d.temperature()
        hum =d.humidity()
        print("Temperature: %3.1f C" %(temp))
        print("Humidity: %3.1f %%" %(hum))
        time.sleep(2)
    except OSError as e:
        print("Failed to read sensor.")