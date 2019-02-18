import numpy as np
from State import State
from Player import Player
from copy import deepcopy
import sys
import time

# Main class of the game
class Pipopipette:
    #xdim and ydim in number of DOTS!
    def __init__(self, xdim, ydim, plies, useAB):
        self.xdim = xdim
        self.ydim = ydim
        self.IMPATIENCEFACTOR = 2 # something to keep the wait times reasonable at the beginning of the game.
        self.plies = plies*2
        self.currentState = State(xdim, ydim, [], [])
        self.infinity = float('inf')
        self.moveCount = 1
        if useAB == 'Y':
            self.useAB = True
        else:
            self.useAB = False
        self.recordedTime = []

    # Method to be called to play the game after it is constructed.
    def play(self, currentPlayer):
        # Managing game state with a loop
        while not self.currentState.check_complete():
            # The algorithm doesnt select for the human player so this manages who is playing.
            if currentPlayer == Player.HUMAN:
                # Print board and scores for human to make a decision.
                self.print_board(self.currentState)
                print('Your score is {0}'.format(self.currentState.score_state()['human']))
                print('Computer score is {0}'.format(self.currentState.score_state()['computer']))
                # Call utility method to take the humans move. This will update the current state.
                self.take_move(self.currentState)
                # Swap players for next iteration.
                currentPlayer = Player.COMPUTER
            elif currentPlayer == Player.COMPUTER:
                # Now its the computers turn.
                # Start a timer for stats.
                start = time.time()
                # Get a copy of the current state so we dont mess it up while recursing.
                # Probably being overly cautious.
                passState = deepcopy(self.currentState)
                # Start the algorithm and assign teh results to the current state.
                self.currentState = self.min_max_ab(passState, True, 1, -self.infinity, self.infinity)
                # Swap players
                currentPlayer = Player.HUMAN
                # Manage time stats
                end = time.time()
                print('Elapsed time this computer move {0}'.format(end-start))
                self.recordedTime.append(end-start)

        # If the game drops out of the loop it ended gracefully.
        # Print the final board state.
        self.print_board(self.currentState)
        # Print the final scores.
        print('Your score is {0}'.format(self.currentState.score_state()['human']))
        print('Computer score is {0}'.format(self.currentState.score_state()['computer']))
        # Print a stat for the computer move time.
        print('Average computer move time is {0}'.format(self.avg_move_time()))
        sys.exit(0)

    # Minmax algorithm with options to use pruning.
    def min_max_ab(self, state, maximize, depth, alpha, beta):
        # I added the IMPATIENCEFACTOR to speed up early moves or games
        # with deep plies and a large board. The first few moves dont need much
        # strategy and I find that if the computer is first it will select the same
        # line (the last one in the array) every start. If I was worried about
        # "FUNFACTOR" Id would drop a flag in and have it just select at random
        # if the computer was first, for its first move.
        if depth == self.IMPATIENCEFACTOR or depth == self.plies:
            # If the algorithm recurses deep enough it will get to one of these limits and return.
            return state
        else:
            # Check for completion - See State class.
            if state.check_complete():
                # If so, return.
                return state
            else:
                # If max player being assessed - In this case, I figured the computer
                # would always be the max player as it is coming up with moves only
                # for itself.
                if maximize: # alpha player
                    # Set some variables up.
                    best = -self.infinity
                    favoriteChild = None

                    # Make children of the state passed.
                    for child in self.make_babies(state):
                        # Recurse and assign the result to a temporary state.
                        newState = self.min_max_ab(child, False, depth+1, alpha, beta)
                        if newState: # I was having issues with it passing null states out...
                            # My understanding of the assignment is that the score to measure
                            # the fitness of a node by is the difference beteween computer and human
                            # scores. reversing this would presumably make the computer let the human win.
                            childScore = newState.score_state()['computer']-newState.score_state()['human']
                            # Determine new alpha
                            alpha = max(alpha, childScore)
                            # Can turn off pruning
                            if self.useAB:
                                if alpha >= beta:
                                    # If alpha is greater than beta then stop checking children.
                                    break
                            # Set up our best result to return
                            if childScore >= best:
                                best = childScore
                                favoriteChild = child
                    # Return back up the tree.
                    return favoriteChild
                else: # beta player
                # Now assessing for min player.
                    best = self.infinity
                    favoriteChild = None
                    # Basically does the same as maximize but assigning min for beta.
                    for child in self.make_babies(state):
                        newState = self.min_max_ab(child, True, depth+1, alpha, beta)
                        if newState:
                            childScore = newState.score_state()['computer']-newState.score_state()['human']
                            beta = min(beta, childScore)
                            if self.useAB:
                                if alpha >= beta:
                                    # Stop assessing new children.
                                    break
                            # Set up for least return.
                            if childScore < best:
                                best = childScore
                                favoriteChild = child
                    # Return for it to percolate.
                    return favoriteChild

    # Successor function
    def make_babies(self, parent):
        children = []
        # Im probably handling these collections poorly but it seems to work.
        # Lots of loops...
        for i in range(self.xdim+(self.xdim-1)):
            for j in range(self.ydim+(self.ydim-1)):
                if parent.get_lines()[i][j]:
                    if not parent.get_lines()[i][j].is_set():
                        # This goes through each line in the parent. If it finds one
                        # that isnt set then it makes a copy of the parent and sets that line
                        tempChild = deepcopy(parent)
                        tempChild.get_lines()[i][j].set()
                        # After setting a line as claimed it has to assign the owner so it
                        # can be scored for fitness.
                        for row in tempChild.get_boxes():
                            for b in row:
                                if b:
                                    if b.is_closed() and not b.get_owner():
                                        b.set_owner(Player.COMPUTER)
                        # Add this new child to the list and work on the next.
                        children.append(tempChild)
        # Return the children.
        return children

    # Utility to take the human players move.
    def take_move(self, state):
        aValidSelection = False
        lineSelected = None
        # Loop for some basic validation. Its not robust so Im sure it can be
        # thrown off.
        while not aValidSelection:
            lineSelected = raw_input('Enter line ID (exit to exit): ')
            if lineSelected == 'exit':
                # If you get bored. Still have to wait for the computer to finish its move though.
                sys.exit(0)

            # Basically walk through all the lines until the one selected by the human player
            # is found. Humans must enter in form 'L#' as labelled on the output.
            for row in state.get_lines():
                for l in row:
                    if l:
                        # print(l.get_id())
                        if l.get_id() == lineSelected and not l.is_set():
                            l.set()
                            lineSelected = None
                            # Once selected successfully then check for closed and assign ownership.
                            for brow in state.get_boxes():
                                for b in brow:
                                    if b:
                                        if b.is_closed() and not b.get_owner():
                                            b.set_owner(Player.HUMAN)

                            aValidSelection = True
                            # House keeping for impatient people
                            self.moveCount+=1
                            if self.moveCount%3 == 0:
                                self.IMPATIENCEFACTOR+=1
                        elif l.get_id() == lineSelected and l.is_set():
                            print('That line is already selected. Try again.')
            if not aValidSelection:
                print('No line by that ID. Try again.')

    # Utility function to print the board.
    def print_board(self, state):
        # Just loops through and drops characters representing the board pieces.
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

    # Utility for stats.
    def avg_move_time(self):
        count = 0
        total = 0
        for et in self.recordedTime:
            count+=1
            total+=et
        return total/count
