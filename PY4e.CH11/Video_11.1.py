#!/usr/env/ python
import re #before you can use regex you have to import it into python
'''Regular Expressions
Regex provides a concise and flexible means for matching strings of text
such as particular characters, words, or patters of characters.
Regex uses wildcards to match zero, one, or more characters

^ matches the beginning of a line
$ matches the end of a line
. matches any character
\s matches whitespace
\S matches non whitespace
* repeats a character 0 or more times
*? repeats a character 0 or more times (non-greedy)
+ repeats a character 1 or more times
+? repeats a character 1 or more times (non-greedy)
[aeiou] matches a single character in the listed set
[^xyz] matches a single character not in the listed set
[a-z0-9] the set of characters can include a range
( indicates where string extraction is to start 
) indicates where string extraction is to end'''

# You can use re.search() similar to find()
# You can use the re.findall() to extract portions of a string that match your regular expression
# Similar to the combination of find() and slicing: varname[:]
'''Using re.search()
for line in hand:
    line = line.strip()
    if re.search('From:', line): # Includes the variable line in the () instead of line.find('From: ')
        print(line)
        
Using re.search() like .startswith()
if re.search('^From:', line): # ^ means the beginning
    print(line)     

re.search('^x-\S+:', line) # ^Start with x- \S+ include any non-whitespace character one or more times end with :

'''