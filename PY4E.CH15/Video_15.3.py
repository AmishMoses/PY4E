#!/usr/env python
# Single Table CRUD (Create, Retrieve, Update, Delete)
'''
We opened SQLite 
Created a new DB named sql1 and exited out of the next screen

# Creating a table in SQLite
(Execute SQL TAB)
CREATE TABLE Users(
    name VARCHAR(128),
    email VARCHAR(128)
)
Created one table with two columns of variables up to 128 chars
This is our schema or DB model

After entering this hit execute 
output:
Execution finished without errors.
Result: query executed successfully. Took 7ms
At line 1:
CREATE TABLE Users(
    name VARCHAR(128),
    email VARCHAR(128)
)

# SQL Insert
The insert statement isnerts a row into a table
INSERT INTO Users (name,email) VALUES ('Casey', 'fakeCaseyemail@femail.com')

# SQL Delete
Deletes a row in a table based on a selection criteria 
DELETE FROM Users WHERE email='fakeSallyemail@femail.com'

# SQL Update 
UPDATE <table name> SET <columnName>=<NewValue>
Allows the updating of a field with a WHERE clause
UPDATE Users SET name='Charles' WHERE email='fakeCaseyemail@femail.com' 
UPDATE Users SET email='fakeCharlesemail@femail.com' WHERE name='Charles'

# Retrieving Records: Select
The SELECT statement retrieves a group of records
You can either retrieve all the recordds or a subset of the records with a WHERE clause
SELECT * FROM Users
SELECT * FROM Users WHERE email='fakeCharlesemail@femail.com'
* is a wildcard meaning ALL

# Sorting with ORDER BY
You can also ORDER BY clause to SELECT statments to get the results sorted in ascending or descending order
SELECT * FROM Users ORDER BY email ASC
SELECT * FROM Users ORDER BY name DESC

'''