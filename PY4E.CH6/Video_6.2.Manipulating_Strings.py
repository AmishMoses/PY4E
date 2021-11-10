#!/usr/env python
'''Using in as a logical operator'''
def quick():
    fruit = "Bananas"
    print('n' in fruit) # Returns a boolean
quick()

print('\n')

'''Python has a number of string functions which are built in the string library
These functions do not modify the original string,  instead they return a new string that has been altered'''
def altered_string():
    greeting = "Hello Bob !"
    print(greeting.upper())
    print(greeting.lower())
    print(greeting.title())
    print(greeting.strip(' Bob! '))
    print(greeting.split())
    print(greeting.splitlines())
altered_string()

print('\n')

'''We can use the find() function to search for a substring within another string
find() finds the first occurrence of the substring and if not found return -1'''
def searching():
    fruit = 'Blueberry'
    location = fruit.find('er')
    print(location)
    noluck = fruit.find('z')
    print(noluck)
searching() # To find more than one occurrence you will need to use RegEx

print('\n')

'''The replace() function is like a "search and replace" operation
it replaces all occurrences of the search string with the replacement string'''
def replacements():
    tbr = "Hello Bob"
    replacement = tbr.replace('Bob', 'Jane')
    print(replacement)
replacements()

print('\n')

"""lstrip() and rstrip() remove whitespace at the left or right while strip() removes both"""
def stripping():
    tbs = '         This has a lot of whitespace to the left and right              '
    print(tbs.lstrip())
    print(tbs.rstrip())
    print(tbs.strip())
stripping()

print('\n')

'''To find if a line startswith a character user startswith() this will return a boolean'''
def start():
    line = "Hello and welcome to the show"
    print(line.startswith('Hello'))
    print(line.startswith('h'))
start()

print('\n')

"""Parsing and Extracting"""
def pande():
    data = "from stephen.marshall@uct.ac.za Sat Jan 5 09:14:17 2021"
    atsign = data.find('@') # this will find the index position of @ and assign it to the variable atsign
    print(atsign)
    space = data.find(' ', atsign) # In this case atsign is the start postition and a space ' ' is the end
    print(space)
    print(data[atsign:space]) # Now that we have assigned those positions as variables we can access them by splicing
pande()