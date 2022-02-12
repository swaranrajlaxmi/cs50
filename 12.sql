SELECT title FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON people.id = stars.person_id
WHERE people.name = "Johnny Depp" AND title IN
    (SELECT title FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON people.id = stars.person_id
    WHERE people.name = "Helena Bonham Carter");


--SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = "Johnny Depp" OR name = "Helena Bonham Carter")