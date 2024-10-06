import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://192.168.2.77/dna/intent/api/v1/network-device"

payload = {}
headers = {
          'x-auth-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NmUwZThhOTc3MjAwYzc3Njg2OWQxZjciLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjY2ZTBlOGE1NzcyMDBjNzc2ODY5ZDFmNiJdLCJ0ZW5hbnRJZCI6IjY2ZTBlOGE0NzcyMDBjNzc2ODY5ZDFmNCIsImV4cCI6MTcyNzgxNzYxMiwiaWF0IjoxNzI3ODE0MDEyLCJqdGkiOiJjZTI4Njg1Mi03MWI5LTRmNzAtODFiMS03YzAxYjRmYTliZDEiLCJ1c2VybmFtZSI6ImFkbWluIn0.J--2o4VZZ6z_TG6RsjhPcu7htKYYUTxNtOB96yixopWFy4i4M-vA89v0xYlytBt0kQadLv1DRi5oINXIBLBME49FZ1xyoMHG7eWCRE_ZpTOt2jCYWqBY4N92RXRa5jFbgQ1bj3kScYork3QfUVOZ3f8BNYX8i2VSkH_YBt2Ti58n5r-x1TSFpHFNLydge_momEbIIPtFnH_yDYwBjY9QfaaZU-iV1-vCwRk_2wnYHPQgdfHlVrjsSRB82wKG15qYJ2nSAbn0xWhEu9ON2v78tcuUpTtjrRjOtrhhZHNPPHSfHHh6b9fcCfgh3Nm0YHrGxoXh9kq2Bu0DJHS6_VlNYg'
          }

response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()

#print(response)

for dev in response['response']:
    print(f"{dev['managementIpAddress']}\t{dev['hostname']}\t{dev['softwareVersion']}")



