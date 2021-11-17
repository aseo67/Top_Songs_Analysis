# Import dependencies
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sqlalchemy import create_engine

def predictions(
    danceability, 
    energy, 
    loudness, 
    speechiness, 
    acousticness, 
    instrumentalness, 
    liveness, 
    valence, 
    tempo, 
    duration_ms, 
    key_type, 
    mode_type, 
    time_sig_type
):
    # Set up connection to database
    from config import db_pswd
    engine = create_engine(f'postgresql://postgres:{db_pswd}@localhost:5432/project_spotify_db')
    # Load in dataframe for machine learning model from database
    song_ml_rf_df = pd.read_sql('SELECT * FROM song_ml;', engine, index_col='index')
    song_ml_rf_df.head()

    # Assign preprocessed data into features and target arrays
    y = song_ml_rf_df["top_twenty"].ravel()
    X = song_ml_rf_df.drop(["top_twenty"], 1)

    # Split preprocessed data into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    # Create StandardScaler instances
    scaler = StandardScaler()
    # Fit the StandardScaler
    X_scaler = scaler.fit(X_train)
    # Scale data
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)

    # Create a random forest classifier
    rf_model = RandomForestClassifier(n_estimators=100, random_state=1)
    # Fitting the model
    rf_model = rf_model.fit(X_train_scaled, y_train)

    # Training score & Testing score
    print(f'Training Data Score: {rf_model.score(X_train_scaled, y_train)}')
    print(f'Testing Data Score: {rf_model.score(X_test_scaled, y_test)}')

    # Return result
    return rf_model.predict([[
        danceability, 
        energy, 
        loudness, 
        speechiness, 
        acousticness, 
        instrumentalness, 
        liveness, 
        valence, 
        tempo, 
        duration_ms, 
        key_type, 
        mode_type, 
        time_sig_type
    ]])

