#!/usr/env/ python
dict = {}
name = "C:/Users/bigal/Desktop/mbox-short.txt" #input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

read = handle.read()
split1 = read.split('From ')

name = split1[1]
fromline = name.split('@')
for line in fromline:
    dict[line] = dict.get(line, 0) + 1
print(dict)




'''9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates 
a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the 
dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''