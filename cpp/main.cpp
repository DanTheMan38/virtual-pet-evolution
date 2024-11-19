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