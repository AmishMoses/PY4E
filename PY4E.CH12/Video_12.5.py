#!/usr/env python
# Parsing web pages
'''What is web scraping
when a program or script pretends to be a browser and retrieves web pages, looks at those web pages, 
extracts information, and then looks at more web pages
Search engines scrape web pages - we call this "spidering the web" or "web crawling"
Why Scrape?
Pull data- particularly social data - who links to who 
Get your own data back out of some system that has no 'export capability' 
Monitor a site for new information
Spider the web to make a database fpr a search engine
Scraping is leagally kinda sketchy

Tons of HTML on the web has a ton of syntax errors
Becuase of this parsing the data can be difficult, luckily python has a built in library
Beautiful Soup from crummy.com'''
import urllib.request, urllib.response, urllib.error
from bs4 import BeautifulSoup
# This initiates all library packages we need to perform the web scrape
url = input('Enter URL -')
html = urllib.request.urlopen(url).read() # Read() makes the file one string
soup = BeautifulSoup(html, 'html.parser') 

# Retrieve all of the anchor tags
tags = soup('a') # Searches for all anchor tags in the document and creates a list
for tag in tags:
    print(tag.get('href', None))

'''Summary
The TCP/IP gives us pipes/sockets between application
We designed application protocols to make use of these pipes
HyperText Transfer Protocols to make use of these pipes
HTTP is a simple yet powerful tool
python has a good support for sockets, HTTP, and HTML parsing'''