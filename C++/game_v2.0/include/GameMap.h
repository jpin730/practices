#ifndef GAMEMAP_H
#define GAMEMAP_H

#include "MapCell.h"

class  GameMap {
    public:
        GameMap();

        MapCell cell[15][10];
        MapCell* playerCell;
        bool isGameOver;

        void drawIntro();
        void drawVictory();
        void draw();
        bool setPlayerCell(int xPosition, int yPosition);

    protected:
        void loadMapFromFile();

    private:
};

#endif // GAMEMAP_H
