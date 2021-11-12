#!/usr/env python
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>
'''

tree = ET.fromstring(data) # Read data and gives us back a tree object
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))


input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
tags = stuff.findall('users/user') # users is the parent object and user is the child
print('User count:', len(tags))

for tag in tags:
    print('Name', tag.find('name').text)
    print('Id', tag.find('id').text)
    print('Attribute', tag.get('x'))