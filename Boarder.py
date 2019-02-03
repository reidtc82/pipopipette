# Just holds the lines for the boxes for state checking and management.
class Boarder:
    def __init__(self, lines):
        self.lines = lines

    def is_closed(self):
        closed = True
        for l in self.lines:
            if not l.is_set():
                closed = False
        return closed

    def set_line(self, index):
        self.lines[index].set()
