#!/usr/bin/bash
import re
print(sum(int(count) for count in re.findall('[0-9]+', open('C:/Users/bigal/Desktop/PY4E/PY4e.CH11/data.txt').read())))
'''oneliner code print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )'''
numlist = []
sum = 0
name = input("Enter file:")
if len(name) < 1:
    name = "C:/Users/bigal/Desktop/PY4E/PY4e.CH11/data.txt"
handle = open(name)

for line in handle:
    num = re.findall('[0-9]+', line) # Pattern should return 0-9+ any number 0-9 repeating
    numlist = numlist + num # Apend wouldn't work in the situation NoneType has no append attribute 
    print(numlist) # ALl data is in one list, must be transformed to perform sum 
for data in numlist: # Data is our iteration variable
    sum = sum + int(data) # Parsing through the list and making each element an int before adding to var(sum)
print(sum) # Correct 399884
# My code still apparently isn't streamlined, but the TA loves to say it's wrong and only give riddles about how to fix it 
# so it runs, it works, it stays. 



'''
We do not use num+numlist. Concatenation is not needed. What ONE line of code to do we write to loop over a list to
 get individual strings?
 Delete everything after the num=re.findall(). We do not need lists, conditionals, or index positions.

Findall() returns lists exactly like split() does. What did we do in assignment 8.4 to go from a list 
of words to individual words?'''








# Prompt 
'''Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers 
in the file and compute the sum of the numbers.
Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a
regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.'''