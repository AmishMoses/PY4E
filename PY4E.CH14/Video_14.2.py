#!/usr/env python
# Our First Class and Object

class PartyAnimal: # Class is a reserved word
    x = 0 # Each PartyAnimal object has this bit of data

    def party(self): # Each PArtyAnimal object has a bit of code
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal() # Construct a PartyAnimal object and store in an variable
# When this is ran 'an' becomes equal to 'self' in the class 
# an.x = an.x + 1

an.party() # Tell the object to run the party() code within it
an.party() # Tell the object to run the party() code within it 2nd time
an.party() # Tell the object to run the party() code within it 3rd time

# PLaying with dir() and type()
'''
The diir() command list capabilities
Ignore the ones with __underscores__ these are used by Python itself
The rest are real operations the object can perform
It is like type() - it tells us something 'about' a variable
'''
print("This is what the var 'an' can do ",dir(an))
print("This is the type of var 'an' is ",type(an))