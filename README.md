# Top Songs Analysis

**_Data Analytics Bootcamp 2021 Final Project_**
<br>
<br>
**Topic:** Spotify Top 200 Charts Analysis 
<br>
<br>
**Project Questions:**
- What songs have the most streams?
- What songs have been #1 on the charts? 
- Which artists have the most streams?
- Which artists have the most songs on the chart?
- Which artists have the most #1 hits?
- Which songs are most danceable? Most energetic? Most positive-sounding (high valence)? etc.
- Can we predict if a song can break into the top 20 positions, based on the song's audio features?

**Data Source:** 
- Scraped data from Spotify Top 200 Charts
  - Top 200 Charts, Daily, United States
  - Timeframe: Jan. 1, 2021 - Nov. 17, 2021
  - Source Link: [Spotify Charts](https://spotifycharts.com/regional/us/daily/)
  - Raw Scraped Data File: [spotifytop200.csv](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Resources/spotifytop200.csv)
- Spotify audio features data for scraped tracks
  - Source Link (API Info): [Spotify - Web API - Audio Features](https://developer.spotify.com/discover/)
  - Raw Song Audio Features API Request Data File: [features.csv](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Resources/features.csv)

**Final Presentation Links**
- Google Slides: [link](https://docs.google.com/presentation/d/1-EKrs4luwS2UCQAzGb-Srn8esqcOBt605LFtJNwqsL4/edit?usp=sharing)
- Google Slides (PDF version) [pdf](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Presentation/Final%20Project_Slides_Songs%20Analysis_Seo.pdf)
- Presentation Recording: [link](https://youtu.be/jN7ACYxz4f0)

**Final Deliverables**
- Data Scraping File: [scraping.py](https://github.com/aseo67/Top_Songs_Analysis/blob/main/scraping.py)
- Data Loading/Cleaning Code: [TopSongsAnalysis_DataLoading.ipynb](https://github.com/aseo67/Top_Songs_Analysis/blob/main/TopSongsAnalysis_DataLoading.ipynb)
- SQL Script for Database Tables [Create_Merge_Table_Script.sql](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Create_Merge_Table_Script.sql)
- Database diagram: [ERD](https://github.com/aseo67/Top_Songs_Analysis/blob/main/ERD/QuickDBD-export.png)
- Exploratory Analysis Code: [TopSongsAnalysis_Exploratory.ipynb](https://github.com/aseo67/Top_Songs_Analysis/blob/main/TopSongsAnalysis_Exploratory.ipynb)
- Plotly Chart Image Files: [Visualizations](https://github.com/aseo67/Top_Songs_Analysis/tree/main/Visualizations)
- Machine Learning Model Code: [TopSongsAnalysis_Model.ipynb](https://github.com/aseo67/Top_Songs_Analysis/blob/main/TopSongsAnalysis_Model.ipynb)
- Flask Dashboard Files:
  - [index.html](https://github.com/aseo67/Top_Songs_Analysis/blob/main/templates/index.html)
  - [results.html](https://github.com/aseo67/Top_Songs_Analysis/blob/main/templates/results.html)
  - [app.py](https://github.com/aseo67/Top_Songs_Analysis/blob/main/app.py)
  - [run_ml.py](https://github.com/aseo67/Top_Songs_Analysis/blob/main/run_ml.py)
- Screenshots: [Folder](https://github.com/aseo67/Top_Songs_Analysis/tree/main/Screenshots)


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
    - Each individual track name and corresponding artist name was saved into its own dataframe ("track_artist_df")
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_TrackArtistDf.png)
4. All dataframes were saved in the database. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_UploadToDatabase.png)
5. Dataframes were joined together into a final, single dataframe to use for analysis later. 
    - SQL script was used to join the tables within the database.
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_MergeTables_SQL.png)
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/2_DataClean_FinalMergedTable.png)


## Exploratory Analysis

(see _Top_Songs_Analysis.Exploratory.ipynb_ file)
1. First, the "songs_df" table was loaded from the database
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_LoadSongDf.png)    
2. **Question 1) What songs have the most streams?**
    - The total number of unique songs on the chart since Jan. 2021 was determined.
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_NumOfSongs.png)
    - The songs are reordered from most to least streams to identify those with songs with the highest number of streams. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_TopStreamingSongs.png)
    - A visualization/bar chart has been created to show the top ten songs with the most streams. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_TopTenStreamingSongs.png)
    - The maximum, minimum, and average streams across songs have been determined. The song with the most streams is "drivers license" by Olivia Rodrigo, while the charted song with the least streams is "Monster Mash" by Bob "Boris" Pickett, The Crypt-Kickers.
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_SummaryStatsForTopSongs.png)
3. **Question 2) How many songs have reached #1 on the Top 200s chart since the beginning of 2021?**
    - The total number of unique songs to reach a #1 position on the chart since Jan. 2021 was determined.
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_NumberOneSongs.png)
4. **Question 3) Which artists have the most streams?**
    - Total streams for each artist have been aggregated, and ordered from most to least. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_TopStreamArtists.png)
    - The top ten streaming artists have been charted in the below visualization. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_TopTenStreamArtists.png)
5. **Question 4) How many artists have entered the charts?**
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_TotalChartingArtists.png)
6. **Question 5) Which artists have the most songs to have entered on the chart this year?**
    - Artists' count of charted of songs have been aggregated and reordered from most to least. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_TopChartingArtists.png)
    - The top ten charting artists have been charted in the below visualization. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_TopTenChartingArtists.png)
7. **Question 6) Which artists have the most #1 hit songs? (i.e. songs to have reached #1 on the charts)****
    - Artists' count of #1 hit songs have been aggregated and reordered from most to least. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_TopHitsArtists.png)
    - The top ten artists with the most #1 hits have been charted in the visualization below. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_TopTenHitsArtists.png)
8. **Question 7) Which songs are most danceable? Most energetic? Most positive-sounding (high valence)?, etc.**
    - Analyses were conducted for each of the focus audio features, determinining the top ten songs for each attribute. Below is an example for the 'danceability' feature, where we identify the song that's most 'danceable' as "NEO" by Aminé. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_AudioFeatTable.png)
    - The top ten songs for each feature were plotted in a bar chart; below is the chart for the 'danceability' feature. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/3_DataAnalysis_AudioFeatChart.png)
    - Additional visualizations for each of the audio features are available on the flask dashboard. 

## Machine Learning Model
The last question to answer was: **Can we predict if a song can break into the top 20 positions, based on the song's musical features?**
To answer, a random forest machine learning model was built based on songs' audio features (as inputs) and the respective chart rank grouping (as the output) - whether it fell within the top twenty or not. 

1. **Data Preprocessing** 
  - Using the "songs" table from the database (loaded into jupyter notebook as "song_df", then saved as "song_ml_df" to make preprocessing updates), an additional column was added, codifying whether a song reached a rank within the top twenty positions or not. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_AddTopTwentyCol.png)
  - Unnecessary columns (such as ID columns, and less relevant variables) have been removed. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_DropCols.png)
  - Categorical variables were identified ('key' and 'mode'), and have been encoded (using LabelEncoder) so that all columns utilize numerica data. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_EncodeCategoricalVar.png)
    - The following screenshot provides a guide on how the categorical variables' values were encoded:
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_EncodedVarGuide.png)
2. **Feature Selection** 
  - First, the model was run utilizing most of the features included in the API audio features request. The model initially focused on features that related to the musicality of the song - danceability, energy, speechiness, acousticness, instrumentalness, valence, tempo, key, and mode (major or minor). Features,  such as 'streams', 'loudness' (volume), 'duration_ms' (length of song), 'time_signature', and 'liveness', were left out of the analysis. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_AssignVar.png)
  - Upon running the model and evaluating the results, the rank of features and their contribution to the model seemed to suggest a few could be removed to try and improve the accuracy of the model. As a test, the two lowest contributing variables ('mode_type' and 'instrumentalness') were excluded and the model was rerun. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_FeaturesRanked.png)
  - However, results did not improve, and rather accuracy fell. Thus, the variables initially used in the model were kept. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_FeaturesRemovedTest_EvalModel.png)
3. **Training & Testing Sets**
  - The dataset was split into training and test sets using the _train_test_split_ function from the scikit-learn library and its default split of ~75% training. 
  - There is some class imbalance, with more songs that did _not_ achieve a rank with the top twenty. Thus, the SMOTEENN technique was utilized to resample the data and provide a better input to train the model. 
  - Finally, with the resampled data, the data was then scaled, given the values of some of the features were on very different scales. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_SplitResampleScale.png)
4. **Model Choice**
  - A random forest model was used to build this model, as it is an ensemble learning method that provides better accuracy and robustness. It utilizes several smaller, simpler decision trees trained on different pieces of data, then combined to create a strong learner. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_RFModel.png)
  - _Benefits of Random Forest Model_:
    - This model type is less prone to overfitting. 
    - It can be used to rank importance of input variables, which is helpful to narrow down the features included and create a model that is less likely to overfit and uses less trainig time. 
    - It can handle thousands of input variables, so the input set can be expanded to improve the model if needed. 
    - This model type is robust against outliers, which can be helpful with a dataset like song features and ranking (essentially, audience reception) which can be more prone to outliers than a clear-cut dataset that's less based on human preference. 
    - It can run large datasets quite efficiently, which is helpful if we want to expand this dataset even more (such as beyond just 2021). 
  - _Limitations_:
    - It's tougher to incorporate non-tabular data into random forest models without heavy modification/cleaning. If there is a wider variety of inputs to be tested to predict the outcome, it would be tough to use this model type. 
    - A deep learning model may be better at identifying variability in the dataset, given a random forest model uses a collection of weaker learners combined, with each trained on a subset of data, whereas a deep learning model can evaluate all input data within a single neuron or with multiple neurons/layers as needed. 
5. **Changes/Updates to Model Choice**
  - The random forest model has been kept, as it seems like the best fit so far out of the model explorations conducted. It allows the robustness of an ensemble learning method, but doesn't overfit as a deep learning model may. 
  - A deep learning was indeed tested to confirm whether overfitting is a risk, or if accuracy can be improved. Based on the tested run (see screenshot below), the deep learning model did show improved accuracy, but reached this level after only a few epochs, suggesting that it overfitted quickly.
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_DeepLearningTest_EvalModel.png)
6. **Model Training**
  - The random forest model was trained using 100 estimators.
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_RFModel.png)
  - Usage of more estimators was tested, but it only added a very small increase to accuracy, suggesting there isn't more improvement to be made by adding on estimators. 
    ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_MoreEstimatorsTest.png)
7. **Model Results** 
  ![Screenshot](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Screenshots/4_Model_EvalModel.png)
  - The final testing accuracy score = ~0.57, which suggests the model is correct only about half the time.
  - When diving deeper into the results with the confusion matrix, we see that we predicted 45 songs to _not_ be in the top twenty ranks, when in actuality they were; and predicted 142 songs to _be in_ the top twenty ranks, when in actuality they were not. Thus, the precision measure for determining if a song will _not_ reach top twenty is pretty good at ~0.83, but predicting top twenty songs is not as precise (with a measure of ~0.19). 
8. **Potential Future Phases & Improvements**
Given there is room for improving the model accuracy, some potential routes to take for future phases are:
  - Testing if the included features' (such as 'tempo', 'speechiness', and 'energy' - as these are the top features based on the random forest model's feature ranking) have statistically different values between songs that do reach top twenty vs. don't reach top twenty. This can be helpful in determining whether these features are useful in this model that aims to distinguish top twenty ranked songs from a dataset. 
  - Testing other new features, such as: artist popularity/followers (as artist fame can be a factor), time of year/season (for example, upbeat/summer songs may have better chance at ranking higher during the summer), etc.
