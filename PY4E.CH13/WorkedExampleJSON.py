#!/usr/env python
import json
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
info = json.loads(data)
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
# print(info2) # [{'id': '001', 'x': '2', 'name': 'Alex'}, {'id': '002', 'x': '7', 'name': 'Chuck'}]
for items in info2:
    print('Name:', items['name'])
    print('X number:', items['x'])
    print('ID:', items['id'])