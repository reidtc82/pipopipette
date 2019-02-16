from Line import Line
# Has a boarder that holds references to the lines, but those are accessed directly for setting.
class Box:
    def __init__(self, value, border):
            self.owner = None
            self.value = value
            # Top, Bottom, Left, Right
            self.border = border

    def get_owner(self):
        return self.owner

    def get_border(self):
        return self.border

    def get_value(self):
        return self.value

    def set_owner(self, owner):
        self.owner = owner
