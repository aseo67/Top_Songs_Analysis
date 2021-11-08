-- CREATE TABLES FOR LOADING DATA
CREATE TABLE top_songs (
	Index VARCHAR, 
	Song_ID VARCHAR,
	Song_Name VARCHAR, 
	Artist VARCHAR, 
	Number_of_Times_Charted INT,
	Highest_Charting_Position INT, 
	Week_of_Highest_Charting_start DATE,
	Week_of_Highest_Charting_end DATE,
	number_weeks_charted INT,
	Streams INT, 
	Artist_Followers INT, 
	Genre VARCHAR,
	Release_Date DATE,
	Popularity NUMERIC, 
	Acousticness NUMERIC,
	Danceability NUMERIC, 
	Energy NUMERIC,
	Liveness NUMERIC,
	Loudness NUMERIC,
	Speechiness NUMERIC,
	Valence NUMERIC,
	Tempo NUMERIC,
	Duration_ms INT,
	Chord VARCHAR,
	PRIMARY KEY (Song_ID)
);

-- SELECT ALL DATA FOR EACH TABLE
SELECT * FROM top_songs;

-- IF NEED TO DELETE TO RECREATE TABLE
DROP TABLE top_songs;