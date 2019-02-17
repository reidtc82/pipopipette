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
    def __init__(self, xdim, ydim, plies):
        self.xdim = xdim
        self.ydim = ydim
        self.plies = plies
        # self.pruning = usePruning
        self.currentState = State(xdim, ydim)
        self.infinity = float('inf')

    def play(self, currentPlayer):
        if not self.currentState.check_complete():
            if currentPlayer == Player.HUMAN:
                self.print_board(state)
                self.take_move()
                # get human input and set state lines accordingly
                currentPlayer = Player.COMPUTER
            elif currentPlayer == Player.COMPUTER:
                # get computer input
                passState = deepcopy(self.currentState)

                self.currentState = self.min_max_ab(passState, True, 1)

                currentPlayer = Player.HUMAN
        elif:
            #return the scoring object
            return state.score_state()

    def min_max_ab(self, state, maximize, depth):
        if depth == self.plies:
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
                        for b in tempChild.get_boxes():
                            if b:
                                if b.is_closed() and not b.get_owner():
                                    b.set_owner(Player.COMPUTER)
                                    break
                        children.append(tempChild)
        return children
