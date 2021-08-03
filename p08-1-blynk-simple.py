import blynklib_mp as blynklib

BLYNK_AUTH = 'YourAuthToken'

blynk = blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
