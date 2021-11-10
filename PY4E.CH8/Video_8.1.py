#!/usr/env python

'''A list is a collection which means in a single variable we can assign more than one value
list constants are surrounded by [] and the elements seperated by commas. A list can contain any python object
including other list'''
def collection():
    list1 = ['one', '[2,3]', '4.2']
    print(list1)
    # We can also index lists 
    print(list1[0])
    # We can also change list which is known as 'mutable' we do this using indexing
    list1[0] = 1 # This will reassign 'one' with the interger 1
    print(list1[0])
    # len() can be used to find the # of elements in a list aswell
    print(len(list1)) # Each element is one is isn't counting the characters
#collection()

print('\n')

'''The range() function returns a list of numbers that range from 0 to one less than the parameter
we can construct an index loop using for and an integer iterator'''
def range_function():
    print(range(4)) # will print (0, 4)
    list1 = ['one', '[2,3]', '4.2']
    print(range(len(list1))) # Will return (0, 3)

    friends = ['Manny', 'Andrew', 'Talyn']
    for i in range(len(friends)): # This will run the range function and substitude the proper number to run the command
        friend = friends[i]
        print("Happy Halloween:", friend)
    
range_function()
print('\n')