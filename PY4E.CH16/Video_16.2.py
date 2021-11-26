#!/usr/env python
# Geocoding Visualization
'''
Process summary:
We will be working with the Google Geodata through interacting with geoload.py and where.data (a flat file of places to lookup)
This data will be stored in geodata.sqlite
The Sqlite data will be parsed using geodump.py
At this point the data from geodump.py will interact with the javascript where.js
where.js links to where.html to visualize the data inside of a browser


'''
