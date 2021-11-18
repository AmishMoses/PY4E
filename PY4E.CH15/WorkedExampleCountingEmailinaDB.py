#!/usr/env python
import sqlite3
# In DBs the opening in two steps:
# The connection to the DB checks access to the file
# And the cursor is like the handle that we send commands and recieve response
connection = sqlite3.connect('emaildb.sqlite') # This will create the DB if it doesn't exsist
cur = connection.cursor()

cur.execute('DROP TABLE IF EXISTS Counts') # If it exists drop and recreate

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTERGER)''') # Creates table named Counts with two colums named email and count
fname = input('Enter a file name: ') # This is the file python will be working with to send data to the DB
if len(fname) < 1: fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue # This is how we will find the email 
    pieces = line.split() # Split will give us ['From:', 'Yadayada@email.com']
    email = pieces[1] # This gives us just the email
    cur.execute('SELECT count FROM Counts WHERE email =?',(email,)) 
    # The ? acts as a placeholder and combats SQL injection that will be replaced by the tuple with one item (email,)
    row = cur.fetchone() # Grab the first item and give it to 'row'
    if row is None:
        cur.execute('''
        INSERT INTO Counts (email, count) VALUES (?, 1)''',(email,))
        # If 'row' doesn't exist add (email,1)

    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email =?',(email,))
        # If the row exists UPDATE Counts to Counts +=1 
    connection.commit()
    # Commit will commit the data from ram to the DB or disk 

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
# This is an SQL command we will execute underneath only this time we will call the variable
for row in cur.execute(sqlstr):
    print(str(row[0],row[1]))
    # Row 0 = email and Row 1 = count
cur.connection()