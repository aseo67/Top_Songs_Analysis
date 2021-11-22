Machine learning model (in README & Presentation)
✓ Description of data preprocessing 
✓ Description of feature engineering and the feature selection, including the team's decision-making process 
✓ Description of how data was split into training and testing sets 
✓ Explanation of model choice, including limitations and benefits 
✓ Explanation of changes in model choice (if changes occurred between the Segment 2 and Segment 3 deliverables) 
✓ Description of how model was trained (or retrained, if they are using an existing model) 
✓ Description and explanation of model’s confusion matrix, including final accuracy score
✓ Additionally, the model obviously addresses the question or problem the team is solving.
✓ If statistical analysis is not included as part of the current analysis, include a description of how it would be included in the next phases of the project.

Dashboard/Flask App
✓ Presents a data story that is logical and easy to follow
✓ Data (images or report) from the machine learning task



# Top Songs Analysis
Data Analytics Bootcamp 2021 Final Project
**Topic:** Spotify Top 200 Charts Analysis 
**Project Questions:**
- What songs have the most streams?
- Which artists have the most streams?
- Which artists have the most songs on the chart?
- What songs have been #1 on the charts? 
- Which artists have the most #1 hits?
- Which songs are most danceable? Most energetic? Most positive-sounding (high valence)? 
- Can we predict if a song can break into the top 20 positions, based on the song's musical features?

**Data Source:** 
- Scraped data from Spotify Top 200 Charts
  - Top 200 Charts, Daily
  - Country: United States
  - Timeframe: Jan. 1, 2021 - Nov. 17, 2021
  - Source Link: [Spotify Charts](https://spotifycharts.com/regional/us/daily/)
  - Raw Scraped Data File: [spotifytop200.csv](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Resources/spotifytop200.csv)
  - Raw API Request Data for Song Features: [features.csv](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Resources/features.csv)
- Corresponding Spotify audio features data for scraped tracks
  - Source Link (API): [Spotify - Web API - Audio Features](https://developer.spotify.com/discover/)

**Final Presentation Links**
- Google Slides: [link](https://docs.google.com/presentation/d/1-EKrs4luwS2UCQAzGb-Srn8esqcOBt605LFtJNwqsL4/edit?usp=sharing)
- Google Slides (PPT version) [link]()
- Presentation Recording: [link]()

**Final Deliverables**
- Data Scraping File: [scraping.py](https://github.com/aseo67/Top_Songs_Analysis/blob/main/scraping.py)
- Data Loading/Cleaning Code: [TopSongsAnalysis_DataLoading.ipynb](https://github.com/aseo67/Top_Songs_Analysis/blob/main/TopSongsAnalysis_DataLoading.ipynb)
- SQL Script for Database Tables [Create_Merge_Table_Script.sql](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Create_Merge_Table_Script.sql)
- Database diagram: [ERD](https://github.com/aseo67/Top_Songs_Analysis/blob/main/ERD/QuickDBD-export.png)
- Exploratory Analysis Code: [TopSongsAnalysis_Exploratory.ipynb](https://github.com/aseo67/Top_Songs_Analysis/blob/main/TopSongsAnalysis_Exploratory.ipynb)
- Plotly Chart Images: [Visualizations](https://github.com/aseo67/Top_Songs_Analysis/tree/main/Visualizations)
- Machine Learning Model Code: [TopSongsAnalsis_Model.ipynb](https://github.com/aseo67/Top_Songs_Analysis/blob/main/TopSongsAnalysis_Model.ipynb)
- Flask Dashboard Files:
  - [index.html](https://github.com/aseo67/Top_Songs_Analysis/blob/main/templates/index.html)
  - [results.html](https://github.com/aseo67/Top_Songs_Analysis/blob/main/templates/results.html)
  - [app.py](https://github.com/aseo67/Top_Songs_Analysis/blob/main/app.py)
  - [run_ml.py](https://github.com/aseo67/Top_Songs_Analysis/blob/main/run_ml.py)

## Data Extraction
1. First, data was extracted from Spotify using python script to automatically read through the Spotify United States daily Top 200 chart tracks, their ranks, and streams via the _scraping.py_ file. 
    - This script runs through each date/page since January 1, 2021 through November 17, 2021 (two days prior to the date of scraping). 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/1_DataExtract_ListDatesToScrape.png)
    - The song info for each day's charted songs - for track title, artist, song url (on Spotify), chart rank/position, # of streams, and date of chart - were scraped. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/1_DataExtract_ScrapeFunction.png)
    - The resulting data is saved as a csv file (_spotifytop200.csv_, located in the Resources folder), and uploaded to the postgreSQL database as the "raw_scrape" table. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/1_DataExtract_RawScrapeConvertSaveUpload.png)

2. Next, the corresponding audio features data was pulled using a Spotify API request (see _Top_Songs_Analysis.DataLoading.ipynb_ file for all data loading/cleaning code).
    - First, the "raw_scrape" table was sourced into the jupyter notebook as "scrape_df" from the postgreSQL database. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/1_DataExtract_RawScrapeAsPandasDf.png)
    - A list of song ids was created from the data in this dataframe, which is then split into groups of 100 or less. This is so API requests can be made in batches of 100 song ids (limit for this API request).
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/1_DataExtract_ListSongIDsForAPI.png)
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/1_DataExtract_BatchSongIDs.png)
    - The API request is conducted and the corresponding audio features data is received as a json in the jupyter notebook, which is then converted into a pandas dataframe for easier cleaning. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/1_DataExtract_AudioFeatAPI.png)
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/1_DataExtract_APIReqToPandasDf.png)
    
## Data Cleaning
(continued on _Top_Songs_Analysis.DataLoading.ipynb_ file)
1. First, the "features_df" was cleaned.
    - Unnecessary columns were removed, and appropriate values for the 'key' and 'mode' columns were relabeled for clarity. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_FeaturesDfDropCol.png)
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_FeaturesReplaceVal.png)
    - Data types were checked and fixed, along with checking for any null values in the table.
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_FeaturesCheckDataTypeAndNulls.png)
    - The final table was saved as a csv.
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_SaveFeaturesDfCSV.png)
2. Similarly, the "scrape_df" was also cleaned. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_ScrapeDfClean.png)
3. Select focus columns were separated and compiled into its own dataframes - to be used in merging into a final dataframe later. 
    - The total streams for each song were aggregated across all dates into a separate dataframe ("total_streams_df"). 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_TotalStreamsDf.png)
    - The highest position for each song was determined and saved as a separate dataframe ("highest_position_df").
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_HighestPositionDf.png)
    - Each indivdual track name and corresponding artist name was saved into its own dataframe ("track_artist_df")
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_TrackArtistDf.png)
4. All dataframes were saved in the database. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_UploadToDatabase.png)
6. Dataframes were joined together into a final, single dataframe to use for analysis later. 
    - SQL script was used to join the tables within the database.
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_MergeTables_SQL.png)
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_FinalMergedTable.png)

## Exploratory Analysis

![Screenshot]()

## Machine Learning Model

![Screenshot]()
