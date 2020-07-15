#ifndef PLAYER_H
#define PLAYER_H

class Player {
    public:
        Player();

        int xPosition, yPosition;
        int lastX, lastY;

        void callInput();
        void resetToLastPosition();

    protected:

    private:
};

#endif // PLAYER_H
