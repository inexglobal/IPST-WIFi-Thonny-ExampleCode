# Blynk-01.py : Opas Sirikunchittavorn
# push button for control LED at IPST WiFi
import blynklib_mp as blynklib
import network
import time
import ipstw
w = ipstw.IPSTW()

WIFI_SSID = 'H---------2'
WIFI_PASS = 'a------b'
BLYNK_AUTH = '-hYiM_dIll9o--------WLKmiySV8WFhj'
LED_PIN = 19

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

@blynk.handle_event('write V1')
def write_handler(pin, values):
    print(values)
    if values[0] == "1":
        w.output(LED_PIN,1)
    else:
        w.output(LED_PIN,0)
        
while True:
    blynk.run()
