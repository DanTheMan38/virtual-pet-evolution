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