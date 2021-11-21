# Import dependencies
import pandas as pd
from sklearn.preprocessing import StandardScaler
from collections import Counter
from imblearn.combine import SMOTEENN
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sqlalchemy import create_engine

def predictions(
    danceability, 
    energy, 
    speechiness, 
    acousticness, 
    instrumentalness, 
    valence, 
    tempo, 
    key_type, 
    mode_type 
):
    # Set up connection to database
    from config import db_pswd
    engine = create_engine(f'postgresql://postgres:{db_pswd}@localhost:5432/project_spotify_db')
    # Load in dataframe for machine learning model from database
    song_ml_df = pd.read_sql('SELECT * FROM song_ml;', engine, index_col="song_id")

    # Assign preprocessed data into features and target arrays
    y = song_ml_df["top_twenty"].ravel()
    X = song_ml_df.drop(["top_twenty"], 1)
    Counter(y)
    # Split preprocessed data into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    Counter(y_train)

    # Data resampled with SMOTEENN
    smote_enn = SMOTEENN(random_state=1)
    X_resampled, y_resampled = smote_enn.fit_resample(X_train, y_train)
    Counter(y_resampled)

    # Create StandardScaler instances
    scaler = StandardScaler()
    # Fit the StandardScaler
    X_scaler = scaler.fit(X_resampled)
    # Scale data
    X_train_scaled = X_scaler.transform(X_resampled)
    X_test_scaled = X_scaler.transform(X_test)

    # Create a random forest classifier
    rf_model = RandomForestClassifier(n_estimators=100, random_state=1)
    # Fitting the model
    rf_model = rf_model.fit(X_train_scaled, y_resampled)

    # Training score & Testing score
    print(f'Training Data Score: {rf_model.score(X_train_scaled, y_resampled)}')
    print(f'Testing Data Score: {rf_model.score(X_test_scaled, y_test)}')

    # Return result
    return rf_model.predict([[
        danceability, 
        energy, 
        speechiness, 
        acousticness, 
        instrumentalness, 
        valence, 
        tempo, 
        key_type, 
        mode_type 
    ]])

