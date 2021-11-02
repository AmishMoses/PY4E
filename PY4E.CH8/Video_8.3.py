#!/usr/env/ python
'''Split breaks a string into parts and produces a list of strings. We think of these as words
We can access a particular word or loop through all the words'''
def splitting():
    string = 'This is a normal string'
    split = string.split() # Makes the string a list and now each word is an element and indexable
    print(len(split))
    print(split[1])
    for words in string: 
        print(words) # The spaces count as an additional element 
    '''When you do not specify a delimiter, multiple spaces are treated as one delimiter.
    You can specify what delimeter character to use in splitting'''
    line = 'A lot        of          spaces'
    etc = line.split()
    print(etc) # The spaces are dropped
    line = 'first;second;third' # At the moment this is one element so spltting would not help
    etc = line.split()
    print(etc)
    print(len(etc))
    etc = line.split(';') # This is known as selecting the delimiter which by default is space
    print(etc)
    print(len(etc))
splitting()

print('\n')
def double_split_patteren():
    data = 'From someemailaddr@uct.ac.za Sat Jan 09:10:19 2021'
    first = data.split() # This will make the entry a list
    email = first[1] # Now that we have it split we can just index to the email postition
    print(email)
    host = email.split('@') # This will seperate the clients email from the host provider at the '@'
    print(host[1])
double_split_patteren()