import requests
import time
from discord import Webhook, RequestsWebhookAdapter
import subprocess
import sys

url = str(input("Enter Profile URL:"))

while True: 
    print('Beginning file download with requests')
    
    r = requests.get(url)
    with open('/Users/Computer/Desktop/Notification/[profile.txt', 'wb') as f: #change this location to match yours!!
        f.write(r.content)   
    #opens text file and searches for a certain keyword
    with open('/Users/Computer/Desktop/Notification/[profile.txt', encoding="utf8") as f:#change this location to match yours!!
        if 'profile-avatar-status' in f.read():
            time.sleep(7)
            continue 
        else:
            webhook = Webhook.from_url("YOUR WEBHOOK HERE!!!!", adapter=RequestsWebhookAdapter()) # indent this to be in the else
            webhook.send("YOUR MESSAGE!!") 
            break
            