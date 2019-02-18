from Line import Line

# Box class is boring like a box. Boxes can share border lines!
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

    def is_closed(self):
        # Just checks each line in the border to see if its closed. Boxes can share border lines!
        closed = True
        if (not self.border['top'].is_set()) or (not self.border['bottom'].is_set()) or (not self.border['left'].is_set()) or (not self.border['right'].is_set()):
            closed = False

        return closed
