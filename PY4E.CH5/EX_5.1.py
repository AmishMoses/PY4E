#!/usr/bin/env python
count = 0
total = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input. Please choose a number or done")
        continue
    print(fval)
    count = count + 1
    total = total + fval
print("All Done")
print("Ran a total of {} queries adding up to {} and a average of {}".format(count, total, total/count))