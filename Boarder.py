# Just holds the lines for the boxes for state checking and management.
class Boarder:
    def __init__(self, top, right, bottom, left):
        self.lines = {'top': top, 'right': right, 'bottom': bottom, 'left': left}

    # Im not sure that Im still using this.
    def is_closed(self):
        closed = True
        for l in self.lines:
            if not l.is_set():
                closed = False
        return closed

    # Or this...
    def set_line(self, index):
        self.lines[index].set()
