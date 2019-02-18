import sys
from Main import Pipopipette
from Player import Player

# Just the code to get the game started. Prompt for starting criteria, instantiate the
# game class, and set it off to play based on selected first player.

# Value passed in for xdim and ydim are the number of dots, not the number of boxes/lines.
if sys.version_info[0] == 3:
    # for Python3
    xdim = int(input('Enter x dimension: '))
    ydim = int(input('Enter y dimension: '))
    plies = int(input('Enter number of plies: '))
    useAB = input('Use Alpha Beta Pruning? (Y or N) ')
    whoFirst = input('Do you want to move first? (Y or N) ')
else:
    # for Python2
    xdim = int(raw_input('Enter x dimension: '))
    ydim = int(raw_input('Enter y dimension: '))
    plies = int(raw_input('Enter number of plies: '))
    useAB = raw_input('Use Alpha Beta Pruning? (Y or N) ')
    whoFirst = raw_input('Do you want to move first? (Y or N) ')

game = Pipopipette(xdim, ydim, plies, useAB)
if whoFirst == 'Y':
    game.play(Player.HUMAN)
else:
    game.play(Player.COMPUTER)
