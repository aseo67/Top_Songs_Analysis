-- CREATE TABLES FOR LOADING DATA
CREATE TABLE top_songs (
	"Index" INT, 
	song_id VARCHAR,
	song_name VARCHAR, 
	artist VARCHAR, 
	number_of_times_charted INT,
	highest_charting_position INT, 
	week_of_highest_charting_start DATE,
	week_of_highest_charting_end DATE,
	number_weeks_charted INT,
	streams INT, 
	artist_followers INT, 
	genre VARCHAR,
	release_date DATE,
	popularity NUMERIC, 
	acousticness NUMERIC,
	danceability NUMERIC, 
	energy NUMERIC,
	liveness NUMERIC,
	loudness NUMERIC,
	speechiness NUMERIC,
	valence NUMERIC,
	duration_ms INT,
	tempo NUMERIC,
	chord VARCHAR,
	PRIMARY KEY ("Index")
);

-- SELECT ALL DATA FOR EACH TABLE
SELECT * FROM top_songs;

-- IF NEED TO DELETE TO RECREATE TABLE
DROP TABLE top_songs;