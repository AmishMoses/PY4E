#!/usr/env python

'''Tuples are immutable versions of lists using () instead of []'''
x = ('Glen', 'Sally', 'Joseph')
print(x[2])
y = ('1', '11', '16')
print(max(y))
for i in y:
    print(i)
# Once a tuple has been created it unlike a list can not be altered using indexing
# y[1] = 2 would traceback error
# .append() .reverse() .sort() etc won't work on Tuples


# We can also put use a tuple during variable assignment
x, y = 4, 'fred'
print(x,y)
a, b = 101, 100
print(a - b)

# The items() method in dicts returns a list of (key, value) tuples
d = {}
d['Alex'] = 1
d['Manny'] = 2
for key, value in d.items(): # Created tuples
    print(key, value)

# Tuples are Comparable 
# The comparison operators work with tuples and other sequences
# If the first item is equal, Python goes on to the next element, and so on until it finds elements that differ
print(('0', '1', '2') > ('0', '5', '6')) # compares 0-0, 1-5 then exits and returns false

# Sorting lists of tuples
''' We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
First we sort the dictionary by the key using the items() method and sorted() function'''
d = {'b' : 10, 'c' : 1, 'a' : 133}
d.items() # Created our tuple ('b', 10), ('c', 1), ('a', 133)
sort = sorted(d.items()) # Will sort based on the Key and not the Value
print(sort) # Returns [('a', 133), ('b', 10), ('c', 1)]
# We can do this even more directly using the built-in function sorted() that takes a sequence
# as a parameter and returns a sorted sequence
for k,v in sorted(d.items()):
    print(k,v)

# Sort by Values Instead of Key
# If we could construct a list of tuples of the form value, key we could sort by value
# We do this with a for loop that creates a list of tuples
d = {'b' : 10, 'c' : 1, 'a' : 133}
tmp = [] # Initiate a list
for k, v in d.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True) # Sorts from highest to lowest
print(tmp)

def mostcommon():
    fopen = open(input())
    count = {}
    for line in fopen:
        words = line.split()
        for word in words:
            count[word] = count[word, 0] + 1
    lst = []
    for key,val in count.items():
        newtuple = (val, key)
        lst.append(newtuple)
    lst = sorted(lst, reverse=True) # High to low
    for val, key in lst[:10]:
        print(key, val)
#mostcommon()