import time
import requests
import json
import RPi.GPIO as GPIO
import logging

# set path of log file
log_file = '/media/pi/log_usb1/test.log'
# set format of log
log_format = '%(asctime)s  %(levelname)s %(message)s'
# set level of log
log_level = logging.INFO
# set log
logging.basicConfig(filename=log_file, format=log_format, level=log_level)

# set up for raspberry pi and firebase
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pin 17,27 is for door
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
# pin 2,3 is for arm claw
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

firebase_url = 'https://projectusm-7209a-default-rtdb.firebaseio.com//'

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

# return 0 for manual mode; retrun 1 for auto mode
def state_detate():
    get_data = requests.get(firebase_url+'a.json').json()
    return get_data

# save one thing to firebase
def save_one(tag, data):
    return_data = {tag: data}
    requests.patch(firebase_url+'a.json', data=json.dumps(return_data))

# save everything to firebase
def save_all(dic):
    save_one('agv', dic['agv'])
    save_one('agv_buffer', dic['agv_buffer'])
    save_one('agv_arm', dic['agv_arm'])
    save_one('agv_claw', dic['agv_claw'])
    save_one('machine_door', dic['machine_door'])
    save_one('machine_buffer', dic['machine_buffer'])

# change one variable and do stuff fellow it
def change(variable_name, variable_value,delay=1):
    data_dictionary[variable_name] = variable_value
    save_one(variable_name,variable_value)
    time.sleep(delay)

def agv_arm(mission):
    if (mission == 'put_in'):
        # open door
        door_open()
        change('machine_door', "1")
        logging.info('door open, ready to put in')

        # agv arm grap object
        change('agv_claw', "1", 0)
        change('agv_buffer', "0", 0)
        agv_claw_close()
        time.sleep(1)

        # move object from agv to machine
        change('agv_arm', "1", 0)
        
        # agv arm move reach destination, open claw
        change('agv_claw', "0", 0)
        change('agv_arm', "2", 0)
        change('machine_buffer', "1", 0)
        agv_claw_open()
        logging.info('object on machine')
        time.sleep(1)

        # avg arm moving back
        change('agv_arm', "1")
        time.sleep(1)

        # arm move to default position
        change('agv_arm', "0")
        # close door
        door_close()
        change('machine_door', "0")
        logging.info('door close, ready for processing')
        time.sleep(1)

    elif (mission == 'take_out'):
        # open door
        door_open()
        change('machine_door', "1")
        logging.info('door open, ready to take out')
        time.sleep(1)

        # avg arm moving
        change('agv_arm', "1")
        time.sleep(1)

        # avg arm take object from machine, close claw
        agv_claw_close()
        change('agv_claw', "1", 0)
        change('agv_arm', "2", 0)
        change('machine_buffer', "0", 0)
        logging.info('object takeing out form machine')
        time.sleep(1)

        # avg arm moving
        change('agv_arm', "1")

        # avg arm move to default position, claw open, object on agv
        agv_claw_open()
        change('agv_claw', "0", 0)
        change('agv_arm', "0", 0)
        change('agv_buffer', "1", 0)
        time.sleep(1)

        # close door
        door_close()
        change('machine_door', "0")
        logging.info('door close, processing finshed')
        time.sleep(1)
    
time.sleep(5)

#initial status
data_dictionary = {
    # agv (0:agv is not at machien; 1: agv is at machine)
    'agv' : "0",
    # agv buffer(0: nothing on the agv, 1: something on the agv)
    'agv_buffer' : "1",
    # machine arm(0: arm is at defult positon, 1: arm is moving, 2: arm is in macine)
    'agv_arm' : "0",
    # agv claw(0: claw is open, 1: claw is close)
    "agv_claw" : "0",
    # machine door(0: closed, 1: open)
    'machine_door' : "0",
    # machien buffer(0: nothing in the machine, 1: something in the machine)
    'machine_buffer' : "0",
    # porcess(0: not processing, 1: processing)
    'process' : "0"
}
save_all(data_dictionary)

while True:
    time.sleep(1)

    if (state_detate()['manual'] == '\"0\"'):
        if (state_detate()['auto_start'] == '\"1\"'):
            # agv in
            change('agv', "1")

            agv_arm('put_in')

            # processing object...
            change('process', "1")
            logging.info('processing...')
            time.sleep(5)
            change('process', "0")
            logging.info('processing finshed')

            agv_arm('take_out')

            # agv out
            change('agv', "0")

            change('auto_start', "0")

    elif state_detate()['manual'] == '\"1\"':
        time.sleep(1)
        firebase_a = requests.get(firebase_url+'.json').json()['a']

        
        if firebase_a['agv_claw'] == '\"1\"':#close，夾
            agv_claw_close()
        else:
            agv_claw_open()
        
        if firebase_a['machine_door'] == '\"1\"':
            door_open()
        else:
            door_close()

