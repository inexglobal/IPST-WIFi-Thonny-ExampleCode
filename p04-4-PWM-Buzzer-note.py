# PWM-buzzer-note.py : By Opas Sirikunchittavorb
import ipstw
from micropython import const

w = ipstw.IPSTW()

DO =const(523)
RE =const(587)
ME =const(659)
FA =const(698)
SO =const(783)
RA =const(880)
TE =const(987)

note = [DO,0.5, RE,0.5, ME,0.5, FA,0.5, SO,0.5, RA,0.5, TE,0.5]

for i in range (0, len(note), 2) :
    w.sound(note[i], note[i+1])
