#!/usr/env python
import sqlite3
import json


conn = sqlite3.connect('ManySManyC.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT
    email TEXT
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT
); 

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id, course_id)
) 
''')
fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'C:/Users/bigal/Desktop/PY4E/Databases/roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)
# [['Charley', 'si110', 1], ['Mea', 'si110', 0]]

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # print((name, title)) 
    # ('Charley', 'si110') ('Mea', 'si110')

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(name,))
    cur.execute('SELECT id FROM User WHERE name =?', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)',(user_id, course_id, role))
    
    
    conn.commit()
'''
Instructions
This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a 
User, Course, and Member table and populate the tables from the data file.

You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py - 
this code is incomplete as you need to modify the program to store the role column in the Member table to complete the assignment.

Each student gets their own file for the assignment. Download this file and save it as roster_data.json. 
Move the downloaded file into the same folder as your roster.py program.

Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data, 
run the following SQL command:

SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

The output should look as follows:
Zi|si206|0
Zarran|si422|0

Once that query gives the correct data, run this query:
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
You should get one row with a string that looks like XYZZY53656C696E613333.
ANSWER = XYZZY414A736933363330
'''