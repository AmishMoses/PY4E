#!/usr/env python
# Parsing XML
import xml.etree.ElementTree as ET
# Like many things in Python one of the first things we will do is an import statement
data = '''
<person>
  <name>Alex</name>
  <phone type="intl">
  1 555 555 5555
  </phone>
    <email hide="yes"/>
</person>
'''
tree = ET.fromstring(data) # Take this string and gives us back a 'Tree'
print('Name:',tree.find('name').text) # Goes to the name branch and grabs the text which is Alex
print('Attr:',tree.find('email').get('hide')) # Goes to the Email node and grabs the attribute 
print('Num:',tree.find('phone').text) # Prints Number

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Alex</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Chuck</name>
    </user>
  </users>
</stuff>
'''
stuff = ET.fromstring(input) # Takes data and gives us a tree
lst = stuff.findall('users/user') # [<Element 'user' at 0x000002B0B1D43540>, <Element 'user' at 0x000002B0B1D43630>]
print('The user count is:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attr:', item.get("x")) 
