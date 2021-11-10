#!/usr/env python

'''We can create a new list by adding two list together this is know as concatenating'''
def cat():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a + b # This only appends the list together it doesn't add intergers
    print (c)
    d = b + a
    print(d) # It also matters which variable you place first
cat()

print('\n')
'''Lists can also be sliced just remember the second number is 'up to but not including' '''
def sliced():
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , 15, 16, 17, 18, 19, 20]
    print(t[0:19]) # The 19th element is 20 but it will not be included
    print(t[:-1]) # This will select the last element if you don't know how long the list is
    count = t[:3] # Accepts 0 as an argument unless one is stated for :
    print(count)
    mixed = t[2:5] + t[8:15]
    print(mixed)
sliced()

print('\n')
'''Lists can be built from scratch. Create an empty list and then add elements using the .append() method
append will keep the order of which items are added'''
def listfromscratch():
    stuff = list() # same as stuff = []
    stuff.append('book')
    stuff.append('cow')
    stuff.append('spider')
    print(stuff)
    # You can also check a list by using the keyword 'in' this does not modify the list
    print('spider' in stuff)
    print('Milk' in stuff)
    '''A list holds the order in which items were created, but with sort() a list will change its' own order'''
    print(stuff)
    stuff.sort() # This changes the value of stuff
    print(stuff)
listfromscratch()

print('\n')
"""Python has many built in functions to take the place of the loops we wrote in chapter 5"""
def builtin():
    nums = [8, 77, 5451, 566, 984, 4, 12, 518, 61]
    print(len(nums)) # Finds element total
    print(max(nums)) # Finds largest
    print(min(nums)) # Finds smallest
    print(sum(nums)) # Gets the total 
    print(sum(nums) / len(nums)) # Gets the average
builtin()


def example():
    numlist = []
    while True:
        usrin = input("Enter a number: ")
        if usrin == 'done' : break
        cleandata = float(usrin) # This will take the input from our user and put it as a float number
        numlist.append(cleandata) # This will add our cleandata var to our list 
    average = sum(numlist) / len(numlist)
    print(average)

example()
