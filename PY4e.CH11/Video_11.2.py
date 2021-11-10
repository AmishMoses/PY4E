#!/usr/env python
import re
# Extracting Data
'''
re.search() returns a T/F depending on the patterns match
if we actually want the matching string to be extracted, we use re.findall()'''
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
z = re.findall('^M.\s.', x) # Start with ^M . include any char \s include whitespace . end with any char
novowel = re.findall('[^aeiou]', x) # Shows everything but vowels
vowels = re.findall('[aeiou]\S+', x) # Come back to this
print(vowels)

# Greedy Matching
# The repeat chars (* and +) push outward in both directions to match the largest string possible
x = 'From: Using the : char'
y = re.findall("^F.+:", x ) # This won't stop at the first : it will instead try to match the largest string possible
print(y)
z = re.findall('^F.+?:', x) # This is non-greedy and will end at the first : non-greedy = shortest
print(z)

# Fine Tuning string extraction
# Emails
x = 'Email from alexsemail@email.com'
y = re.findall('\S+@\S+', x) # \S+ one or more non-whitespace chars followed by @ followed by \S+ again
print(y)
z = re.findall('^from (\S+@\S+)', x) # This says find a line that ^ w/ From and space then extract the \S+@\S+ data from x
# () are not part of the match but they tell where to start and stop what string to extract
# Finding just the email after the @ 
a = re.findall('@(.*)', x) # start at @ extract (. any char * many occurences) from x
# [^ ] means not a blank char
y = re.findall('^From .*@([^ ]*)' , x)
# Says line will ^From <space> .* include any number of chars before @ then begin extracting
# ([^ ]*) says extract any non-blank char 0 or more times
print(a)
# If you want to match a wildcard just quote/escape the char with a \
money = 'I have $432.21'
m = re.findall('\$[0-9.]+', money) # find \$[0-9.]+ 0-9 including . repeating + one or more times
print(m)