from State import State
from Line import Line
from Box import Box
from Boarder import Boarder
from Manager import Manager
from random import randint

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
        self.hlines = [0] *self.ydim+1
        self.vlines = [0] *self.xdim+1
        self.manager = Manager()
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
