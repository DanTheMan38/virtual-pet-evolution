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