# AIM: DRIVER PROGRAM THAT LOADS COMPUTER AND PLAYER AND STARTS THE GAME TO COMPETE WITH EACH OTHER.

from Grid import Grid
from Computer import Computer
from Player import Player
from Displayer import Displayer
from random import randint
import time

defaultInitialTiles = 2
defaultProbability = 0.9

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}

(PLAYER_TURN, COMPUTER_TURN) = (0, 1)

# Time Limit Before Losing
timeLimit = 0.2
allowance = 0.05


class GameManager:
    def __init__(self, size=4):
        self.grid = Grid(size)
        self.possibleNewTiles = [2, 4]
        self.probability = defaultProbability
        self.initTiles = defaultInitialTiles
        self.computer = None
        self.player = None
        self.displayer = None
        self.over = False

    def setComputer(self, computer):
        self.computer = computer

    def setPlayer(self, player):
        self.player = player

    def setDisplayer(self, displayer):
        self.displayer = displayer

    def updateAlarm(self, currTime):
        if currTime - self.prevTime > timeLimit + allowance:
            self.over = True
        else:
            while time.clock() - self.prevTime < timeLimit + allowance:
                pass

            self.prevTime = time.clock()

    def start(self):
        for i in range(self.initTiles):
            self.insertRandonTile()

        self.displayer.display(self.grid)

        # Player Goes First
        turn = PLAYER_TURN
        maxTile = 0

        self.prevTime = time.clock()

        while not self.isGameOver() and not self.over:
            # Copy to Ensure Cannot Change the Real Grid to Cheat
            gridCopy = self.grid.clone()

            move = None

            if turn == PLAYER_TURN:
                print("Player's Turn:", end="")
                move = self.player.getMove(gridCopy)
                print(actionDic[move])

                # Validate Move
                if move != None and move >= 0 and move < 4:
                    if self.grid.canMove([move]):
                        self.grid.move(move)

                        # Update maxTile
                        maxTile = self.grid.getMaxTile()
                    else:
                        print("Invalid Player Move")
                        self.over = True
                else:
                    print("Invalid Player Move - 1")
                    self.over = True
            else:
                print("Computer's turn:")
                move = self.computer.getMove(gridCopy)

                # Validate Move
                if move and self.grid.canInsert(move):
                    self.grid.setCellValue(move, self.getNewTileValue())
                else:
                    print("Invalid Computer  Move")
                    self.over = True

            if not self.over:
                self.displayer.display(self.grid)

            # Exceeding the Time Allotted for Any Turn Terminates the Game
            self.updateAlarm(time.clock())

            turn = 1 - turn
        print(maxTile)

    def isGameOver(self):
        return not self.grid.canMove()

    def getNewTileValue(self):
        if randint(0, 99) < 100 * self.probability:
            return self.possibleNewTiles[0]
        else:
            return self.possibleNewTiles[1]

    def insertRandonTile(self):
        tileValue = self.getNewTileValue()
        cells = self.grid.getAvailableCells()
        cell = cells[randint(0, len(cells) - 1)]
        self.grid.setCellValue(cell, tileValue)


def main():
    gameManager = GameManager()
    player = Player()
    computer = Computer()
    displayer = Displayer()

    gameManager.setDisplayer(displayer)
    gameManager.setPlayer(player)
    gameManager.setComputer(computer)

    gameManager.start()


if __name__ == '__main__':
    main()
