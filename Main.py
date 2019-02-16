import numpy as np
from State import State
from Line import Line
from Box import Box
from Boarder import Boarder
from Manager import Manager
from random import randint
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
    def __init__(self, xdim, ydim, plies, usePruning):
        self.xdim = xdim
        self.ydim = ydim
        self.plies = plies
        self.field = []
        #raw state with no moves
        for i in range(xdim):
            self.field.append([])
            for j in range(ydim):
                self.field[i].append(Box(randint(1,9)))

        self.currentState = State(self.field)
        self.pruning = usePruning

    def get_current_state(self):
        return self.currentState

    def calc_next_move(self, state):
        line = None
        return line

    def get_hlines(self):
        return self.hlines

    def get_vlines(self):
        return self.vlines
