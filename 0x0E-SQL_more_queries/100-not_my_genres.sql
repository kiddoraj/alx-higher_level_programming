-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Get the genre_id linked to the show "Dexter"
SET @dexter_genre_id = (SELECT tv_show_genres.genre_id FROM tv_show_genres WHERE tv_show_genres.show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter'));

-- List genres not linked to the show "Dexter"
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id AND tv_show_genres.genre_id = @dexter_genre_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_genres.name ASC;
