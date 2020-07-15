#include <iostream>

#include "Player.h"
#include "MapCell.h"
#include "GameMap.h"

using namespace std;

int main() {
    Player hero;
    GameMap gameMap;

    gameMap.drawIntro();
    gameMap.setPlayerCell(hero.xPosition, hero.yPosition);

    while (!gameMap.isGameOver) {
        gameMap.draw();
        hero.callInput();
        if ( !gameMap.setPlayerCell(hero.xPosition, hero.yPosition) ) {
            hero.resetToLastPosition();
        }
    }

    return 0;
}
