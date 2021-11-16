#!/usr/env python
# Object life cycle
'''
Objects are created, used and discarded
We have special blocks of code (Methods) that get called 
    At the moment of creation (constructor)
    At the moment of destruction (destructor)
Constructors are used a lot
Destructors are seldom used
The primary purpose of the constructor is to set up some instance variables to have proper inital values
'''

# The constructor and destructor are specially named variables and optional 
class PartyAnimal: # Class is a reserved word
    x = 0 # Each PartyAnimal object has this bit of data

    def __init__(self):
        print("I am constructed")

    def party(self): # Each PArtyAnimal object has a bit of code
        self.x = self.x + 1
        print("So far",self.x)

    def __del__(self):
        print("I am destructed",self.x)

an = PartyAnimal() # Construct a PartyAnimal object and store in an variable
# When this is ran 'an' becomes equal to 'self' in the class 
# an.x = an.x + 1
an.party()
an.party()
an.party()
an = 42
print('an contains', an)

# Many Instances 
'''
We can create lots of objects- the class is the template for the object
We can store each distinct object in its own variable
We call this having multiple instances of the same class
Each instance has its own copy of the instance vaiables
Comstructors can have additional parameters. These can be used to set up instance variables for the
particular instance of the class ie: for the particular object
'''

class PartyAnimal: # Class is a reserved word
    x = 0 # Each PartyAnimal object has this bit of data

    def __init__(self, z):
        self.name = z

    def party(self): # Each PArtyAnimal object has a bit of code
        self.x = self.x + 1
        print(self.name,"party count of",self.x)
s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()