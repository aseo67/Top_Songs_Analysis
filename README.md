Main branch should include: 
✓ All code necessary to perform exploratory analysis 
✓ All code necessary to complete machine learning portion of project 
✓ Any images that have been created (at least three) 
✓ Requirements.txt file

README.md must include: 
✓ Cohesive, structured outline of the project (this may include images, but
should be easy to follow and digest) 
✓ Link to dashboard (or link to video of dashboard demo) - Flask App
✓ Link to Google Slides presentation

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
✓ Images from the initial analysis 
✓ Data (images or report) from the machine learning task 
✓ At least one interactive element (machine learning predictions)

Presentation/Slides
✓ Selected topic 
✓ Reason why they selected their topic 
✓ Description of their source of data 
✓ Questions they hope to answer with the data 
✓ Description of the data exploration phase of the project 
✓ Description of the analysis phase of the project 
✓ Technologies, languages, tools, and algorithms used throughout the project 
✓ Result of analysis 
✓ Recommendation for future analysis 
✓ Anything the team would have done differently 




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
  - Scraped Data File: [spotifytop200.csv](https://github.com/aseo67/Top_Songs_Analysis/blob/main/Resources/spotifytop200.csv)
- Corresponding Spotify audio features data for scraped tracks
  - Source Link (API): [Spotify - Web API - Audio Features](https://developer.spotify.com/discover/)

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

![Screenshot]()

## Data Cleaning

![Screenshot]()

## Exploratory Analysis

![Screenshot]()

## Machine Learning Model

![Screenshot]()
