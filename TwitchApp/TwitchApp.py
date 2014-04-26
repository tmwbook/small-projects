__author__ = "thomas"
import authentication

import requests
import json
import getpass
import subprocess
from sys import exit
from time import sleep

#take this out when settings.ini is finally formatted
username = ''
#list of channels that are live and that you follow
followingLive = {'name': [],
                 'url': [],
                 'game': []}


def getUsername():
    global username
    try:
        with open(authentication.workingDir + '/settings.ini', 'r') as var:
            user = var.readline()
            user.strip('\n')
            if user[0:7] == 'username':
                return user[9:]
    except IOError:
        user = raw_input('What is your username? ')
        #this will only print at the correct time now, but I need to move it somewhere else
        print 'Retrieving list of followed channels from Twitch...'
        username = user
        return user


def getPassword():
    try:
        with open(authentication.workingDir + '/settings.ini', 'r') as var:
            var.readline()
            password = var.readline()
            if password[0:7] == 'password':
                return password[9:]
    except IOError:
        password = getpass.getpass('Enter your password (will not be shown on screen) ')
        return password


def getFollowing():
    if len(username) > 0:
        following = requests.get('https://api.twitch.tv/kraken/users/'+username+'/follows/channels')
        followingData = json.loads(following.content)
        return followingData
    else:
        getUsername()
        following = requests.get('https://api.twitch.tv/kraken/users/'+username+'/follows/channels')
        followingData = json.loads(following.content)
        return followingData


def formatFollowing(following):
    """should take getFollowing() as arugment"""
    formatted = ''
    for channel in following['follows']:
        formatted += channel['channel']['display_name']+'\n'
    return formatted


def customHelp(command):
    if command == 'following':
        information = 'gives a list of channels that you follow\n'
        return information
    elif command == 'live':
        information = 'gives a list of channels you follow that are live\n'
        return information
    elif command == 'watch':
        information = 'launches a stream in VLC.  Requires VLC Media player and Livestreamer to be installed\n' \
                      'While stream is active, no other commands can be entered\n' \
                      'Syntax is "watch <number of stream>"\n'
        return information
    elif command == 'quit':
        information = 'quits the program\n'
        return information
    else:
        information = 'Commands are: quit, following, live, and watch.\n' \
                      'For more information, type help + command\n'
        return information


def whoFollowingIsLive(following):
    global followingLive
    print 'Retrieving list of followed streams that are currently live...'
    followingChannels = following['follows']
    stringForParams = ''
    for channel in followingChannels:
        stringForParams += channel['channel']['name']+','
    stringForParams = stringForParams.strip(',')
    #would be requestParams but it would shadow global right now
    sendParams = {'Accept': 'application/vnd.twitchtv.v2+json',
                  'channel': stringForParams}
    rawLive = requests.get('https://api.twitch.tv/kraken/streams', params=sendParams)
    live = json.loads(rawLive.content)
    for name, url, game in zip(live['streams'], live['streams'], live['streams']):
        followingLive['name'].append(name['channel']['name'])
        followingLive['url'].append(url['channel']['url'])
        followingLive['game'].append(game['channel']['game'])
    return followingLive


def formatLive(liveStreams):
    """should take whoFollowingIsLive() as the argument"""
    formatted = ''
    for x in range(len(liveStreams['name'])):
        formatted += str(x) + '.  ' + liveStreams['name'][x] + ' is playing ' + liveStreams['game'][x] + '\n'
    return formatted


def startLivestreamerSession(streamNumber):
    quality = raw_input('What quality setting would you like? (normally the settings are: low, medium, high, source) ')
    streamLink = followingLive['url'][streamNumber]
    command = 'livestreamer '+streamLink + ' ' + quality
    subprocess.check_output(command, shell=True)


if __name__ == '__main__':
    print 'Welcome to Failfixer\'s Twitch app!'
    commands = {'following': formatFollowing(getFollowing()),
                'live': formatLive(whoFollowingIsLive(getFollowing()))}
    while True:
        command = raw_input('Enter a command. ')
        if command[0:5] == 'watch':
            startLivestreamerSession(int(command[-1:]))
        elif command[0:4] == 'help':
            if len(command) > 4:
                print customHelp(command[5:])
                sleep(3)
            else:
                print customHelp('')
                sleep(3)
        elif command == 'quit':
            exit()
        elif command in commands:
            print commands[command]
            sleep(3)
        else:
            print 'Invalid command. Type "help" for help.\n'
            sleep(2)
            continue