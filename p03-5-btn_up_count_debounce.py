# btn_up_count_debounce.py : By Opas Sirikunchittavorn
import ipstw
import time

button = 0
led = 18
past_value = 1
cur_value  = 1
counter    = 0
state      = 0
w=ipstw.IPSTW()

while True:
    cur_value = w.input(button)
    
    if (cur_value == 0) and (past_value==1):
        time.sleep_ms(10)
        if(w.input(button) == 0):
            counter = counter +1
            print("Counter =", counter)
            state = not state
            w.output(led,state)
    past_value = cur_value
    