import numpy as np
from State import State
import sys

# Prompt for playing field dimension.
# Prompt for plies.
# I need two arrays of lines; lines vertical and horizontal.
# Need to construct an array of boxes to pass to State.

# Init order:
# 1. Create two line arrays and populate with new lines.
# 2. Create array of boxes passing a boarder of lines to each - lines will be reused.
# 3. Create starting state passing it the array of boxes as the "field."

class Pipopipette:
    #xdim and ydim in number of DOTS!
    def __init__(self, xdim, ydim, plies, usePruning):
        self.xdim = xdim
        self.ydim = ydim
        self.plies = plies
        self.pruning = usePruning
        self.currentState = State(xdim, ydim)

    def play(self, state, currentPlayer):
        if not state.check_complete():
            if currentPlayer == Player.HUMAN:
                # get human input and set state lines accordingly
                currentPlayer = Player.COMPUTER
            elif currentPlayer == Player.COMPUTER:
                # get computer input
                currentPlayer = Player.HUMAN
        elif:
            return state.score_state()

    def calc_next_move(self, state):
        line = None
        return line
