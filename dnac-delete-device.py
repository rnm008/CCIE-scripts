# IMPORTS
import requests
import json
import urllib3

# DISABLE SSL WARNINGS
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# DNAC INFO
dnac_host = "192.168.2.70"
dnac_username = "bob"
dnac_password = "Nichol@s1"


# DEFINE HEADERS
headers = {
    "Content-Type":"application/json",
    "Accept":"application/json"
}


# URL FOR AUTHENTICATION API
auth_url = f"https://{dnac_host}/dna/system/api/v1/auth/token"


# OBTAIN A TOKEN
response = requests.post(auth_url, auth=(dnac_username,dnac_password), headers=headers, verify=False)
print(response)

"""
if response.status_code == 200:
    token = response.json()['Token']
    print(token)
else:
    print("Failed to retrieve token")



# X-Token-AUTH
headers["X-Auth-Token"] = token

# GET DEVICE URL
device_url = f"https://{dnac_host}/dna/intent/api/v1/network-device"

# GET DEVICE ID
response = requests.get(device_url, headers=headers, verify=False)
print(response.json())

# DELETE DEVICE

url = "/dna/intent/api/v1/network-device/{id}"

payload = '''{}'''

headers = { "Accept": "application/json" }

response = requests.request('DELETE', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

"""