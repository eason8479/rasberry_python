import requests
import json
import time

firebase_url = 'https://projectusm-7209a-default-rtdb.firebaseio.com//'

def save_one(tag, data):
    return_data = {tag: data}
    requests.patch(firebase_url+'a.json', data=json.dumps(return_data))

def save_all(dic):
    save_one('agv', dic['agv'])
    save_one('agv_buffer', dic['agv_buffer'])
    save_one('agv_arm', dic['agv_arm'])
    save_one('machine_door', dic['machine_door'])
    save_one('machine_buffer', dic['machine_buffer'])

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

time.sleep(5)

save_all(data_dictionary)