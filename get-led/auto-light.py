import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
photo = 6
GPIO.setup(photo, GPIO.IN)
while True:
    if GPIO.input(photo):
        state = 0
    else:
        state = 1
    GPIO.output(led, state)