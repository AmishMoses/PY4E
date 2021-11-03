#!/usr/env/ python
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di = {}
for line in handle:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        hrminsec = time.split(':')
        hour = hrminsec[0] # Now we have just the hour marks
        di[hour] = di.get(hour, 0) + 1
for k,v in sorted(di.items()):
    print(k,v)

'''10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for 
each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string 
a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

'''Reworked exercise

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
times = {}
handle = open(name)
for line in handle:
    line = line.strip() # Gives us clean lines of data to work with
    if line.startswith('From '): # Gives us our list of senders
        line = line.split() # Puts our data into a list format
        hrminsec = line[5] # Gives us our time at index 5
        hrminsecsplt = hrminsec.split(':') # Splits the data into a further list using ':' as the delim
        hour = hrminsecsplt[0] # Grabs the hour section only
        times[hour] = times.get(hour, 0) + 1 # Idiom to count the entries in the dict
for key, value in sorted(times.items()):
    print(key,value)'''