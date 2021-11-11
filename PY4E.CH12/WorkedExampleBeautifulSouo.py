#!/usr/env python
# Worked ecample BeautifulSoup chapter 12
import urllib.request, urllib.response, urllib.error
from bs4 import BeautifulSoup
import ssl 

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
html = urllib.request.urlopen(url, context=ctx).read() # Read() makes the file one string
soup = BeautifulSoup(html, 'html.parser') 

# Retrieve all of the anchor tags
tags = soup('a') # Searches for all anchor tags in the document and creates a list
for tag in tags:
    print(tag.get('href', None))
