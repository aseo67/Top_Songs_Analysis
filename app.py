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

    # Creat dataframe for top 'danceability' songs
    dance_df = song_df[['artist', 'song', 'danceability']]
    dance_df = dance_df.sort_values(['danceability'], ascending=False)
    toptendanceable = dance_df[:10]
    # Create visualization 5: top 'danceability' songs
    fig5 = px.bar(
        toptendanceable, 
        x='song', 
        y='danceability',
        title='Top Ten Danceable Songs',
        hover_data=['artist'],
        labels={'song':'Song', 'artist':'Artist', 'danceability': 'Danceability'}
    ).update_xaxes(tickangle=45)
    # Encode chart as json
    graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

    # Creat dataframe for top 'energy' songs
    energy_df = song_df[['artist', 'song', 'energy']]
    energy_df = energy_df.sort_values(['energy'], ascending=False)
    toptenenergy = energy_df[:10]
    # Create visualization 6: top 'energy' songs
    fig6 = px.bar(
        toptenenergy, 
        x='song', 
        y='energy',
        title='Top Ten Energetic Songs',
        hover_data=['artist'],
        labels={'song':'Song', 'artist':'Artist', 'energy': 'Energy'}
    ).update_xaxes(tickangle=45)
    # Encode chart as json
    graph6JSON = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)

    # Creat dataframe for top 'speechy' songs
    speech_df = song_df[['artist', 'song', 'speechiness']]
    speech_df = speech_df.sort_values(['speechiness'], ascending=False)
    toptenspeechy = speech_df[:10]
    # Create visualization 7: top 'speechy' songs
    fig7 = px.bar(
        toptenspeechy, 
        x='song', 
        y='speechiness',
        title='Top Ten "Speechy" Songs',
        hover_data=['artist'],
        labels={'song':'Song', 'artist':'Artist', 'speechiness': 'Speechiness'}
    ).update_xaxes(tickangle=45)
    # Encode chart as json
    graph7JSON = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)

    # Create dataframe for top 'acoustic' songs
    acoustic_df = song_df[['artist', 'song', 'acousticness']]
    acoustic_df = acoustic_df.sort_values(['acousticness'], ascending=False)
    toptenacoustic = acoustic_df[:10]
    # Create visualization 8: top 'acoustic' songs
    fig8 = px.bar(
        toptenacoustic, 
        x='song', 
        y='acousticness',
        title='Top Ten Acoustic Songs',
        hover_data=['artist'],
        labels={'song':'Song', 'artist':'Artist', 'acousticness': 'Acousticness'}
    ).update_xaxes(tickangle=45)
    # Encode chart as json
    graph8JSON = json.dumps(fig8, cls=plotly.utils.PlotlyJSONEncoder)

    # Create dataframe for top 'instrumental' songs
    instrument_df = song_df[['artist', 'song', 'instrumentalness']]
    instrument_df = instrument_df.sort_values(['instrumentalness'], ascending=False)
    topteninstrumental = instrument_df[:10]
    # Create visualization 9: top 'instrumental' songs
    fig9 = px.bar(
        topteninstrumental, 
        x='song', 
        y='instrumentalness',
        title='Top Ten Instrumentalness Songs',
        hover_data=['artist'],
        labels={'song':'Song', 'artist':'Artist', 'instrumentalness': 'Instrumentalness'}
    ).update_xaxes(tickangle=45)
    # Encode chart as json
    graph9JSON = json.dumps(fig9, cls=plotly.utils.PlotlyJSONEncoder)

    # Create dataframe for top 'positive' songs
    valence_df = song_df[['artist', 'song', 'valence']]
    valence_df = valence_df.sort_values(['valence'], ascending=False)
    toptenpositive = valence_df[:10]
    # Create visualization 10: top 'positive' songs
    fig10 = px.bar(
        toptenpositive, 
        x='song', 
        y='valence',
        title='Top Ten Positive Songs',
        hover_data=['artist'],
        labels={'song':'Song', 'artist':'Artist', 'valence': 'Valence'}
    ).update_xaxes(tickangle=45)
    # Encode chart as json
    graph10JSON = json.dumps(fig10, cls=plotly.utils.PlotlyJSONEncoder)

    # Create dataframe for fastest songs
    tempo_df = song_df[['artist', 'song', 'tempo']]
    tempo_df = tempo_df.sort_values(['tempo'], ascending=False)
    toptenfast = tempo_df[:10]
    # Create visualization 11: fastest songs
    fig11 = px.bar(
        toptenfast, 
        x='song', 
        y='tempo',
        title='Top Ten Fast Songs',
        hover_data=['artist'],
        labels={'song':'Song', 'artist':'Artist', 'tempo': 'Tempo'}
    ).update_xaxes(tickangle=45)
    # Encode chart as json
    graph11JSON = json.dumps(fig11, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", 
        graph1JSON=graph1JSON, 
        graph2JSON=graph2JSON, 
        graph3JSON=graph3JSON, 
        graph4JSON=graph4JSON, 
        graph5JSON=graph5JSON, 
        graph6JSON=graph6JSON, 
        graph7JSON=graph7JSON, 
        graph8JSON=graph8JSON, 
        graph9JSON=graph9JSON, 
        graph10JSON=graph10JSON, 
        graph11JSON=graph11JSON
    )

@app.route("/predict", methods=["POST"])
def predict():
    # Get data from POST request
    if request.method == "POST":
        danceability = float(request.form["danceability"])
        print(danceability)

        energy = float(request.form["energy"])
        print(energy)

        speechiness = float(request.form["speechiness"])
        print(speechiness)

        acousticness = float(request.form["acousticness"])
        print(acousticness)

        instrumentalness = float(request.form["instrumentalness"])
        print(instrumentalness)

        valence = float(request.form["valence"])
        print(valence)

        tempo = int(request.form["tempo"])
        print(tempo)

        key_type = int(request.form["key_type"])
        print(key_type)

        mode_type = int(request.form["mode_type"])
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
        output = int(prediction[0])
        print(output)

        results = ""
        if(output == 0):
            results = "Not Top 20."
        elif(output == 1):
            results = "Top 20!"
        print(results)

        return render_template("results.html", results=results)