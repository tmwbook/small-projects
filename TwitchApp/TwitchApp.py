__author__ = "thomas"

import requests
import json

requestParam = {}

r = requests.get('https://api.twitch.tv/kraken/teams/entertainment')

data = json.loads(r.content)

print data
