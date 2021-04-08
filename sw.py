import RPi.GPIO as GPIO
import time, os
from signal import pause

GPIO.setmode(GPIO.BCM)

mysw = 23
GPIO.setup(mysw, GPIO.IN)

try:
    while True:
        button_state = GPIO.input(mysw)
        button_string = "off"
        if button_state == 1:
            button_string = "on"
        print("button_state: "+button_string)
        time.sleep(5)

except keyboardInterrupt:
    GPIO.cleanup()
