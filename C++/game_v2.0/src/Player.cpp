#include "Player.h"

#include <iostream>

using namespace std;

Player::Player() {
    xPosition = 1;
    yPosition = 1;
}

void Player::callInput() {
    char userInput;
    cin >> userInput;
    lastX = xPosition;
    lastY = yPosition;
    switch (userInput) {
        case 'w':
            yPosition--;
            break;
        case 'd':
            xPosition++;
            break;
        case 's':
            yPosition++;
            break;
        case 'a':
            xPosition--;
            break;
    }
}

void Player::resetToLastPosition() {
    xPosition = lastX;
    yPosition = lastY;
}
