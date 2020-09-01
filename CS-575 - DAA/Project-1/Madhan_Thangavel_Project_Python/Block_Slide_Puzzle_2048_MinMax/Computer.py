# AIM: TO INHERIT FROM BASE.
# The getMove() function returns a computer action.

from random import randint
from Base import Base


class Computer(Base):
    def getMove(self, grid):
        cells = grid.getAvailableCells()

        return cells[randint(0, len(cells) - 1)] if cells else None
