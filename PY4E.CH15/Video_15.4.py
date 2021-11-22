#!/usr/env python
# Designing a Data Model
'''
Database Design
Is an artform of its own with particular skills and exp
Our goal is to avoid the really bad mistakes and design clean and easily understood databases
Others may tune performance later
The design starts off as a picture

Building a Data Model
Drawing a picture of the data obkects for our application and then figuring out how to represent
the objects and their relationships.
Basic Rule: Don't put the same string data in twice - use a relationship instead
When there is one thing in the 'Real World' there should be one copy of that thing in the DB

For each 'piece of info' 
Is the column an object or an attribute of another object
Once we define objects, we need to define the relationships between objects
Big question 'Where do you start'
Think of the most essential purpose or a one sentenance summary
We are building a 'DB to manage tracks'

DATA: Track/Title Album Artist Genre Rating Len Count
What is an attribute of track? (title, len, rating, count) non-replicated data

Albums have many Tracks and also belong to Artist
'''