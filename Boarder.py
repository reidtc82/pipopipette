# Just holds the lines for the boxes for state checking and management.
class Boarder:
    def __init__(self, top, right, bottom, left):
        self.lines = {'top': top, 'right': right, 'bottom': bottom, 'left': left}

    def is_closed(self):
        closed = True
        for l in self.lines:
            if not l.is_set():
                closed = False
        return closed

    def set_line(self, index):
        self.lines[index].set()
