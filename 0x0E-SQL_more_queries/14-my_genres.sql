-- because Batch 3 is the best!
SELECT tv_genres.name FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id INNER JOIN tv_shows on tv_shows.id=tv_show_genres.show_id WHERE title="Dexter" ORDER BY tv_genres.name ASC;
