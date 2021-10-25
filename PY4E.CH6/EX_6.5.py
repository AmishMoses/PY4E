#!?usr/env/ python

def my_solution():
    text = "X-DSPAM-Confidence:    0.8475"
    okay = text.find('0')
    fokay = float(text[okay:])
    print(fokay)
my_solution()

'''6.5 Write code using find() and string slicing (see section 6.10) to 
extract the number at the end of the line below. Convert the extracted 
value to a floating point number and print it out.'''
print('\nCharles\' solution from the book')
def charles_solution():
    text = "X-DSPAM-Confidence:    0.8475"
    ipos = text.find(':')
    print(ipos)
    piece = text[ipos + 2 :]
    value = float(piece)
    print(value)
charles_solution()