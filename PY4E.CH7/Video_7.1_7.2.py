#!/usr/env/ python

'''Using open() handle = open('filename', 'mode')'''
# Modes = open, read, write, close (o,r,w,c)

def new_line():
    print('\n')
# new line is only represtented as one character inside of python it is basically an enter button

def file_manipulation():

    read_file = open("C:/Users/bigal/Desktop/PY4E/PY4E.CH7/mbox.txt") # It would open in r by default
    
   
   
    def read_lines():
        count = 0 # we can count the lines of the file
        for line in read_file:
            count += 1
            print(line, count)
    #read_lines()

   
   
    def search_file():
        for line in read_file:
            line = line.strip() # This gets rid of the below talked about extra \n
            if line.startswith('From:'): # Will show a list of received email domains
                print(line) # This will have a blank line due to the print statement adding a \n .strip() fixes this
                # Print adds a \n and the file itself has a \n strip() or rstrip() woould fix that
    #search_file()

    
    
    def continue_skip(): # The same process as above with reversed logic
        counter = 0
        for line in read_file:
            line = line.strip() # This gets rid of the below talked about extra \n
            if not line.startswith('From:'): # If the line doesn't match the criteria it is skipped
                continue
            else:
                counter += 1 # Will count the lines it accepts 
            print(line, counter)
    #continue_skip()

    
    
    def user_input():
        usr = input("What file would you like to open? : ")
        try:
           usrfile = open(usr)

        except:
            print(f"I'm sorry {usr} is not a valid filename")
            quit()

        count = 0
        for line in usrfile:
            if line.startswith('Subject:'):
                count += 1
        print(f"There were {count} lines inside of {usr} that start with 'Subject:'")

    user_input()

file_manipulation()