import RPi.GPIO as GPIO
import time, os
from signal import pause

GPIO.setmode(GPIO.BCM)

myled = 18

GPIO.setup(18, GPIO.OUT)

try:
    while True:
        for i in range(0,100):
            GPIO.output(myled,i%2)
            time.sleep(0.30)
except keyboardInterrupt:
        GPIO.cleanup()

