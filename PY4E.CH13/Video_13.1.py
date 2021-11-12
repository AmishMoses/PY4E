#!/usr/env python
# Data on the Web
'''
With HTTP Request/Response well undersstood and well supported, there was a natural move
toward exchanging data between programs using these protocols
We needed to come up with an agreed way to represent data going between applications and accross networks
There are two commonly used formats: XML and JSON
When sending data from python to another source we use 'serialization' (one char at a time) to send the data on an 
agreed upon 'wire format' before is is 'de-searlized' at the endpoint
'''
# XML- Marking up data to send accross the network 