#!/usr/env python
'''
Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization 
(i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the 
loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to 
disk every time it is called.

The program can be sped up greatly by moving the commit operation outside of the loop. In any database program, there is a 
balance between the number of operations you execute between commits and the importance of not losing the results of operations 
that have not yet been committed.'''


import sqlite3 
# First we import the library

# In DBs the opening in two steps:
# The connection to the DB checks access to the file
# And the cursor is like the handle that we send commands and recieve response
connect2DB = sqlite3.connect('emaildatabase.sqlite') # If no file exists one will be created
cursor = connect2DB.cursor()

# First we will use a command that will drop data that may already exist
# This is very helpful when running the command multiple times to not fill the DB
cursor.execute('DROP TABLE IF EXISTS Counts') 

# Now we will send another command through the cursor to create a table Counts
# With two columns named email and count
cursor.execute('CREATE TABLE Counts (email TEXT, count INTERGER)')

# Now we will bring the file in that we will be working with
fname = input('Enter a file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'
fh = open(fname)

# Now lets work with that data
for line in fh:
    if not line.startswith('From: '): continue # Only grab From: lines
    pieces = line.split() # Return a list of the words in the string using a delimiter string
    email = pieces[1] # This gives us just the email
    cursor.execute('''
    SELECT count from Counts WHERE email =?''',(email))
    # The ? acts as a placeholder and combats SQL injection that will be replaced by the tuple with one item (email,)
    row = cursor.fetchone() # Grabs the first item and assigns it to row

    if row is None:
        cursor.execute('''
        INSERT INTO Counts (email, count) VALUES (?,1)''',(email,))
        # If 'row' doesn't exist add (email,1) as VALUES

    else:
        cursor.execute('UPDATE Counts SET counts = counts + 1 WHERE email =?',(email,))
        # If the row exists UPDATE Counts to Counts +=1 
    connect2DB.commit()
    # Commit will commit the data from ram to the DB or disk 

# Now we will write and SQL command and loop through it with our row command from earlier
sqlstr =' SELECT email, counts FROM Counts ORDER BY count DESC LIMIT 10'
for row in cursor.execute(sqlstr):
    print(str(row[0],row[1]))
    # Row 0 = email and Row 1 = count
cursor.connection()