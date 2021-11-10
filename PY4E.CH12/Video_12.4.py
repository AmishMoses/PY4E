#!/usr/env python
# Retrieving Web Pages Using urllib in Python
'''Since HTTP is so common, we have a library that does all the socket work for us and makes 
web pages look like a file'''
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
'''for line in fhand:
    print(line.decode().strip()) # Strip() is just being used to get rid of whitespace'''
# This doesn't return headers it only returns the data
# urllib has a function to ask for the headers
# Now that we have the webpage open as a file we can iterate through it just like any other file
counts = {}
for line in fhand:
    words = line.decode().split() # The line must be decoded before python can work with it
    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print(counts)

'''Code it replaces 
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# mysock.connect ( ( 'Hostname', port#))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() 
# \r\n is just saying enter newline 
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()'''