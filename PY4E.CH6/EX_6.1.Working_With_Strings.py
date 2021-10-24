#!/usr/env/ python

'''Using indexing to get a specific value in an input string'''
def index_string():
    fruit = 'banana'
    letter_index = fruit[0] #this will be 'b' due to the index starting at 0
    print(letter_index)
    
    x = 3 
    w = fruit[x + 1] #Takes index of 4
    print(w)
index_string()

print("\n")

def finding_length():
    string = "howlongisthisword"
    print(f"{string} is {len(string)} letters long")
finding_length()

print('\n')

def looping_through_strings():
    fruit = "Strawberry"
    index = 0
    while index < len(fruit):
        letter = fruit[index] # will iterate through the string
        print(f"{letter} is the {index} letter of the word {fruit}")
        index += 1 #Works the same as ' index = index + 1 '
    print(len(fruit)) # len starts counting at 1 while index starts at 0
# Another way to loop easier
    count = 1
    for letter in fruit:
        print(letter, count)
        count += 1
looping_through_strings()

print('\n')

def looping_and_counting():
    word = "pneumonoultramicroscopicsilicovolcanoconiosis"
    count = 0
    for i in word:
        if i == "i":
            count += 1
    print("{} has {} i's".format(word, count))
looping_and_counting()

print('\n')

def slicing_strings():
    '''When splicing the sytax is (start:end but not including) which means if you say :2 you will end at 
    2 and wont return the character indexed at that position'''
    name = 'Monty Python'
    print(name[0:5]) #This will print the first 6 letters using the index 0-5
    print(name[0:100000]) # if the range is beyond the string it will stop at the end
    print("The len is: ", len(name)) # Remember the len is one more than the index
    print(name[6:12]) # The space counts as a indexable character and to get the full string we need to use 12 not 11
    print(name[:5]) # Will start at begginning 
    print(name[6:]) # Will end at EOL
slicing_strings()