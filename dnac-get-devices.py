#Section place my imports
import requests
import json
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# DNAC INFORMATION
dnac_host = "dnac.sd-geeks.com"
dnac_username = "student"
dnac_password = "1234QWer"


# DEFINE MY HEADERS
headers = {
    "Content-Type":"application/json",
    "Accept":"application/json"
}

# URL for AUTHENTICATION API
auth_url = f"https://{dnac_host}/dna/system/api/v1/auth/token"

# Obtain a Token
response = requests.post(auth_url, auth=(dnac_username,dnac_password), headers = headers, verify=False)
if response.status_code == 200:
    token = response.json()["Token"]
    print(f"Successfully obtained token: {token}")
else:
    print(f"Failed to obtain token: {response.status_code} {response.text}")
    exit(1)


# X-Token-AUTH
headers["X-Auth-Token"] = token


# URL Get a list of Devices
devices_url = f"https://{dnac_host}/dna/intent/api/v1/network-device"


# Get the list of device from the DNAC
response = requests.get(devices_url, headers = headers, verify=False)


if response.status_code == 200:
    devices = (response.json()["response"])
else:
    print(f"Failed to retrieve device: {response.status_code}{response.text}")
    exit(1)

#Open a file
with open('dnac-device.txt', 'w') as file:
    file.write("List of Onboarded device:\n")
    for device in devices:
        device_info = f"Hostname: {device['hostname']}) IP:{device['managementIpAddress']}"
        file.write(device_info + "\n")

print("Device information has been written to dnac-devices.txt")





# Open a fie and save the information in that file
