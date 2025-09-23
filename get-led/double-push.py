import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
leds = [24,22,23,27,17,25,12,16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
up = 9
down = 10
GPIO.setup(up,GPIO.IN)
GPIO.setup(down,GPIO.IN)
num = 0
sleep_time = 0.2

while True:
    if (GPIO.input(up) & GPIO.input(down)):
        num = 255
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    elif GPIO.input(up):
        if (num == 255):
            num = 0
            time.sleep(sleep_time)
        if (num >= 0 & num<255):
            num+=1
            print(num, dec2bin(num))
            time.sleep(sleep_time)
    elif GPIO.input(down):
        if (num == 0):
             time.sleep(sleep_time)
        elif (num >= 1 & num<=255):
            num-=1
            print(num, dec2bin(num))
            time.sleep(sleep_time)
    const = 0
    for led in leds:
        if dec2bin(num)[const]:
            GPIO.output(led,1)
        else:
            GPIO.output(led,0)
        const+=1
    