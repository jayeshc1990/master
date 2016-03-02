import time
import requests
import shutil
import re
crontable = []
outputs = []
from slackclient import SlackClient

def process_message(data):
        token = "xoxb-111111111111-2222222222222222222"    #This is your own slack token
        sc = SlackClient(token)
        if data['text'].lower().startswith("hi") or data['text'].lower().startswith("hello"):
                print sc.api_call("users.info",user=data['user'])
                capturestring = sc.api_call("users.info",user=data['user'])
                namestring = re.split('"|:|,',capturestring)
                #print namestring[23]
                sendstring = "Hiii... %s. I am BOT." %namestring[23]
                outputs.append([data['channel'], sendstring])
