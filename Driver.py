import sys
from Main import Pipopipette
from Player import Player

class Game:
    def __init__(self, master):
        self.game = Pipopipette(self.xdim, self.ydim, self.plies, False)

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
