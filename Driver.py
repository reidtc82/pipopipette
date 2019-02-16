import sys
if sys.version_info[0] == 3:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
else:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter

from Main import Pipopipette
from Player import Player

class Game:
    def __init__(self, master):
        self.io = None

        self.currentPlayer = Player.COMPUTER

        self.xdim = 6
        self.ydim = 20

        self.boxsize = 400/self.ydim

        self.canvas_width = self.xdim*self.boxsize
        self.canvas_height = self.ydim*self.boxsize
        self.plies = 2
        self.rectangles = [0] *8
        self.texts = [0] *8

        self.game = Pipopipette(self.xdim, self.ydim, self.plies, False)

        # setting up the tkinter GUI
        self.master = master
        self.master.title("Pipopipette")
        self.master.geometry('640x480')

        self.label = Label(master, text="Pipopipette")
        self.label.pack()

        # score = Label(master, text=self.board.getScore())
        # score.pack()

        self.canvasSpace = Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.canvasSpace.pack()

        self.canvasSpace.create_rectangle(0, 0, self.canvas_width, self.canvas_height, fill="#696969")
        self.draw_board(self.canvasSpace)

        # self.resetPuzzle_button = Button(master, text="Reset Puzzle", command=self.newPuzzle)
        # self.resetPuzzle_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        # self.up_button = Button(master, text="Up", command=self.moveUp)
        # self.up_button.pack()

        # self.down_button = Button(master, text="Down", command=self.moveDown)
        # self.down_button.pack()

        # self.left_button = Button(master, text="Left", command=self.moveLeft)
        # self.left_button.pack()

        # self.right_button = Button(master, text="Right", command=self.moveRight)
        # self.right_button.pack()

    def play(self):
        while not self.game.get_current_state().check_complete():
            if currentPlayer == Player.HUMAN:
                unlock_input()
                while not io:
                    pass
                update_board(io)
                io = None
                currentPlayer = Player.COMPUTER
            elif currentPlayer == Player.COMPUTER:
                lock_input()
                io = self.game.calc_next_move()
                update_board(io)
                io = None
                currentPlayer = Player.HUMAN

        #If it got this far its done
        print(self.game.get_current_state().score_state())

    def update_board(selected):
        for l in self.game.get_hlines():
            if l == selected:
                l.set()
        for l in self.game.get_vlines():
            if l == selected:
                l.set()

    def draw_board(self, canvas):
        for rec in self.rectangles:
            canvas.delete(rec)

        for txt in self.texts:
            canvas.delete(txt)

        currentState = self.game.get_current_state().get_field()
        for i in range(self.xdim):
            for j in range(self.ydim):
                if currentState[i][j] != 0:
                    origin_X = self.boxsize*i
                    origin_Y = self.boxsize*j
                    final_X = origin_X+self.boxsize
                    final_Y = origin_Y+self.boxsize
                    if currentState[i][j].get_owner() == Player.HUMAN:
                        fillcolor = "#1E559E"
                    elif currentState[i][j].get_owner() == Player.COMPUTER:
                        fillcolor = "#DD0000"
                    else:
                        fillcolor = "#DCDCDC"
                    self.rectangles.append(canvas.create_rectangle(origin_X, origin_Y, final_X, final_Y, fill=fillcolor))
                    self.texts.append(canvas.create_text(origin_X+(self.boxsize/2),origin_Y+(self.boxsize/2),text=currentState[i][j].get_value()))


root = Tk()
mainPanel = Game(root)
root.mainloop()
