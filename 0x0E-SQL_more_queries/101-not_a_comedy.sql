-- No Comedy tonight! 
-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT DISTINCT s.title FROM tv_shows AS s LEFT JOIN tv_show_genres AS sg
