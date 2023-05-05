import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarning(False)

# pin 2 is for door
GPIO.setup(2, GPIO.OUT)
# pin 3 is for arm claw
GPIO.setup(3, GPIO.OUT)

def door_open():
    GPIO.output(2, GPIO.HIGH)

def door_close():
    GPIO.output(2, GPIO.LOW)

def arm_claw_open():
    GPIO.output(3, GPIO.HIGH)

def arm_claw_close():
    GPIO.output(3, GPIO.LOW)
