from Line import Line
from Box import Box
from random import randint
from Player import Player
# Siply meant to track the progress of the game. I can acces the lines individually.
class State:
    def __init__(self, xdim, ydim, lines, boxes):
        # Field is just an array of dots.
        # self.field = field
        self.scoreState = {'human' : 0, 'computer' : 0}
        self.lines = lines
        self.boxes = boxes
        lineCount = 1
        #move out of here
        for i in range(xdim+(xdim-1)):
            self.lines.append([])
            for j in range(ydim+(ydim-1)):
                if (j == 0 or j%2 == 0) and (i != 0 and i%2 != 0):
                    self.lines[i].append(Line('L'+str(lineCount)))
                    lineCount+=1
                elif (j != 0 and j%2 != 0) and (i == 0 or i%2 == 0):
                    self.lines[i].append(Line('L'+str(lineCount)))
                    lineCount+=1
                else:
                    self.lines[i].append(None)

        #move out of here
        for i in range(xdim+(xdim-1)):
            self.boxes.append([])
            for j in range(ydim+(ydim-1)):
                if (j == 0 or j%2 == 0) or (i == 0 or i%2 == 0):
                    self.boxes[i].append(None)
                else:
                    border = {'top':self.lines[i][j-1],
                        'bottom':self.lines[i][j+1],
                        'left': self.lines[i-1][j],
                        'right':self.lines[i+1][j]}
                    self.boxes[i].append(Box(randint(1,9), border))

    def score_state(self):
        # If this is too slow move to the front end when line gets selected.
        tempHumanScore = 0
        tempComputerScore = 0
        for row in self.boxes:
            for box in row:
                if box:
                    if box.get_owner() == Player.HUMAN:
                        tempHumanScore += box.get_value()
                    elif box.get_owner() == Player.COMPUTER:
                        # print('Box value equals {0}'.format(box.get_value()))
                        tempComputerScore += box.get_value()
        self.scoreState['human'] = tempHumanScore
        self.scoreState['computer'] = tempComputerScore
        return self.scoreState

    def get_boxes(self):
        return self.boxes

    def set_boxes(self, boxes):
        self.boxes = boxes

    def get_lines(self):
        return self.lines

    def set_lines(sef, lines):
        self.lines = lines

    def check_complete(self):
        complete = True
        for row in self.boxes:
            for box in row:
                if box:
                    if not box.get_owner():
                        complete = False
                        break
        return complete
