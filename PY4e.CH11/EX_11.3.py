#!/usr/bin/bash
import re
numlist = [] # Not sure whether to use a list or dict at the moment
numdict = {} # So using both until i can figure it out
sum = 0
name = input("Enter file:")
if len(name) < 1:
    name = "C:/Users/bigal/Desktop/PY4E/PY4e.CH11/data.txt"
handle = open(name)
'''for line in handle:
    line = line.strip() # Now we have our data read to lines
    for nums in line: # Iterate through lines to find pattern
        num = re.findall('[0-9]+', line) # Pattern should return 0-9+ any number 0-9 repeating
        if len(num) != 1: continue
        flt = int(num[0])
        numlist.append(flt) # And append the numbers to a list so i can calculate sum
print(sum(numlist))
print(len(numlist))
print(numlist)'''
# But for some reason i'm getting a ton of [] empty list items
# Tried using re.findall('[^\s][0-9]+.[0-9]+') to search for only non-whitespace but am still missing something
# Tried ('[0-9]+.\S') # Started giving me .... 

# Getting sum of 4687043 which is wrong 
# Should end in 884 
for line in handle:
    num = re.findall('[0-9]+', line) # Pattern should return 0-9+ any number 0-9 repeating
    numlist = numlist + num # Apend wouldn't work in the situation NoneType has no append attribute 
    print(numlist) # ALl data is in one list, must be transformed to perform sum 
for data in numlist: # Data is our iteration variable
    sum = sum + int(data) # Parsing through the list and making each element an int before adding to var(sum)
print(sum) # Correct 399884



'''
We do not use num+numlist. Concatenation is not needed. What ONE line of code to do we write to loop over a list to
 get individual strings?
 Delete everything after the num=re.findall(). We do not need lists, conditionals, or index positions.

Findall() returns lists exactly like split() does. What did we do in assignment 8.4 to go from a list 
of words to individual words?'''








'''Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers 
in the file and compute the sum of the numbers.
Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a
regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.'''