import sys
from Main import Pipopipette
from Player import Player

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
