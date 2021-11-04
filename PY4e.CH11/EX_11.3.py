#!/usr/bin/bash
name = input("Enter file:")
if len(name) < 1:
    name = "C:/Users/bigal/Desktop/PY4E/PY4e.CH11/data.txt"
handle = open(name)
handle1 = handle.read()
for line in handle1:
    line = line.strip()

    print(line)


'''Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the 
sum of the numbers.
Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and 
summing up the integers.'''