#!/usr/env python

# This video is a repeat of Video_12.3.py


# Unicode characters and Strings
# ord() function tells us the numeric value of a simple ASCII character
# Each ascii character is 8 bits or one byte
print(ord('H')) # 72
print(ord('h')) # 104



# ASCII only represents 127 characters which was to small and the reason Unicode was established
# Multi-Byte Characters
'''To represent the wide range of characters computers must hand;e we represent characters with more than
one byte
UFT-16 fixed length 2 bytes
UTF-32 fixed length 4 bytes
UTF-8 1-4 bytes
UTF-8 is reccommended practice for encoding data to be exchanged between systems'''



# In Pyth0n 3 all strings are Unicode 
# In Python 3 if you want to make a 'byte string' you need to declare that with b'string'
x = b'abc'
print(type(x)) # Class bytes



'''When we talk to an external resource like a network socket we send bytes, 
so we need to encode python 3 strings into a given character encoding
When we read data from an external resource, we must decode it based on the character set
so it is properly represented in Pyrhon 3 as a string
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    mystring = data.decode()
    print(mystring)'''
# .decode() by default asumes UTF-8 and ASCII 
# .encode() takes a string and turns it into bytes
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
