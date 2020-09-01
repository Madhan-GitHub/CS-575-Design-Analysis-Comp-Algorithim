# AIM: PLAYER GETS THE NEXT MOVE FOR THE PLAYER


from Base import Base
from Helper import *
from Minmaxab import *
from Grid import *
import numpy as np


class Player(Base):
    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        maxUtility = -np.inf
        nextDir = -1

        for move in moves:
            child = getChild(grid, move)

            utility = Decision(grid=child, max=False)

            if utility >= maxUtility:
                maxUtility = utility
                nextDir = move

        return nextDir
