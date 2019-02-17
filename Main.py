import numpy as np
from State import State
from Player import Player
from copy import deepcopy
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
    def __init__(self, xdim, ydim, plies):
        self.xdim = xdim
        self.ydim = ydim
        self.plies = plies
        # self.pruning = usePruning
        self.currentState = State(xdim, ydim, [], [])
        self.infinity = float('inf')

    def play(self, currentPlayer):
        while not self.currentState.check_complete():
            if currentPlayer == Player.HUMAN:
                self.print_board(self.currentState)
                print('Your score is {0}'.format(self.currentState.score_state()['human']))
                print('Computer score is {0}'.format(self.currentState.score_state()['computer']))
                self.take_move()
                # get human input and set state lines accordingly
                currentPlayer = Player.COMPUTER
            elif currentPlayer == Player.COMPUTER:
                # get computer input
                passState = deepcopy(self.currentState)
                # print('current Stte 1: '+str(self.currentState))
                self.currentState = self.min_max_ab(passState, True, 1)
                # print('current Stte 2: '+str(self.currentState))
                currentPlayer = Player.HUMAN

        #return the scoring object
        return self.currentState.score_state()

    def min_max_ab(self, state, maximize, depth):
        if depth == self.plies:
            # print('End of plies')
            return state
        else:
            if state.check_complete():
                return state
            else:
                if maximize:
                    best = -self.infinity
                    favoriteChild = None
                    for child in self.make_babies(state):
                        newState = self.min_max_ab(child, False, depth+1)
                        if newState.score_state()['computer'] >= best:
                            best = newState.score_state()['computer']
                            favoriteChild = child
                    return favoriteChild
                else:
                    best = self.infinity
                    favoriteChild = None
                    for child in self.make_babies(state):
                        newState = self.min_max_ab(child, True, depth+1)
                        if newState.score_state()['human'] < best:
                            best = newState.score_state()['human']
                            favoriteChild = child
                    return favoriteChild

    def make_babies(self, parent):
        children = []
        # tempLines = deepcopy(parent.get_lines())
        for i in range(self.xdim+(self.xdim-1)):
            for j in range(self.ydim+(self.ydim-1)):
                if parent.get_lines()[i][j]:
                    if not parent.get_lines()[i][j].is_set():
                        tempChild = deepcopy(parent)
                        tempChild.get_lines()[i][j].set()
                        for row in tempChild.get_boxes():
                            for b in row:
                                if b:
                                    if b.is_closed() and not b.get_owner():
                                        b.set_owner(Player.COMPUTER)
                                        break
                        children.append(tempChild)
        return children

    def take_move(self):
        io = input('Enter move: ')

    def print_board(self, state):
        for j in range(self.ydim+(self.ydim-1)):
            line = ''
            for i in range(self.xdim+(self.xdim-1)):
                if (j != 0 and j%2 != 0) and (i != 0 and i%2 != 0):
                    line = line+' B'+str(state.get_boxes()[i][j].get_value())
                if (j == 0 or j%2 == 0) and (i == 0 or i%2 == 0):
                    line = line+' *'
                if (j != 0 and j%2 != 0) and (i == 0 or i%2 == 0):
                    if state.get_lines()[i][j].is_set():
                        line = line+' |'
                    else:
                        line = line+'  '
                if (j == 0 or j%2 == 0) and (i != 0 and i%2 != 0):
                    if state.get_lines()[i][j].is_set():
                        line = line+' __'
                    else:
                        line = line+'   '
            print(line)
