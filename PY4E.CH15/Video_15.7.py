#!/usr/env python
# Reconstructing data with JOIN
'''
Relational Power
By removing the replicated data and replacing it with references to a single copy of each bit of data
we build a 'web' of information that the relational database can read through very quickly- even for large amounts of data
Often when you want some data it comes from a number of tables linked by these foreign keys

The JOIN Operation 
The JOIN operation links accross several tables as part of a SELECT operation
You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause

SELECT Album.title, Artist.name from Album join Artist on Album.artist_id = Artist_id
SELECT Album.title, Artist.name     - What we want to see (Tablename.Fieldname)
from Album join Artist             - The tables that hold the data
on Album.artist_id = Artist_id      - How the tables are linked

SELECT Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id
SELECT Track.title, Genre.name      - What we want to see
from Track join Genre               - The tables that hold the data
on Track.genre_id = Genre.id        - How the tables are linked

If you don't include the ON clause you will get every combonation of the data IE: Repeated data

It Can Get Complex
SELECT Track.title, Artist.name, Album.title, Genre.name from Track JOIN Genre JOIN Album JOIN Artist 
ON Track.Genre_id and Track.album_id = Album.id and Album.artist_id = Artist.id
'''