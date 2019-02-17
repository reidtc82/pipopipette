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
        self.IMPATIENCEFACTOR = 1 # something to keep the wait times reasonable at the beginning of the game.
        self.plies = plies*2
        # self.pruning = usePruning
        self.currentState = State(xdim, ydim, [], [])
        self.infinity = float('inf')
        self.moveCount = 1

    def play(self, currentPlayer):
        while not self.currentState.check_complete():
            if currentPlayer == Player.HUMAN:
                self.print_board(self.currentState)
                print('Your score is {0}'.format(self.currentState.score_state()['human']))
                print('Computer score is {0}'.format(self.currentState.score_state()['computer']))
                self.take_move(self.currentState)
                # get human input and set state lines accordingly
                currentPlayer = Player.COMPUTER
            elif currentPlayer == Player.COMPUTER:
                # get computer input
                passState = deepcopy(self.currentState)
                # print('current Stte 1: '+str(self.currentState))
                self.currentState = self.min_max_ab(passState, True, 1, -self.infinity, self.infinity)
                # print('current Stte 2: '+str(self.currentState))
                currentPlayer = Player.HUMAN

        #return the scoring object
        self.print_board(self.currentState)
        print('Your score is {0}'.format(self.currentState.score_state()['human']))
        print('Computer score is {0}'.format(self.currentState.score_state()['computer']))
        sys.exit(0)

    def min_max_ab(self, state, maximize, depth, alpha, beta):
        if depth == self.IMPATIENCEFACTOR or depth == self.plies:
            return state
        else:
            if state.check_complete():
                return state
            else:
                if maximize:#alpha player
                    best = -self.infinity
                    favoriteChild = None
                    for child in self.make_babies(state):
                        newState = self.min_max_ab(child, False, depth+1, alpha, beta)
                        if newState:
                            childScore = newState.score_state()['computer']-newState.score_state()['human']
                            alpha = max(alpha, childScore)
                            if alpha >= beta:
                                break
                            if childScore>= best:
                                best = childScore
                                favoriteChild = child
                    return favoriteChild
                else:#beta player
                    best = self.infinity
                    favoriteChild = None
                    for child in self.make_babies(state):
                        newState = self.min_max_ab(child, True, depth+1, alpha, beta)
                        if newState:
                            childScore = newState.score_state()['computer']-newState.score_state()['human']
                            beta = min(beta, childScore)
                            if alpha >= beta:
                                break
                            if childScore < best:
                                best = childScore
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

                        children.append(tempChild)
        return children

    def take_move(self, state):
        aValidSelection = False
        lineSelected = None
        while not aValidSelection:
            lineSelected = raw_input('Enter line ID (exit to exit): ')
            if lineSelected == 'exit':
                sys.exit(0)
            for row in state.get_lines():
                for l in row:
                    if l:
                        # print(l.get_id())
                        if l.get_id() == lineSelected and not l.is_set():
                            l.set()
                            lineSelected = None
                            for brow in state.get_boxes():
                                for b in brow:
                                    if b:
                                        if b.is_closed() and not b.get_owner():
                                            b.set_owner(Player.HUMAN)

                            aValidSelection = True
                            self.moveCount+=1
                            if self.moveCount%2 == 0:
                                self.IMPATIENCEFACTOR+=1
                        elif l.get_id() == lineSelected and l.is_set():
                            print('That line is already selected. Try again.')
            if not aValidSelection:
                print('No line by that ID. Try again.')

    def print_board(self, state):
        for j in range(self.ydim+(self.ydim-1)):
            line = ''
            for i in range(self.xdim+(self.xdim-1)):
                if (j != 0 and j%2 != 0) and (i != 0 and i%2 != 0):
                    line = line+' B'+str(state.get_boxes()[i][j].get_value())
                if (j == 0 or j%2 == 0) and (i == 0 or i%2 == 0):
                    line = line+'  *'
                if (j != 0 and j%2 != 0) and (i == 0 or i%2 == 0):
                    if state.get_lines()[i][j].is_set():
                        line = line+'  |'
                    else:
                        line = line+' '+state.get_lines()[i][j].get_id()
                if (j == 0 or j%2 == 0) and (i != 0 and i%2 != 0):
                    if state.get_lines()[i][j].is_set():
                        line = line+' __'
                    else:
                        line = line+' '+state.get_lines()[i][j].get_id()
            print(line)
