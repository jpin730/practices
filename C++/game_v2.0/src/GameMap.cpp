#include "GameMap.h"

#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

GameMap::GameMap() {
    playerCell = NULL;
    loadMapFromFile();
    isGameOver = false;
}

void GameMap::drawIntro() {
    system("clear");
    string line;
    ifstream fileIn("intro.txt");
    if ( fileIn.is_open() ) {
        while ( getline(fileIn, line) ) {
            cout << line << endl;
        }
        cin.ignore();
    }
    else {
        cout << "ERROR: INTRO FILE COULD NOT BE LOADED.\n";
    }
}

void GameMap::drawVictory() {
    system("clear");
    string line;
    ifstream fileIn("victory.txt");
    if ( fileIn.is_open() ) {
        while ( getline(fileIn, line) ) {
            cout << line << endl;
        }
    }
    else {
        cout << "ERROR: VICTORY FILE COULD NOT BE LOADED.\n";
    }
}

void GameMap::draw() {
    system("clear");
    for (int i = 0; i < 15; i++) {
        for (int j = 0; j < 10; j++) {
            cout << " " << cell[i][j].id;
        }
        cout << endl;
    }
    cout << "\nUP:\tw\tDOWN:\ts\nLEFT:\ta\tRIGHT:\td\n\nEnter move key: ";
}

bool GameMap::setPlayerCell(int xPosition, int yPosition) {
    if ( !cell[yPosition][xPosition].isBlocked() ) {
        if (cell[yPosition][xPosition].id == '$') {
            drawVictory();
            isGameOver = true;
            return true;
        }
        else {
            if (playerCell != NULL) {
                playerCell->id = ' ';
            }
            playerCell = &cell[yPosition][xPosition];
            playerCell->id = 'H';
        }
        return true;
    }
    else {
        return false;
    }
}

void GameMap::loadMapFromFile() {
    string line;

    ifstream fileIn("map.txt");
    if ( fileIn.is_open() ) {
        int row = 0;
        while ( getline(fileIn, line) ) {
            for (int col = 0; col < line.length(); col++) {
                if (line[col] == '0') {
                    cell[row][col].id = ' ';
                }
                else {
                    cell[row][col].id = line[col];
                }
            }
            row++;
        }
    }
    else {
        cout << "ERROR: MAP FILE COULD NOT BE LOADED.\n";
    }
}
