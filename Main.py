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
        tempy = self.ydim+1
        tempx = self.xdim+1
        self.hlines = []
        self.vlines = []
        self.manager = Manager()
        #build horizontal lines
        self.hlines = [[Line() for j in range(ydim+1)] for i in range(xdim)]
        # for i in range(xdim):
        #     for j in range(ydim+1):
        #         self.hlines[i][j] = Line()

        #build vertical lines
        self.vlines = [[Line() for j in range(ydim)] for i in range(xdim)]
        # for i in range(ydim):
        #     for j in range(xdim+1):
        #         self.vlines[i][j] = Line()

        field = np.empty((xdim+1,ydim+1))
        for i in range(xdim+1):
            for j in range(ydim+1):
                #draw out this array
                #top,right,bottom,left
                if i < xdim and j < ydim:
                    boarder = Boarder(self.hlines[i][j], self.vlines[i+1][j], self.hlines[i+1][j], self.vlines[i][j])
                elif i < xdim and j == ydim:
                    if i == 0:
                        boarder = Boarder(self.hlines[i][j-1], self.vlines[i][j], self.hlines[i+1][j-1], self.vlines[i][j])
                    if i > 0:
                        boarder = Boarder(self.hlines[i][j-1], self.vlines[i][j], self.hlines[i+1][j-1], self.vlines[i-1][j])
                elif j < ydim and i == xdim:
                    if j == 0:
                        boarder = Boarder(self.hlines[i-1][j], self.vlines[i][j], self.hlines[i][j], self.vlines[i][j])
                    elif j > 0:
                        boarder = Boarder(self.hlines[i-1][j], self.vlines[i][j-1], self.hlines[i][j], self.vlines[i][j-1])
                elif i == xdim and j == ydim:
                    boarder = Boarder(self.hlines[i-1][j-1], self.vlines[i][j-1], self.hlines[i][j-1], self.vlines[i-1][j-1])

                rand = randint(0,9)
                try:
                    field[i][j] = Box(rand, boarder)
                except:
                    print(sys.exc_info()[0])

        #raw state with no moves
        self.currentState = State(field)
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

    # def play(self, whoIsFirst, usePruning):
    #     #Do all the solving here
    #     currentState = self.seedState
    #     currentPlayer = whoIsFirst
    #     while currentState.has_open():
    #         #keep playing
    #         if currentPlayer == Player.HUMAN:
    #
    #             # self.manager.unlock_input()
    #             # #wait for input
    #             # io = None
    #             # while not io:
    #             #     io = self.manager.check_io()
    #             #
    #             # #process the input
    #             # for l in self.hlines:
    #             #     if l = io['selected']:
    #             #         l.set()
    #             #
    #             # for i in self.vlines:
    #             #     if l = io['selected']:
    #             #         l.set()
    #
    #             #switch player
    #             currentPlayer = Player.COMPUTER
    #
    #         elif currentPlayer == Player.COMPUTER:
    #             self.manager.lock_input()
    #             #do algoirthm
    #             #switch player
    #             currentPlayer = Player.HUMAN


        #board is closed return scores
        print('Game Over! '+currentState.score_state())
