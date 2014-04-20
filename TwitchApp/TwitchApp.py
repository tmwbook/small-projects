__author__ = "thomas"

import requests
import json

requestParam = {}

r = requests.get('https://api.twitch.tv/kraken/chat/emoticons')

data = json.loads(r.content)

kappa = None

for emote in data['emoticons']:
    if emote['regex'] == 'Kappa':
        kappa = emote['images'][0]['url']
        print kappa
    else:
        continue

#print data['emoticons'][0]['regex']