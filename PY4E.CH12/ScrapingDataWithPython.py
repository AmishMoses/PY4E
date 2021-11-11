#!/usr/env python
# Scraping HTML Data with BeautifulSoup
'''
Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to 
http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, 
extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the 
actual data you need to process for the assignment.
You do not need to save these files to your folder since your program will read the data directly from the URL. 
Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1383145.html (Sum ends with 26)
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

Data Format
The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and 
extract the various aspects of the tags.

...
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs
You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.
Sample Execution

$ python3 solution.py
Enter - http://py4e-data.dr-chuck.net/comments_42.html
Count 50
Sum 2...
'''
import urllib.request, urllib.response, urllib.error
from bs4 import BeautifulSoup
import ssl 
import re
# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
data = []
sum = 0
url = 'http://py4e-data.dr-chuck.net/comments_1383145.html'
html = urllib.request.urlopen(url, context=ctx).read() # Read() makes the file one string
soup = BeautifulSoup(html, 'html.parser') 

#print(soup) # Gives me a body of data to work with
# Retrieve all of the Span tags
# Using RegEX
'''tags = soup('span') # Searches for all Span tags in the document and creates a list
print(tags)    
for tag in tags:
    tag = str(tag) # Convert tag to a string so we can use re.findall('<pattern>', string)
    nums = re.findall('[0-9]+', tag)
    print(nums)
    for x in nums:
        # x = int(x) # Wasted line
        sum = sum + int(x)
print(sum)'''
# Attempting to use decode()
tags = soup('span') # Searches for all Span tags in the document and creates a list
print(tags)    
for tag in tags:
    tag = tag.decode()
    nums = re.findall('[0-9]+', tag)
    print(nums)
    for num in nums:
        sum = sum + int(num)
        print(sum)

'''
Doesn't work becuase I wasn't making line a string before iterating over it
for line in soup:
    line = line.split()
    data = re.findall('[0-9]+', line)
    print(data)'''