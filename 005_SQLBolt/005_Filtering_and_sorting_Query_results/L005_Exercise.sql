-- 001. List all directors of Pixar movies(alphabetically), without duplicates
SELECT DISTINCT Director
FROM L005_Movies
ORDER BY Director;

--002. List the last four Pixar movies released (ordered from most recent to least)
SELECT *
FROM L005_Movies
ORDER BY Year DESC
LIMIT 4;

--003. List the first five Pixar movies sorted alphabetically.
SELECT *
FROM L005_Movies
ORDER BY Title
LIMIT 5;

--004. List the next five Pixar movies sorted alphabetically
SELECT *
FROM L005_Movies
ORDER BY Title
LIMIT 5 OFFSET 5;