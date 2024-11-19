#include "Pet.h"
#include <iostream>

Pet::Pet() : happiness(50), hunger(50), personalityTrait("Neutral") {}

void Pet::display() {
    // Placeholder for rendering logic
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
    // Update personalityTrait based on happiness and hunger
    // This could be replaced with data from the ML model
    if (happiness > 70) {
        personalityTrait = "Happy";
    } else if (hunger > 70) {
        personalityTrait = "Hungry";
    } else {
        personalityTrait = "Neutral";
    }
}