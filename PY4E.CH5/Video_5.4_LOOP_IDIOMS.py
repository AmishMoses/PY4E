#!/usr/env python

# Counting in a loop
# Counts the total amounts of iteations through the list
count = 0
print ("Count before loop runs", count)
for element in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    print(count, element)
print("Total number of iterations", count)

# Summing a loop together
'''Takes the first element of a list and adds the next value in the iteration. Always holding the 
sum in memory as a variable to add to every element in the list'''
sum = 0
print ("Before running through list", sum)
for element in [9, 41, 12, 3, 74, 15]:
    sum = sum + element
    print (f"Adding {sum} to {element}")
print("The array adds up to:", sum)

# Taking an average of the sum 
sum = 0
count = 0 # this will take the number of iterations and divide it by the sum 
print ("Before running through list", count, sum)
for element in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + element
    print(element, sum, count)
print(f"A total of {count} items divided by the sum {sum}")
print("The average is:", sum/count)

# Filtering in a loop
print("Before filtering")
for element in [9, 41, 12, 3, 74, 15]:
    if element > 20:
        print ("Value over 20:", element)
    else:
        print("Value under 20:", element)
print("Done filtering")

# Search using a Boolean variable (T/F)
found = False
count = 0
print("Have we found the element?", found)
for element in [9, 41, 12, 3, 74, 15]:
    if element == 3:
        found = True
        print(found)
        print("We have found the value!")
        # break here would exit at the first success
    else:
        count = count + 1
print("We checked {} items".format(count))

# Finding the smallest value
max = 0
print("The largest value so far is:", max)
for element in [9, 41, 12, 3, 74, 15]:
    print(f"Running through loop {max} {element}")
    if element > max:
        print(f"Switching the previous largest {max} with {element}")
        max = element
print(f"Largest number:", max)

# Finding the smallest value
min = None
print("The largest value so far is:", min)
for element in [9, 41, 12, 3, 74, 15]:
    print(f"Running through loop {min} {element}")
    if min == None:
        min = element
        # Without this bit of code you will get an error comparing None to an interger
    elif element < min:
        print(f"Switching the previous smallest {min} with {element}")
        min = element
print(f"Smallest number:", min)