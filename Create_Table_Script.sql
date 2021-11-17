-- CREATE TABLES FOR LOADING DATA
CREATE TABLE raw_scrape (
	index VARCHAR, 
	song_id VARCHAR,
	song_url VARCHAR,
	song VARCHAR,
	artist VARCHAR, 
	date VARCHAR, 
	position INT, 
	streams VARCHAR
)

CREATE TABLE songs (
	song_id VARCHAR,
	song VARCHAR, 
	artist VARCHAR, 
	streams INT,
	position INT, 
	danceability NUMERIC, 
	energy NUMERIC,
	key VARCHAR,
	loudness NUMERIC,
	mode VARCHAR, 
	speechiness NUMERIC,
	acousticness NUMERIC,
	instrumentalness NUMERIC,
	liveness NUMERIC,
	valence NUMERIC,
	tempo NUMERIC,
	duration_ms NUMERIC,
	time_signature VARCHAR,
	PRIMARY KEY ("song_id")
);

CREATE TABLE clean_scrape (
	song_id VARCHAR,
	song VARCHAR,
	artist VARCHAR, 
	date DATE, 
	position INT, 
	streams INT
);

CREATE TABLE features (
	song_id VARCHAR, 
	danceability NUMERIC,
	energy NUMERIC,
	key VARCHAR, 
	loudness NUMERIC, 
	mode VARCHAR, 
	speechiness NUMERIC, 
	acousticness NUMERIC, 
	instrumentalness NUMERIC, 
	liveness NUMERIC, 
	valence NUMERIC, 
	tempo NUMERIC, 
	duration_ms NUMERIC, 
	time_signature VARCHAR, 
	PRIMARY KEY ("song_id")
);

CREATE TABLE total_streams (
	song_id VARCHAR, 
	streams INT, 
	PRIMARY KEY ("song_id")
);

CREATE TABLE highest_position (
	song_id VARCHAR, 
	position INT, 
	PRIMARY KEY ("song_id")
);

CREATE TABLE track_artist (
	song_id VARCHAR, 
	song VARCHAR, 
	artist VARCHAR, 
	PRIMARY KEY ("song_id")
);

CREATE TABLE song_ml (
	index VARCHAR, 
	danceability NUMERIC, 
	energy NUMERIC,
	loudness NUMERIC,
	speechiness NUMERIC,
	acousticness NUMERIC,
	instrumentalness NUMERIC,
	liveness NUMERIC,
	valence NUMERIC,
	tempo NUMERIC,
	top_twenty NUMERIC, 
	key_type NUMERIC, 
	mode_type NUMERIC, 
	PRIMARY KEY ("index")
);

-- SELECT ALL DATA FOR EACH TABLE
SELECT * FROM raw_scrape;
SELECT * FROM songs;
SELECT * FROM clean_scrape;
SELECT * FROM features;
SELECT * FROM total_streams;
SELECT * FROM highest_position;
SELECT * FROM track_artist;
SELECT * FROM song_ml;

-- IF NEED TO DELETE TO RECREATE TABLE
DROP TABLE raw_scrape;
DROP TABLE songs;
DROP TABLE clean_scrape;
DROP TABLE features;
DROP TABLE total_streams;
DROP TABLE highest_position;
DROP TABLE track_artist;
DROP TABLE song_ml;
