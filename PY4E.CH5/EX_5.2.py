#!/usr/bin/env python
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fval = int(num)
    except:
        print("Invalid input")
    if largest is None:
        largest = fval
    if smallest is None:
        smallest = fval
    if fval > largest:
        largest = fval
    if fval < smallest:
        smallest = fval

    #print(num)

print("Maximum is", largest)
print("Minimum is", smallest)

'''5.2 Write a program that repeatedly prompts a user for integer numbers until
the user enters 'done'. Once 'done' is entered, print out the largest and
smallest of the numbers. If the user enters anything other than a valid number
catch it with a try/except and put out an appropriate message and ignore the
number. Enter 7, 2, bob, 10, and 4 and match the output below.'''
