# Blynk_DHT22.py : Opas Sirikunchittavorn
import blynklib_mp as blynklib
import blynktimer
import network
import time
import ipstw
from machine import Pin
import dht

WIFI_SSID = 'H--------2'
WIFI_PASS = 'a------b'
BLYNK_AUTH = '-hYiM_dIll--------0WLKmiySV8WFhj'
LED_PIN = 19          # LED or relay pin
DHT22_PIN = 23        # DHT22 Pin 19
T_VPIN=2              # Temp Virtual Pin2
H_VPIN=3              # Hum  Virtual Pin3

w = ipstw.IPSTW()
dht22 = dht.DHT22(Pin(DHT22_PIN))
timer = blynktimer.Timer()

print("Connecting to WiFi network '{}'".format(WIFI_SSID))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
    print('WiFi connect retry ...')
print('WiFi IP:', wifi.ifconfig()[0])

print("Connecting to Blynk server...")
blynk = blynklib.Blynk(BLYNK_AUTH)

@timer.register(interval=4, run_once=False)
def send_data():
    temperature = 0.0
    humidity = 0.0    
    # read sensor data
    try:
        dht22.measure()
        temperature = dht22.temperature()
        humidity = dht22.humidity()
    except OSError as o_err:
        print("Unable to get DHT22 sensor data: '{}'".format(o_err))

    if temperature != 0.0 and humidity != 0.0:
        blynk.virtual_write(T_VPIN, temperature)
        blynk.virtual_write(H_VPIN, humidity)

@blynk.handle_event('write V1')
def write_handler(pin, values):
    print(values)
    if values[0] == "1":
        w.output(LED_PIN,1)
    else:
        w.output(LED_PIN,0)
        
while True:
    blynk.run()
    timer.run()
