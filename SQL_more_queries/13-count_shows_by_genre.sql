-- Lists all genres in hbtn_0D_tvshows with number of shows linked
SELECT name, COUNT(show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
