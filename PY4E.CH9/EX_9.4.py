#!/usr/env/ python
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
addr = {}
for line in handle:
    line = line.strip()
    if line.startswith('From '):
        data = line.split()
        sender = data[1]
        #print(sender)
        addr[sender] = addr.get(sender, 0) + 1
#print(addr)
maxsender = None
emailcount = None
for k,v in addr.items():
    if emailcount == None or emailcount < v:
        emailcount = v
        maxsender = k
print(maxsender, emailcount)




'''9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates 
a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the 
dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''


'''Reworked code
name = input("Enter file:")
senders = {} # Opens an empty dict 
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.strip()
    if line.startswith('From '):
        #print(line) # Now we have a list of senders
        split = line.split()
        #print(split) # Now the lines are indexed in a list
        sender = split[1]
        #print(sender)
        senders[sender] = senders.get(sender, 0) + 1 # Idiom that says if it exists add one to it 
#print(senders)

maxsend = None
sendcount = None

for key, value in senders.items():
    if sendcount is None or sendcount < value:
        maxsend = key
        sendcount = value
print(maxsend, sendcount)
        '''