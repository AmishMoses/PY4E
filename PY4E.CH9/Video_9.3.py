#!/usr/env python
'''The general pattern to count the words in a line of text is to split the line into words, then loop
through the words and use a dict to track the count of each word independently'''
def countpattern():
    counts = {}
    line = input('Enter a line of text: ')
    words = line.split() # This made the text a list named words

    print('List of words:', words) # Will return the list 

    print("Counting...")
    for word in words:
        counts[word] = counts.get(word, 0) + 1 # If word exsists in words add 1 
    print('Counts:', counts)
#countpattern()

'''Definite loops and dictionaries
Even though dicts are not stored in order, we can write a for loop that goes through
all the entries in a dict - actually it goes through all the keys in the dict and look up the values'''
def defloop():
    counts = {'Hello': 1, 'my': 1, 'name': 1, 'is': 1, 'chicka': 2, 'Slim': 1, 'Shady': 1}
    for word in counts:
        print(word, counts[word])
    # You can also print just they key or vales and store them in a list
    print(counts.keys())
    print(counts.values())
    # Or just call a list method which will only take your keys from the dict
    print(list(counts))
    # Or create a tuple using items()
    print(counts.items())
defloop()

'''Two Iteration Variables
we loop through the key-value pairs in a dict using 2 iteration vars
each iteration the first var is the key and the second var is the corresponding value'''
def iteratedict():
    counts = {'Hello': 1, 'my': 1, 'name': 1, 'is': 1, 'chicka': 2, 'Slim': 1, 'Shady': 1}
    for k, v in counts.items():
        print(k, v)
iteratedict()

def project():
    name = input('enter a file name: ')
    handle = open(name)

    count = {}
    for line in handle:
        words = line.split() # This will both strip the whitespace and place it in a list
        for word in words:
            count[word] = count.get(word, 0) + 1

    bigcount = None
    bigword = None
    for word, count in count.items():
        if bigcount is None or count > bigcount: # The next few lines is a max idiom 
            bigword = word
            bigcount = count
    print(bigword, bigcount)

project()