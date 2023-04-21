import requests
import json

firebase_url = 'https://projectusm-7209a-default-rtdb.firebaseio.com//'

get_data = requests.get(firebase_url+'a.json').json()
print(get_data['manual'])


