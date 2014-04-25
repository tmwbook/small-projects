__author__ = "thomas"
import authentication

import requests
import json
import getpass


def getUsername():
    try:
        with open(authentication.workingDir + '/settings.ini', 'r') as var:
            user = var.readline()
            user.strip('\n')
            if user[0:7] == 'username':
                return user[9:]
    except IOError:
        user = raw_input('What is your username? ')
        return user


def getPassword():
    try:
        with open(authentication.workingDir + '/settings.ini', 'r') as var:
            var.readline()
            password = var.readline()
            if password[0:7] == 'password':
                return password[9:]
    except IOError:
        print 'hrere'
        password = getpass.getpass('Enter your password (will not be shown on screen) ')
        return password


authRequest = {'grant_type': 'password',
               'client_id': authentication.appID,
               'client_secret': authentication.secretID,
               'username': getUsername(),
               'password': '',
               'scope': 'user_follows_edit user_subscriptions'}


requestParam = {}

r = requests.post('https://api.twitch.tv/kraken/oauth2/token', params=authRequest)

token = json.loads(r.content)

print token
