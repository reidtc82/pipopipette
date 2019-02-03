# Has a boarder that holds references to the lines, but those are accessed directly for setting.
class Box:
    def __init__(self, value, boarder):
            self.owner = None
            self.boarder = boarder
            self.value = value

    def get_owner(self):
        return self.owner

    def get_boarder(self):
        return self.boarder

    def get_value(self):
        return self.value

    def set_owner(self, owner):
        self.owner = owner
