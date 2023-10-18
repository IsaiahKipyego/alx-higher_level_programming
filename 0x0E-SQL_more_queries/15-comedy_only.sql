-- lists all comedy shows in db
-- list the shows
SELECT C.title
FROM tv_genres A
JOIN tv_show_genres B
ON A.id = B.genre_id
JOIN tv_shows C
ON C.id = B.show_id
WHERE A.name = 'Comedy'
ORDER BY C.title ASC;
