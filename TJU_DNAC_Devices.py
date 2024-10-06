import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://dnac.jefferson.edu/dna/intent/api/v1/network-device?offset=1000"

payload = {}
headers = {
  'x-auth-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NDIxY2U2MGFmYmRjZDc2NjYxYzY2NWIiLCJhdXRoU291cmNlIjoiZXh0ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYyMzhlMjM5NjE4Y2EyNDljY2E1YWVlYyJdLCJ0ZW5hbnRJZCI6IjYyMzhlMjM5NjE4Y2EyNDljY2E1YWVlYSIsImV4cCI6MTcyNjc3NDk2NywiaWF0IjoxNzI2NzcxMzY3LCJqdGkiOiJhODk0ZGI3NS05NmU2LTQwZTQtODU2Ny0xMzhiYjMwMGJiYTUiLCJ1c2VybmFtZSI6InJubTAwOCJ9.W3hQU4ZTWu8aFkLdIWHo3dzLO3xjrImJuVebgPJTrh4-89X1YPAl26w7vPhxFtpTQn11fZ-A8h2FJpMthDLyesWfERYg9rvhpkB2RNDtZaey0U4Z1scwobwCVnbV6yfXnQMGFq6nmvxc_QYMZVD0ATsYxGOH04lkeBECu0FrviqvOZukI3UMAaDCAcPi6tRZl3OTGJARuFM7fA31E8GcoXtjZlMy-VLF03R4EnyMQazqES-7RA8fATbx9KRhLHEMRgdEnmF5gwzHznCZVf9tW_pQHBR0jKGKCWuwuCBA1wxySuWbmHqGd1x4_iJntGSFQbf31II11Zq87X9HvfXPwQ'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()

#print(response)
#print(response.text)
for device in response['response']:
    if "J" in device['hostname']:
        print({device['hostname']})
