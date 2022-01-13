import requests 
import json
webhook_url="https://webhook.site/cecac731-bb66-46bf-84a7-19513312b099?"
data ={"name":"John", "age":30, "car":'No'}
r=requests.post(webhook_url,data=json.dumps(data),headers={'Content-Type':'application/json'})
