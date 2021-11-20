from flask import Flask, render_template, request
from run_ml import predictions
import pandas as pd
from sqlalchemy import create_engine
import plotly
import plotly.express as px
import json

app = Flask(__name__)

@app.route("/")
def index(): 

    # Set up connection to database
    from config import db_pswd
    engine = create_engine(f'postgresql://postgres:{db_pswd}@localhost:5432/project_spotify_db')
    # Load in dataframe for machine learning model from database
    song_df = pd.read_sql('SELECT * FROM songs;', engine, index_col='song_id')
    song_df.head()

    # Create dataframe for songs' total streams
    song_streams_df = song_df[['song', 'artist', 'streams']]
    song_streams_df = song_streams_df.sort_values(['streams'], ascending=False)
    top_ten_streams = song_streams_df[:10]
    # Create visualization 1: top streaming songs
    fig1 = px.bar(
        top_ten_streams, 
        x='song', 
        y='streams',
        color='artist', 
        title='Top 10 Streamed Songs of 2021', 
        labels={'song':'Song', 'streams':'Number of Streams', 'artist':'Artist'}
    ).update_xaxes(categoryorder='total descending', tickangle=45)
    # Encode chart as json
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Create dataframe sorting for artists' songs
    artists_grouped = song_df[['artist', 'song']].groupby(['artist'])
    artist_song_count_df = pd.DataFrame(artists_grouped['song'].count())
    artist_song_count_df = artist_song_count_df.rename(columns={'song':'count_of_charted_songs'})
    artist_song_count_df = artist_song_count_df.sort_values(['count_of_charted_songs'], ascending=False)
    artist_song_count_df = artist_song_count_df.reset_index()
    # Create visualization 2: top charting artists
    artists_most_songs = artist_song_count_df[:10]
    fig2 = px.bar(
        artists_most_songs, 
        x='artist', 
        y='count_of_charted_songs',
        title='Artists with Most Charted Songs of 2021',
        labels={'artist':'Artist', 'count_of_charted_songs':'Number of Charted Songs'}
    ).update_xaxes(tickangle=45)
    # Encode chart as json
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Create dataframe for artists' streams
    artist_streams_grouped = song_df[['artist', 'streams']].groupby(['artist'])
    artist_streams_total_df = pd.DataFrame(artist_streams_grouped['streams'].sum())
    artist_streams_total_df = artist_streams_total_df.sort_values(['streams'], ascending=False)
    artist_streams_total_df = artist_streams_total_df.reset_index()
    artists_most_streams = artist_streams_total_df[:10]
    # Create visualization 3: top streaming artists
    fig3 = px.bar(
        artists_most_streams, 
        x='artist', 
        y='streams',
        title='Artists with Most Streams',
        labels={'artist':'Artist', 'streams':'Total Number of Streams'}
    ).update_xaxes(tickangle=45)
    # Encode chart as json
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    # Create dataframe for artists with #1 hits
    artist_hits_df = song_df.loc[song_df["position"] == 1, ['artist', 'song', 'position']]
    artist_hits_grouped = artist_hits_df[['artist', 'song']].groupby(['artist'])
    total_hits_by_artist_df = pd.DataFrame(artist_hits_grouped['song'].count())
    total_hits_by_artist_df = total_hits_by_artist_df.rename(columns={'song':'count_of_number_ones'})
    total_hits_by_artist_df = total_hits_by_artist_df.sort_values(['count_of_number_ones'], ascending=False)
    total_hits_by_artist_df = total_hits_by_artist_df.reset_index()
    artists_most_hits = total_hits_by_artist_df[:10]
    # Create visualization 4: top artists with hits
    fig4 = px.bar(
        artists_most_hits, 
        x='artist', 
        y='count_of_number_ones',
        title='Artists with Most #1 Hits',
        labels={'artist':'Artist', 'count_of_number_ones':'Number of #1 Hits'}
    ).update_yaxes(nticks=4).update_xaxes(tickangle=45)
    # Encode chart as json
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", graph1JSON=graph1JSON, graph2JSON=graph2JSON, graph3JSON=graph3JSON, graph4JSON=graph4JSON)

@app.route("/predict", methods=["POST"])
def predict():
    # Get data from POST request
    if request.method == "POST":
        danceability = request.form["danceability"]
        print(danceability)

        energy = request.form["energy"]
        print(energy)

        speechiness = request.form["speechiness"]
        print(speechiness)

        acousticness = request.form["acousticness"]
        print(acousticness)

        instrumentalness = request.form["instrumentalness"]
        print(instrumentalness)

        valence = request.form["valence"]
        print(valence)

        tempo = request.form["tempo"]
        print(tempo)

        key_type = request.form["key_type"]
        print(key_type)

        mode_type = request.form["mode_type"]
        print(mode_type)

        # Predictions
        prediction = predictions(
            danceability,
            energy,
            speechiness,
            acousticness,
            instrumentalness,
            valence,
            tempo,
            key_type,
            mode_type
        )
        output = prediction[0]
        print(output)

        results = ""
        if(output == '0'):
            results = "Not Top 20."
        elif(output == '1'):
            results = "Top 20!"
        print(results)

        return render_template("results.html", results=results)