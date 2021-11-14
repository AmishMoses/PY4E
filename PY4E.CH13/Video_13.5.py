#!/usr/env python
# JavaScript Object Notation (JSON)
'''
JSON was invented by the CONSTANT syntax in JS 
XML is more powerful than we need on a day to day basis so JSON is the default serialization tool of today
'''
import json 
# JSON represents data as nested "lists" and "dictionaries" 
# In JS a dictionary is an 'object'
data = '''{
    "name" : "Alex",
    "phone" : {
        "type" : "intl",
        "number" : "555-555-5555"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
info = json.loads(data) # Loads means load from string
print(data)
print('Name:',info["name"])
print("Hide attr Y/N?", info['email']['hide'])
print("My number is:",info['phone']['number'])

input = '''[
    {"id" : "001",
    "x" : "2",
    "name" : "Alex"
    },
    {"id" : "002",
    "x" : "7",
    "name" : "Chuck"
    }
]'''
info2 = json.loads(input)
print("User count is:",len(info2)) # Info is a list with 2 dictionaries
for items in info2:
    print('Name:', items['name'])
    print('X number:', items['x'])
    print('ID:', items['id'])