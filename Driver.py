import sys
if sys.version_info[0] == 3:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
else:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter

import Pipopipette from Main
import Player from Player

io = None

currentPlayer = Player.COMPUTER
game = Pipopipette(2, 2, 2, False)

self.canvas_width = 300
self.canvas_height = 300
self.rectangles = [0] *8
self.texts = [0] *8

self.board = PuzzleBoard()

# setting up the tkinter GUI
self.master = master
master.title("8 Puzzle")
master.geometry('640x480')

self.label = Label(master, text="This is 8 Puzzle")
self.label.pack()

self.score = Label(master, text=self.board.getScore())
self.score.pack()

self.canvasSpace = Canvas(master, width=self.canvas_width, height=self.canvas_height)
self.canvasSpace.pack()

self.canvasSpace.create_rectangle(0, 0, 300, 300, fill="#696969")
self.drawBoard(self.canvasSpace)

self.resetPuzzle_button = Button(master, text="Reset Puzzle", command=self.newPuzzle)
self.resetPuzzle_button.pack()

self.close_button = Button(master, text="Close", command=master.quit)
self.close_button.pack()

self.up_button = Button(master, text="Up", command=self.moveUp)
self.up_button.pack()

self.down_button = Button(master, text="Down", command=self.moveDown)
self.down_button.pack()

self.left_button = Button(master, text="Left", command=self.moveLeft)
self.left_button.pack()

self.right_button = Button(master, text="Right", command=self.moveRight)
self.right_button.pack()

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
