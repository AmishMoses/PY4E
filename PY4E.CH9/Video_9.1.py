#!/usr/env/ python
'''Dictionaries are the second types of collections we will be working with
A list is a linear collection of values thtat stay in order
A dictionary is a 'bag' of values, each with its own label (key:value)'''

def dict1():
    purse = dict() # same as saying purse = {}
    purse['Money'] = 12
    purse['Candy'] = 3
    purse['Tissues'] = 75
    print(purse) # Will print out our data collection in a Key:Value realation
    print(purse['Candy'])
    purse['Candy'] = purse['Candy'] + 2 # Dictionaires like lists are mutable so they can be changed
    print(purse)
'''Where lists use indexing ie: purse[1] = 3 
Dictionaries use labels ie: purse['Key'] = value'''
dict1()   

def constantdict():
    friendage = {'Chuck': 25, 'Rob': 42, 'Dave': 30}
    print(friendage)
    friendage['Chuck'] += 20 # Is the same as friendage['Chuck'] + 20
    print(friendage)
constantdict()
