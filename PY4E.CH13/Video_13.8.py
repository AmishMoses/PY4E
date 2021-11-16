#!/usr/env python
# Securing API Requests
'''
The compute resources to run these APIs are not 'free'
THe data provided by these APIs is usually valuable
The data providers might limit the number of requests per day, deman an API 'key',
or even charge for usage
They might change the rules as things progress
'''
import urllib.request, urllib.parse, urllib.error
import twurl # twurl is a library written by Dr Charles 
import json
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders()) # This is the line of code you use to get the headers from urllib
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])