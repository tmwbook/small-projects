__author__ = "thomas"

import requests
import json




requestParam = {'OAuth': appId}


r = requests.delete('https://api.twitch.tv/kraken/users/failfixer89/follows/channels/shotbownetwork_official', params=requestParam)

re = requests.get('https://api.twitch.tv/kraken/users/failfixer89/follows/channels')
data = json.loads(re.content)

for channel in data['follows']:
    print channel['_links']
