#!/usr/env python
# Many-to-Many Relationships
'''
Many to Many
Sometimes we need to model a relationship that is many-to-many
We need to add a 'connection' table with two foreign keys
There is usually no seperate primary value

To do this we build a 'Junction Table' to combine the two tables
This will give us a table with two (ore more) foriegn keys but no primary keys

Course              Member(junction)              User
id                  user_id                       id
title               course_id                     name
                    role

Start With a Fresh Database

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


Insert Users and Courses
INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP')

Junction Table
INSERT INTO Member (user_id, course_id, role) VALUES (1,1,1);
INSERT INTO Member (user_id, course_id, role) VALUES (2,1,0);
INSERT INTO Member (user_id, course_id, role) VALUES (3,1,0);

INSERT INTO Member (user_id, course_id, role) VALUES (1,2,0);
INSERT INTO Member (user_id, course_id, role) VALUES (2,2,1);

INSERT INTO Member (user_id, course_id, role) VALUES (2,3,1);
INSERT INTO Member (user_id, course_id, role) VALUES (3,3,0)


Now we can combine the tables
SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name
'''