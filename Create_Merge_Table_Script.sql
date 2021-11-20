-- TABLE FOR RAW SPOTIFY TOP 200 CHART (U.S) DATA SCRAPE
CREATE TABLE raw_scrape (
	song_id VARCHAR,
	song_url VARCHAR,
	song VARCHAR,
	artist VARCHAR, 
	date DATE, 
	position INT, 
	streams VARCHAR
)

-- TABLE FOR SPOTIFY API PULL OF EACH SONG'S FEATURES
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
	duration_ms INT, 
	time_signature VARCHAR, 
	PRIMARY KEY ("song_id")
);

-- TABLE FOR CLEANED (via jupyter notebook file) SCRAPE DATA 
CREATE TABLE clean_scrape (
	song_id VARCHAR,
	song VARCHAR,
	artist VARCHAR, 
	date DATE, 
	position INT, 
	streams INT
);

-- TABLE OF TOTAL STREAMS DATA FOR EACH SONG
CREATE TABLE total_streams (
	song_id VARCHAR, 
	streams INT, 
	PRIMARY KEY ("song_id")
);

-- TABLE OF HIGHEST POSITION RANKING FOR EACH SONG
CREATE TABLE highest_position (
	song_id VARCHAR, 
	position INT, 
	PRIMARY KEY ("song_id")
);

-- TABLE LISTING EACH TRACK & ARTIST & SONG ID
CREATE TABLE track_artist (
	song_id VARCHAR, 
	song VARCHAR, 
	artist VARCHAR, 
	PRIMARY KEY ("song_id")
);

-- SCRIPT FOR JOINING total_streams, highest_position, track_artist TABLES AND features TABLE (via SQL)
SELECT DISTINCT ON (ta.song_id) ta.song_id, 
	ta.song, 
	ta.artist, 
	ts.streams, 
	hp.position, 
	f.danceability, 
	f.energy, 
	f.key, 
	f.loudness, 
	f.mode, 
	f.speechiness, 
	f.acousticness, 
	f.instrumentalness, 
	f.liveness, 
	f.valence, 
	f.tempo, 
	f.duration_ms, 
	f.time_signature
INTO songs
FROM track_artist AS ta
JOIN total_streams AS ts
ON (ta.song_id = ts.song_id)
JOIN highest_position AS hp
ON (ta.song_id = hp.song_id)
JOIN features AS f
ON (ta.song_id = f.song_id);

-- CREATE TABLE FOR FINAL MACHINE LEARNING MODEL DATAFRAME
CREATE TABLE song_ml (
	song_id VARCHAR, 
	danceability NUMERIC, 
	energy NUMERIC,
	speechiness NUMERIC,
	acousticness NUMERIC,
	instrumentalness NUMERIC,
	valence NUMERIC,
	tempo NUMERIC,
	top_twenty VARCHAR, 
	key_type NUMERIC, 
	mode_type NUMERIC, 
	PRIMARY KEY ("song_id")
);

-- SELECT ALL DATA SCRIPT FOR EACH TABLE
SELECT * FROM raw_scrape;
SELECT * FROM clean_scrape;
SELECT * FROM features;
SELECT * FROM total_streams;
SELECT * FROM highest_position;
SELECT * FROM track_artist;
SELECT * FROM songs;
SELECT * FROM song_ml;

-- SCRIPT IN CASE NEED TO DELETE ANY TABLES
DROP TABLE raw_scrape;
DROP TABLE clean_scrape;
DROP TABLE features;
DROP TABLE total_streams;
DROP TABLE highest_position;
DROP TABLE track_artist;
DROP TABLE songs;
DROP TABLE song_ml;
