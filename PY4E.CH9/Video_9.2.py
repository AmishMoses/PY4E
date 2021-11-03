#!/usr/env/ python
# Dictionary tracebacks 
# It is an error ti reference a key which is not in the dictionary
# We can use the in operator to see if a key is in the dictionary
def inop():
    ccc = {}
    #print(ccc['Alex']) # Will return key error
    print('Alex' in ccc) # Will return a boolean in this instance False
inop()


# Building a histogram using a dictionary
'''When we encounter a new name, we need to add a new entry in the dict and if this is the second or later time 
we have seen the name, we simply add one to the count in the dict under that name '''
def histdict():
    names = ['Manny', 'Alex', 'Andrew', 'Mike', 'Talyn', 'Steve', 'Alex']
    countdict = {} # or dict()
    for name in names:
        if name not in countdict:
            countdict[name] = 1 # This assigns the name to the dict and gives it a value of 1
        else:
            countdict[name] += 1 # This means if it is already in the dict add 1 to the value
    print(countdict)
histdict()

'''There's a better way to do this. The pattern of checking to see if a key is already in a dict
and assuming a default value if the key is not there is so common that there is a method called
get() that does this for us'''
def getmethod():
    count = {}
    names = ['Manny', 'Alex', 'Andrew', 'Mike', 'Talyn', 'Steve', 'Alex']
    for name in names:
        count[name] = count.get(name, 0) + 1 # This assigns a key in this case name a default value and if the key is present adds 1
    print(count)
getmethod()