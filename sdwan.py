import requests
import pprint

url = "https://192.168.2.113:8443/dataservice/device"

payload = {}
headers = {
  'Cookie': 'JSESSIONID=V6zYPdfpmGLSDBaOLTz2CNrSrptTi-4Ru4OYqSfK.790f3192-9a07-48a3-ab4c-ade61ed1aa32'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

pprint.pp(response.text)
