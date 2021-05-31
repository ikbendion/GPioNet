import requests
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:5002/setpin"


# Test the post request
payload =  {
    "pin": "1",
    "state": "HIGH"
  },

response = requests.post(url, data=payload, auth=HTTPBasicAuth('user', 'password'))
if response.status_code == 200:
    print("[OK] POST Request works!")
else:
    print("[FAIL] There was a error completing the POST request. error code is "+str(response.status_code))

# test the get request
pin = str(5)
geturl = "http://127.0.0.1:5002/getpin?pin="
information = requests.get(geturl+pin, auth=HTTPBasicAuth('user', 'password'))
if information.status_code == 200:
    print("[OK] GET Request works!")
else:
    print("[FAIL] There was a error completing the GET request. error code is "+str(information.status_code))