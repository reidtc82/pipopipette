import sys
from Main import Pipopipette
from Player import Player

xdim = int(raw_input('Enter x dimension: '))
ydim = int(raw_input('Enter y dimension: '))
plies = int(raw_input('Enter number of plies: '))
game = Pipopipette(xdim,ydim,plies)
game.play(Player.HUMAN)
