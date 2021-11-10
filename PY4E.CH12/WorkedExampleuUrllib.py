#!/usr/env python
import urllib.request, urllib.response, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
counts = {}
for line in fhand:
    words = line.decode().split() # The line must be decoded before python can work with it
    # Split puts each line in a list with each word being an element
    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print(counts)

