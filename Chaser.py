#!/usr/bin/python3
#pip install gpiozero

from gpiozero import LED
from time import sleep

led1 = LED()
led2 = LED()
led3 = LED()
led4 = LED()
led5 = LED()
led6 = LED()
led7 = LED()
led8 = LED()
led9 = LED()

sleeptime = 0.2

while True:
	led1.ON()
	sleep(sleeptime)
	led1.OFF()