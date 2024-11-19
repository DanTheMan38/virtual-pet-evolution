# Virtual Pet Evolution

An interactive virtual pet with evolving personality traits using C++, SQL, and Python. Features real-time animations, behavior tracking, and AI-driven adaptation based on user interaction.

## Project Features
- **C++**: Handles the pet's interface and animations.
- **SQL**: Stores pet stats, behaviors, and user interaction history.
- **Python**: Utilizes machine learning to adapt the pet’s personality based on interactions.

## Folder Structure
virtual-pet-evolution/
├── cpp/                   # C++ source files for interface and animations
│   ├── main.cpp
│   ├── Pet.cpp
│   └── Pet.h
├── python_ml/             # Python scripts for machine learning
│   ├── train_model.py
│   └── predict_behavior.py
├── sql/                   # SQL scripts for database setup
│   └── database_setup.sql
├── assets/                # Images, animations, and other assets
├── docs/                  # Documentation
├── LICENSE                # MIT License file
└── README.md              # Project description and setup instructions

## Setup Instructions
1. Clone the repository:
   git clone https://github.com/DanTheMan38/virtual-pet-evolution.git
   cd virtual-pet-evolution
2. Install Python dependencies:
   pip install -r requirements.txt
3. Set up the SQL database:
   mysql -u <username> -p < sql/database_setup.sql

## Usage
1. Compile and run the C++ program:
   g++ cpp/*.cpp -o virtual_pet
   ./virtual_pet
2. Train the machine learning model:
   python python_ml/train_model.py
3. Run the personality prediction:
   python python_ml/predict_behavior.py <happiness> <hunger>

## Code Overview

### C++ Code

#### Pet.h
#ifndef PET_H
#define PET_H

#include <string>

class Pet {
public:
    Pet();
    void display();  // Render the pet on screen
    void interact(const std::string& action);  // User interactions
private:
    int happiness;
    int hunger;
    std::string personalityTrait;
    void updateState();
};

#endif // PET_H

#### Pet.cpp
#include "Pet.h"
#include <iostream>

Pet::Pet() : happiness(50), hunger(50), personalityTrait("Neutral") {}

void Pet::display() {
    std::cout << "Pet is displayed with personality: " << personalityTrait << std::endl;
}

void Pet::interact(const std::string& action) {
    if (action == "feed") {
        hunger -= 10;
    } else if (action == "play") {
        happiness += 10;
    }
    updateState();
}

void Pet::updateState() {
    if (happiness > 70) {
        personalityTrait = "Happy";
    } else if (hunger > 70) {
        personalityTrait = "Hungry";
    } else {
        personalityTrait = "Neutral";
    }
}

#### main.cpp
#include "Pet.h"
#include <iostream>

int main() {
    Pet myPet;
    myPet.display();

    std::string action;
    while (true) {
        std::cout << "What would you like to do? (feed/play/exit): ";
        std::cin >> action;

        if (action == "exit") break;

        myPet.interact(action);
        myPet.display();
    }

    return 0;
}

### SQL Code

#### database_setup.sql
CREATE DATABASE virtual_pet;

USE virtual_pet;

CREATE TABLE interactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    action VARCHAR(50),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pet_state (
    id INT AUTO_INCREMENT PRIMARY KEY,
    happiness INT,
    hunger INT,
    personality_trait VARCHAR(50),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

### Python Code

#### train_model.py
import pandas as pd
from sklearn.cluster import KMeans
import joblib

data = pd.read_csv('interaction_history.csv')
features = data[['happiness', 'hunger']]
kmeans = KMeans(n_clusters=3)
kmeans.fit(features)
joblib.dump(kmeans, 'personality_model.pkl')

#### predict_behavior.py
import joblib
import sys

kmeans = joblib.load('personality_model.pkl')
happiness = int(sys.argv[1])
hunger = int(sys.argv[2])
cluster = kmeans.predict([[happiness, hunger]])
personality_trait = ['Happy', 'Hungry', 'Neutral'][cluster[0]]
print(personality_trait)

## License
This project is licensed under the MIT License - see the LICENSE file for details.