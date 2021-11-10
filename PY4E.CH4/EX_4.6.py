#!/usr/env python
def computepay(hours, rate):
    print(f"Computing pay at {hours} hours and {rate} per hour")
    if hours < 40:
        pay = hours * rate
        print(pay)
    elif hours > 40:
        pay = (hours - 40) * (rate * 1.5) + (40 * rate)
    return pay
userhours = input("How many hours did you work?:")
userrate = input("At what rate?:")
uh = float(userhours)
ur = float(userrate)
total = computepay(uh, ur)
print("Pay",total)
