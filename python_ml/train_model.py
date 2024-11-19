import pandas as pd
from sklearn.cluster import KMeans
import joblib

# Load interaction history from database export (placeholder)
data = pd.read_csv('interaction_history.csv')

# Preprocess data
features = data[['happiness', 'hunger']]

# Train a simple model (e.g., clustering personality traits)
kmeans = KMeans(n_clusters=3)
kmeans.fit(features)

# Save the model
joblib.dump(kmeans, 'personality_model.pkl')