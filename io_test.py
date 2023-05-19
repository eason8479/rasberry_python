import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pin 17,27 is for door
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
# pin 2,3 is for arm claw
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

def door_open():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)

def door_close():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)

def agv_claw_open():
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.HIGH)

def agv_claw_close():
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    
    

while True:
    object = input("which one?")
    if (object == "door"):
        i = input("On or off?")
        if (i == "on"):
            door_open()
        elif (i == "off"):
            door_close()
        else:
            break

    elif (object == "claw"):
        i = input("On or off?")
        if (i == "on"):
            agv_claw_open()
        elif (i == "off"):
            agv_claw_close()
        else:
            break
    
    else:
        break


