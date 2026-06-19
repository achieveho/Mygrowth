-- 1. Find all the Toy Story movies.
SELECT *
FROM L002_Movies
WHERE Title LIKE "Toy%"
ORDER BY Year;

-- 2. Find all the movies directed by John Lasseter.
SELECT *
FROM L002_Movies
WHERE Director LIKE "John Lasseter"
ORDER BY Year;

-- 3. Find all the movies (and director) not directed by John Lasster
SELECT *
FROM L002_Movies
WHERE Director NOT LIKE "John Lasseter"
ORDER BY Year;

-- 4. Find all the WALL-* movies.
SELECT *
FROM L002_Movies
WHERE Title LIKE "WALL-%"
ORDER BY Year;