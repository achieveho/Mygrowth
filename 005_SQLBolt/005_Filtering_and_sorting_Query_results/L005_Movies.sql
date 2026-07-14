-- 005_Filtering_and_sorting_Query_results
-- SQLBOLT Lesson 05 / Filtering and sorting Query results
-- Original table name: Movies
-- Local practice table name: L005_Movies

DROP TABLE IF EXISTS L005_Movies;

CREATE TABLE L005_Movies (
    Id INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    Director TEXT NOT NULL,
    Year INTEGER NOT NULL CHECK (Year >= 1900),
    Length_minutes INTEGER NOT NULL CHECK (Length_minutes > 0)
);

INSERT INTO L005_Movies
    (Id, Title ,Director, Year, Length_minutes)
VALUES
    (1, 'Ratatouille', 'Brad Bird', 2007, 115),
    (2, 'Finding Nemo', 'Andrew Stanton', 2003, 107),
    (3, 'The Incredibles', 'Brad Bird', 2004, 116),
    (4, 'Brave', 'Brenda Chapman', 2012, 102),
    (5, 'Cars 2', 'John Lasseter', 2011, 120),
    (6, 'A Bug''s life', 'John Lasseter', 1998, 95),
    (7, 'Toy Story 2', 'John Lasseter', 1999, 93),
    (8, 'Monsters University', 'Dan Scanlon', 2013, 110),
    (9, 'Toy Story 3', 'Lee Unkrich', 2010, 103),
    (10, 'Toy Story', 'John Lasseter', 1995, 81),
    (11, 'Up', 'Pete Docter', 2009, 101),
    (12, 'Cars', 'John Lasseter', 2006, 117),
    (13, 'WALL_E', 'Andrew Stanton', 2008, 104),
    (14, 'Monsters, Inc.', 'Pete Doctor', 2001, 92)