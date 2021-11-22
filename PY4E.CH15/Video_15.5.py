#!/usr/env python
# Representing a Data Model in Tables
'''
A relational database is made up of multiple parts
Tables
Primary Keys
Logical Keys
Foreign Keys

For example the track table may have a column named album_id 
album_id would be a foreign key pointing to a primary key in the table Album

The primary key is a way to refer to a particular row
The logical key is an unique way to look up the row from the outside (WHERE clause, ORDER BY clause)

Using the DB creation wizard
Not= Not NULL     PK = Primary Key     AI = Auto Increment     U = Unique 
Now we will create the Artist table
id INTERGER 
name TEXT
CREATE TABLE "Artist" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

When creating the DB you work from the outside in so now we will create our genre
CREATE TABLE "Genre" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)

Now we will create our table using a foriegn key
CREATE TABLE "Album" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "artist_id" INTEGER,
	"title" TEXT
)

And finally our Track list
CREATE TABLE "Track" (
	"id"	INTEGER NOT NULL UNIQUE,
    "title" TEXT, 
    "album_id" INTEGER,
    "genre_id" INTEGER,
    "len" INTEGER, "rating" INTEGER, "count" INTERGER
)
'''
