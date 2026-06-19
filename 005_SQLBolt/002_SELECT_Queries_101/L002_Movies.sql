-- 002_SELECT_Quries_101/00_create_L002_Movies.sql
-- SQLBolt Lesson 1 / SELECT Quries 101
-- Original table name: Movies
-- Local practice table name: L002_Movies

DROP TABLE IF EXISTS L002_Movies;

CREATE TABLE L002_Movies (
    Id INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    Director TEXT NOT NULL,
    Year INTEGER NOT NULL CHECK (Year >= 1900),
    Length_minutes INTEGER NOT NULL CHECK (Length_minutes > 0)
);

INSERT INTO L002_Movies
    (Id, Title, Director, Year, Length_minutes)
VALUES
    (1,  'Toy Story',            'John Lasseter',  1995,  81),
    (2,  'A Bug''s life',        'John Lasseter',  1998,  95),
    (3,  'Toy Story 2',          'John Lasseter',  1999,  93),
    (4,  'Monsters, Inc.',       'Pete Docter',    2001,  92),
    (5,  'Finding Nemo',         'Andrew Stanton', 2003, 107),
    (6,  'The Incredibles',      'Brad Bird',      2004, 116),
    (7,  'Cars',                 'John Lasseter',  2006, 117),
    (8,  'Ratatouille',          'Brad Bird',      2007, 115),
    (9,  'WALL-E',               'Andrew Stanton', 2008, 104),
    (10, 'Up',                   'Pete Docter',    2009, 101),
    (11, 'Toy Story 3',          'Lee Unkrich',    2010, 103),
    (12, 'Cars 2',               'John Lasseter',  2011, 120),
    (13, 'Brave',                'Brenda Chapman', 2012, 102),
    (14, 'Monsters University',  'Dan Scanlon',    2013, 110);