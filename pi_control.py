import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# pin 2 is for door
GPIO.setup(2, GPIO.OUT)
# pin 3 is for arm claw
GPIO.setup(3, GPIO.OUT)

def door_open():
    GPIO.output(2, GPIO.HIGH)

def door_close():
    GPIO.output(2, GPIO.LOW)

def agv_claw_open():
    GPIO.output(3, GPIO.HIGH)

def agv_claw_close():
    GPIO.output(3, GPIO.LOW)

door_close()
agv_claw_close()

while(1):
    door_open()
    time.sleep(5)
    agv_claw_open()
    time.sleep(5)
    door_close()
    time.sleep(5)
    agv_claw_close()
    time.sleep(5)

