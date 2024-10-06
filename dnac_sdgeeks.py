import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


dnac_username = "student"
dnac_password = "1234QWer"
dnac_host = "dnac.sd-geeks.com"


headers = {
    "Content-Type":"application/json",
    "Accept":"application/json"
}

url_auth = f"https://{dnac_host}/dna/system/api/v1/auth/token"

results = requests.post(url_auth, auth=(dnac_username, dnac_password), headers = headers,verify=False)

token = results.json()['Token']

headers['X-Auth-Token'] = token

device_url = f"https://{dnac_host}/dna/intent/api/v1/network-device"

devices = requests.get(device_url, auth=(dnac_username, dnac_password), headers = headers,verify=False)

print(devices.json()['response'])

for device in devices.json()['response']:
    print(f"hostname is {device['hostname']} IP address is: {device['managementIpAddress']}")











