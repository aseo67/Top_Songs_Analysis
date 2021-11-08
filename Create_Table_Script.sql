-- CREATE TABLES FOR LOADING DATA
CREATE TABLE top_songs (
	Song_Name VARCHAR, 
	Song_ID VARCHAR,
	Artist VARCHAR, 
	Number_of_Times_Charted INT,
	Highest_Charting_Position INT, 
	Streams INT, 
	Artist_Followers INT, 
	Genre VARCHAR,
	Release_Date DATE,
	Popularity NUMERIC, 
	Danceability NUMERIC, 
	Energy NUMERIC,
	Loudness NUMERIC,
	Speechiness NUMERIC,
	Acousticness NUMERIC,
	Liveness NUMERIC,
	TEMPO NUMERIC,
	Duration INT,
	Valence NUMERIC,
	Chord VARCHAR,
	Week_of_Highest_Charting_start DATE,
	Week_of_Highest_Charting_end DATE,
	number_weeks_charted int,
	PRIMARY KEY (Song_ID)
);

-- SELECT ALL DATA FOR EACH TABLE

SELECT * FROM top_songs;

-- IF NEED TO DELETE TO RECREATE TABLE
DROP TABLE top_songs;