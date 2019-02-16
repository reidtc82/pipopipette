from Line import Line
from Box import Box
from random import randint
# Siply meant to track the progress of the game. I can acces the lines individually.
class State:
    def __init__(self, xdim, ydim):
        # Field is just an array of boxes.
        self.field = field
        self.scoreState = {'human' : 0, 'computer' : 0}
        self.pieces = []

        for i in range(xdim+(xdim-1)):
            self.pieces.append([])
            for j in range(ydim+(ydim-1)):
                if ((j != 0) and (j%2 != 0)) and ((i == 0) or (i%2 == 0)):
                    self.pieces[i][j] = Line()
                elif ((j == 0) or (j%2 == 0)) and ((i != 0) and (i%2 != 0)):
                    self.pieces[i][j] = Line()

        for i in range(xdim+(xdim-1)):
            for j in range(ydim+(ydim-1)):
                if ((j != 0) and (j%2 != 0)) and ((i != 0) and (i%2 != 0)):
                    border = {'top':self.pieces[i][j-1],
                              'bottom':self.pieces[i][j+1],
                              'left': self.pieces[i-1][j],
                              'right':self.pieces[i+1][j]}
                    self.pieces[i][j] = Box(randint(1,9), border)

    def score_state(self):
        # If this is too slow move to the front end when line gets selected.
        for box in field:
            if box.get_owner() == Player.HUMAN:
                self.scoreState['human'] += box.get_value()
            elif box.get_owner() == Player.COMPUTER:
                self.scoreState['computer'] += box.get_value()
        return self.scoreState

    def get_state(self):
        return self.pieces

    def check_complete(self):
        complete = True
        for box in field:
            if not box.get_owner():
                complete = False
        return complete
