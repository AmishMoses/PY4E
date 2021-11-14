#!/usr/env python
'''In this assignment you will write a Python program that expands on https://www.py4e.com/code3/urllinks.py. 
The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags, 
scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times, 
and report the last name you find.'''
'''
We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the 
actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name
that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Lyall.html
Hint: The first character of the name of the last page that you will load is: L
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

Sample execution

Here is a sample execution of a solution:
$ python3 solution.py
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
position = int(input('What position would you like to select? :'))
iterations = int(input('How man times should we run this?: '))
for i in range(iterations):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    count = 0 # Will reset everytime we re run through this portion of the code
    for tag in tags:
        count += 1
        if count > position: break
        url = tag.get('href', None)
        name = tag.contents[0]

    print(name)
    
    #tag = tag.get('href', None)
    #print(list(tag))
'''Doesn't work splits the lines into letters strip() isn't working either    
    
    for line in tag:
        line = line.split()
        print(line)
'''
'''
People that Fikret knows
Aniqa
Ogheneruno
Montgomery
Owain
Haniyah
Anona
Edyn
Dallace
Zoe
Kiarash
Tracy
Carmyle
Zahraa
Alanys
Airidas
Melisa
Vivian
Margaret
Hajra
Ajooni
Alexanne
Sudais
Seb
Christin
Jaimie
Jennah
Landon
Mea
Cacie
Colton
Mitchel
Chintu
Hyden
Chrystal
Lincon
Jaden
Roma
Manolo
Clio
Teos
Rihonn
Griffin
Conley
Xiao
Dhyia
Manahil
Diona
Dharam
Danielle
Rori
Lang
Sabila
Zoha
Jemma
Silvana
Asal
Dillon
CJ
Joanna
Atal
Callun
Anubhav
Coray
Graeme
Chrissie
Ayub
Heather
Katie
Inaara
Siddhant
Salymat
Shahd
Anaya
Kevaugh
Thumbiko
Xida
Alaska
Shonagh
Kaiya
Khadija
Kieron
Filip
Dorothy
Kallan
Mena
Abbie
Amyleigh
Annalise
Carrich
Rachel
Etinosa
Amie
Lisa
Liv
Baylie
Jubin
Kacie
Falyn
Conli
Cohen'''