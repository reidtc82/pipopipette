from Line import Line
from Box import Box
from random import randint
# Siply meant to track the progress of the game. I can acces the lines individually.
class State:
    def __init__(self, xdim, ydim, lines, boxes):
        # Field is just an array of dots.
        # self.field = field
        self.scoreState = {'human' : 0, 'computer' : 0}
        self.lines = lines
        self.boxes = boxes

        #move out of here
        for i in range(xdim+(xdim-1)):
            self.lines.append([])
            for j in range(ydim+(ydim-1)):
                if (j == 0 or j%2 == 0) and (i != 0 and i%2 != 0):
                    self.lines[i][j] = Line()
                elif (j != 0 and j%2 != 0) and (i == 0 or i%2 == 0):
                    self.lines[i][j] = Line()
                else:
                    self.lines[i][j] = None

        #move out of here
        for i in range(xdim+(xdim-1)):
            self.boxes.append([])
            for j in range(ydim+(ydim-1)):
                if (j == 0 or j%2 == 0) or (i == 0 or i%2 == 0):
                    self.boxes[i][j] = None
                else:
                    border = {'top':self.lines[i][j-1],
                        'bottom':self.lines[i][j+1],
                        'left': self.lines[i-1][j],
                        'right':self.lines[i+1][j]}
                    self.boxes[i][j] = Box(randint(1,9), border)

    def score_state(self):
        # If this is too slow move to the front end when line gets selected.
        for box in self.boxes:
            if box:
                if box.get_owner() == Player.HUMAN:
                    self.scoreState['human'] += box.get_value()
                elif box.get_owner() == Player.COMPUTER:
                    self.scoreState['computer'] += box.get_value()
        return self.scoreState

    def set_boxes(self, boxes):
        self.boxes = boxes

    def get_lines(self):
        return self.lines

    def set_lines(sef, lines):
        self.lines = lines

    def check_complete(self):
        complete = True
        for box in self.boxes:
            if box:
                if not box.get_owner():
                    complete = False
                    break
        return complete
