# Siply meant to track the progress of the game. I can acces the lines individually.
class State:
    def __init__(self, field):
        # Field is just an array of boxes.
        self.field = field
        self.scoreState = {'p1' : 0, 'p2' : 0}

    def score_state(self):
        # If this is too slow move to the front end when line gets selected.
        for box in field:
            if box.get_owner() == Player.ONE:
                self.scoreState['p1'] += box.get_value()
            elif box.get_owner() == Player.TWO:
                self.scoreState['p2'] += box.get_value()
        return self.scoreState

    def get_field(self):
        return self.field

    def check_complete(self):
        complete = True
        for box in field:
            if not box.get_owner():
                complete = False
        return complete
