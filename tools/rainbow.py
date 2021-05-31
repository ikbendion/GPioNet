import requests
from requests.auth import HTTPBasicAuth
import time

url = "http://10.0.1.169:5002/setpin"
list = [3,5,7,8,10]

while True:
    for item in list:
        item = str(item)
        response = requests.post(url+"?pin="+item+"&state=1", auth=HTTPBasicAuth('user', 'password'))
        print(response.elapsed)
    for item in list:
        item = str(item)
        response = requests.post(url+"?pin="+item+"&state=0", auth=HTTPBasicAuth('user', 'password'))
        print(response.elapsed)