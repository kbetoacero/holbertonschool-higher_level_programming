-- list all genres from hbtn_od_tvshows and displays the number
-- of shows linked to each
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_show_genres JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id GROUP BY name ORDER BY number_of_shows DESC;
