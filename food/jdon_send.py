import requests
import json
response=requests.post("https://crm-back.prolabagency.com/api/v1/directions/",data=data)
print(response.json())
