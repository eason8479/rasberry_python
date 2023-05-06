import time
import requests
import json

firebase_url = 'https://projectusm-7209a-default-rtdb.firebaseio.com//'

def door_open():
    pass

def door_close():
    pass

def arm_claw_open():
    pass

def arm_claw_close():
    pass

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

        # agv arm grap object
        change('agv_claw', "1", 0)
        change('agv_buffer', "0", 0)
        arm_claw_close()
        time.sleep(1)

        # move object from agv to machine
        change('agv_arm', "1", 0)
        
        # agv arm move reach destination, open claw
        change('agv_claw', "0", 0)
        change('agv_arm', "2", 0)
        change('machine_buffer', "1", 0)
        arm_claw_open()
        time.sleep(1)

        # avg arm moving back
        change('agv_arm', "1")

        # arm move to default position
        change('agv_arm', "0")

        # close door
        door_close()
        change('machine_door', "0")

    elif (mission == 'take_out'):
        # open door
        door_open()
        change('machine_door', "1")

        # avg arm moving
        change('agv_arm', "1")

        # avg arm take object from machine, close claw
        arm_claw_close()
        change('agv_claw', "1", 0)
        change('agv_arm', "2", 0)
        change('machine_buffer', "0", 0)
        time.sleep(1)

        # avg arm moving
        change('agv_arm', "1")

        # avg arm move to default position, claw open, object on agv
        arm_claw_open()
        change('agv_claw', "0", 0)
        change('agv_arm', "0", 0)
        change('agv_buffer', "1", 0)
        time.sleep(1)

        # close door
        door_close()
        change('machine_door', "0")
    
time.sleep(5)

if (state_detate()['manual'] == '\"0\"'):
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
        'machine_buffer' : "0"
    }
    save_all(data_dictionary)

    # agv in
    change('agv', "1")

    agv_arm('put_in')

    # processing object...
    time.sleep(5)

    agv_arm('take_out')

    # agv out
    change('agv', "0")

else:
    while True:
        firebase_a = requests.get(firebase_url+'.json').json()['a']
        
        if firebase_a['agv'] == 1:
            print("agv=1")
        else:
            print("agv=0")

        if firebase_a['agv_arm'] == 1:
            print("agv_arm=1")
        else:
            print("agv_arm=0")

        if firebase_a['agv_buffer'] == 1:
            print("agv_buffer=1")
        else:
            print("agv_buffer=0")

        if firebase_a['agv_claw'] == 1:
            print("agv_claw=1")
        else:
            print("agv_claw=0")

        if firebase_a['machine_buffer'] == 1:
            print("machine_buffer=1")
        else:
            print("machine_buffer=0")

        if firebase_a['machine_door'] == 1:
            print("machine_door=1")
        else:
            print("machine_door=0")
