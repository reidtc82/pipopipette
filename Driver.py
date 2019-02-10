import sys
if sys.version_info[0] == 3:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
else:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter

from Main import Pipopipette
from Player import Player 

io = None

currentPlayer = Player.COMPUTER
game = Pipopipette(2, 2, 2, False)

canvas_width = 300
canvas_height = 300
rectangles = [0] *8
texts = [0] *8

board = PuzzleBoard()

# setting up the tkinter GUI
master = master
master.title("8 Puzzle")
master.geometry('640x480')

label = Label(master, text="This is 8 Puzzle")
label.pack()

score = Label(master, text=self.board.getScore())
score.pack()

canvasSpace = Canvas(master, width=self.canvas_width, height=self.canvas_height)
canvasSpace.pack()

canvasSpace.create_rectangle(0, 0, 300, 300, fill="#696969")
drawBoard(self.canvasSpace)

resetPuzzle_button = Button(master, text="Reset Puzzle", command=self.newPuzzle)
resetPuzzle_button.pack()

close_button = Button(master, text="Close", command=master.quit)
close_button.pack()

up_button = Button(master, text="Up", command=self.moveUp)
up_button.pack()

down_button = Button(master, text="Down", command=self.moveDown)
down_button.pack()

left_button = Button(master, text="Left", command=self.moveLeft)
left_button.pack()

right_button = Button(master, text="Right", command=self.moveRight)
right_button.pack()

while not game.get_current_state().check_complete():
    if currentPLayer == Player.HUMAN:
        unlock_input()
        while not io:
            pass
        update_board(io)
        io = None
        currentPlayer = Player.COMPUTER
    elif currentPlayer == Player.COMPUTER:
        lock_input()
        io = game.calc_next_move()
        update_board(io)
        io = None
        currentPlayer = Player.HUMAN

#If it got this far its done
print(game.get_current_state().score_state())

def update_board(selected):
    for l in game.get_hlines():
        if l == selected:
            l.set()
    for l in game.get_vlines():
        if l == selected:
            l.set()
