from dnacentersdk import DNACenterAPI

dnacConnection = DNACenterAPI(base_url="https://dnac.jefferson.edu", username="rnm008", password="J0hnny18091@3", verify=False, version="2.3.5.3")

devices = [] # Store all devices in this variable

"""
for i in range(1, 50000, 500): # Start at 1, move up to 50k by 500 increments
    devices_part = dnacConnection.devices.get_device_list(offset=i,limit=500)["response"] # Get from DNAC and only store the data we care about
    if(devices_part): # If there is devices being returned
        devices += devices_part # save them
    else: # otherwise, there are no more devices to get
        break # end the loop
"""

for i in range(1, 50000, 500): # Start at 1, move up to 50k by 500 increments
    devices_part = dnacConnection.devices.get_device_list(offset=i,limit=500)["response"] # Get from DNAC and only store the data we care about
    for dev in devices_part:
        if "OOB" in dev["hostname"]:
            print(f"{dev['hostname']},{dev['managementIpAddress']}")
