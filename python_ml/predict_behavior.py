import joblib
import sys

# Load the trained model
kmeans = joblib.load('personality_model.pkl')

# Receive current pet state as command-line arguments
happiness = int(sys.argv[1])
hunger = int(sys.argv[2])

# Predict personality trait
cluster = kmeans.predict([[happiness, hunger]])
personality_trait = ['Happy', 'Hungry', 'Neutral'][cluster[0]]

print(personality_trait)