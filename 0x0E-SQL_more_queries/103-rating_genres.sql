-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT name, SUM(rate) AS rating
FROM tv_genres gen
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = gen.id
INNER JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY name
ORDER BY rating DESC;
