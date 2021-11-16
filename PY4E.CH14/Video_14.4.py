#!/usr/env python
# Object Inheritance
'''
When we make a new class- we can reuse an existing class and inherit all the capabilities
of an existing class and then add our own little bit to make our new class
Another form of store and release
Written once - used many
The new class (child) has all the capabilities of the old class (parent) and more
These child classes can also be called sub-classes
'''
class PartyAnimal: # Class is a reserved word
    x = 0 # Each PartyAnimal object has this bit of data
    name = ""

    def __init__(self, nam):
        self.name = nam
        print(self.name)

    def party(self): # Each PartyAnimal object has a bit of code
        self.x = self.x + 1
        print(self.name,"party count of",self.x)

class FootballFan(PartyAnimal): # FootballFan is a class which extends PartyAnimal 
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points",self.points)
s = PartyAnimal('Sally')
s.party()
j = FootballFan("Jim")
j.touchdown()
