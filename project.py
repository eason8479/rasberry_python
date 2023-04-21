import time
import requests
import json

firebase_url = 'https://projectusm-7209a-default-rtdb.firebaseio.com//'

# return 0 for manual mode; retrun 1 for auto mode
def state_detate():
    get_data = requests.get(firebase_url+'a.json').json()
    return get_data['manual']

# save one thing to firebase
def save_one(tag, data):
    return_data = {tag: data}
    requests.patch(firebase_url+'a.json', data=json.dumps(return_data))

# save everything to firebase
def save_all(dic):
    save_one('agv', dic['agv'])
    save_one('agv_buffer', dic['agv_buffer'])
    save_one('agv_arm', dic['agv_arm'])
    save_one('machine_door', dic['machine_door'])
    save_one('machine_buffer', dic['machine_buffer'])

# change one variable and do stuff fellow it
def change(variable_name, variable_value,delay=1):
    data_dictionary[variable_name] = variable_value
    save_one(variable_name,variable_value)
    time.sleep(delay)

def agv_arm_process():
    # move object from agv to machine
    change('agv_arm',1,0)
    change('agv_buffer',0,0)
    time.sleep(1)

    # agv arm move reach destination
    change('agv_arm', 2, 0)
    change('machine_buffer', 1, 0)
    time.sleep(1)

    # avg arm moving
    change('agv_arm',1)

    # arm move to default position
    change('agv_arm', 0)

    # close door
    change('machine_door', 0)

    # processing object...
    time.sleep(5)

    # open door
    change('machine_door', 1)

    # avg arm moving
    change('agv_arm',1)

    # avg arm take object from machine
    change('agv_arm', 2, 0)
    change('age_buffer', 0, 0)
    time.sleep(1)

    # avg arm moving
    change('agv_arm',1)

    # avg arm move to default position
    change('agv_arm', 1, 0)
    change('agv_buffer', 1, 0)
    time.sleep(1)

time.sleep(5)

if (state_detate() == 0):
    #initial status
    data_dictionary = {
        # agv (0:agv is not at machien; 1: agv is at machine)
        'agv' : 0,
        # agv buffer(0: nothing on the agv, 1: something on the agv)
        'agv_buffer' : 1,
        # machine arm(0: arm is at defult positon, 1: arm is moving, 2: arm is in macine)
        'agv_arm' : 0,
        # machine door(0: closed, 1: open)
        'machine_door' : 0,
        # machien buffer(0: nothing in the machine, 1: something in the machine)
        'machine_buffer' : 0
    }
    save_all()

    # agv in
    change('agv', 1)

    # machine door open
    change('machine_door', 1)
    machine_door = 1
    save_one('machine_door', machine_door)

    # detect if unwanted object is in the machine
    #   if yes, take it out
    #   if no, continue   
    
    # machine door close
    change('machine_door', 0)

    # agv put object in the machine
    agv_arm_process()

    # agv out
    change('agv', 0)

else:
    pass

print('finshed')
