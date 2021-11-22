#!/usr/env python
# Inserting Relational Data
'''
INSERT INTO Artist (name) VALUES ("Led Zepplin")
INSERT INTO Artist (name) VALUES ("AC/DC")
Doing this will auto increment the id field to 1 for LZ and 2 for AC/DC

INSERT INTO Genre (name) VALUES ("Rock")
INSERT INTO Genre (name) VALUES ("Metal")
Now Rock = id 1 and Metal = id 2

Now we will work with Album which has the first Foriegn Key which points to Artist (artist_id)
INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2)
INSERT INTO Album (title, artist_id) VALUES ('IV', 1)
Remeber that the artist_id of 1 = Led Zepplin and the artist_id of 2 = AC/DC
Foriegn Keys must be implemented explictlly which is why it is easier for a program to remember

Now we will work on Track which is by far the most complex
INSERT INTO Track ( title, rating, len, count, album_id, genre_id) VALUES ('Black Dog', 5, 297, 0, 2, 1)
INSERT INTO Track ( title, rating, len, count, album_id, genre_id) VALUES ('Stairway', 5, 482, 0, 2, 1)
INSERT INTO Track ( title, rating, len, count, album_id, genre_id) VALUES ('About to Rock', 5, 313, 0, 1, 2)
INSERT INTO Track ( title, rating, len, count, album_id, genre_id) VALUES ('Who Made Who', 5, 207, 0, 1, 2)
'''