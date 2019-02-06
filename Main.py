import State from State
import Line from Line
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
        self.hlines = [] *self.ydim+1
        self.vlines = [] *self.xdim+1

        #build horizontal lines
        for i in range(xdim):
            for j in range(ydim+1):

        #build vertical lines
        for i in range(ydim):
            for j in range(xdim+1):


    def solve(self):
        #Do all the solving here
