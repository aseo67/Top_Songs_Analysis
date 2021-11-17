from flask import Flask, render_template, request
from run_ml import predictions

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get data from POST request
    if request.method == "POST":
        danceability = float(request.form["danceability"])
        print(danceability)

        energy = float(request.form["energy"])
        print(energy)

        loudness = int(request.form["loudness"])
        print(loudness)

        speechiness = float(request.form["speechiness"])
        print(speechiness)

        acousticness = float(request.form["acousticness"])
        print(acousticness)

        instrumentalness = float(request.form["instrumentalness"])
        print(instrumentalness)

        liveness = float(request.form["liveness"])
        print(liveness)

        valence = float(request.form["valence"])
        print(valence)

        tempo = int(request.form["tempo"])
        print(tempo)

        key_type = int(request.form["key_type"])
        print(key_type)

        mode_type = request.form["mode_type"]
        print(mode_type)

        # Predictions
        prediction = predictions(
            danceability,
            energy,
            loudness,
            speechiness,
            acousticness,
            instrumentalness,
            liveness,
            valence,
            tempo,
            key_type,
            mode_type
        )
        output = prediction[0]

        results = ""
        if(output == 0):
            results = "Not Top 10"
        elif(output == 1):
            results = "Top 10!"

        return render_template("results.html", results=results)