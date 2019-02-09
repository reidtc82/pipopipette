import State from State
import Line from Line
import Box from Box
import Boarder from Boarder
from random import randint
# Prompt for playing field dimension.
# Prompt for plies.
# I need two arrays of lines; lines vertical and horizontal.
# Need to construct an array of boxes to pass to State.

# Init order:
# 1. Create two line arrays and populate with new lines.
# 2. Create array of boxes passing a boarder of lines to each - lines will be reused.
# 3. Create starting state passing it the array of boxes as the "field."

class Main:
    def __init__(self, xdim, ydim, plies):
        self.xdim = xdim
        self.ydim = ydim
        self.plies = plies
        self.hlines = [0] *self.ydim+1
        self.vlines = [0] *self.xdim+1

        #build horizontal lines
        for i in range(xdim):
            for j in range(ydim+1):
                self.hlines[i][j] = Line()

        #build vertical lines
        for i in range(ydim):
            for j in range(xdim+1):
                self.vlines[i][j] = Line()

        field = []
        for i in range(xdim-1):
            for j in range(ydim-1):
                #draw out this array
                boarder = Boarder(self.hlines[][], self.vlines[][], self.hlines[][], self.vlines[][])
                field[i][j] = Box(randint(0,9), boarder)
        #raw state with no moves
        self.seedState = State(field)

    def play(self, whoIsFirst, usePruning):
        #Do all the solving here
        currentState = self.seedState
        currentPlayer = whoIsFirst
        while currentState.has_open():
            #keep playing
            if currentPlayer == Player.HUMAN:
                #wait for input

            elif currentPlayer == Player.COMPUTER:
                #do algoirthm
                

        #board is closed return scores
        return currentState.scoreState()
