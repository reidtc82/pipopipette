from Line import Line
# Has a boarder that holds references to the lines, but those are accessed directly for setting.
class Box:
    def __init__(self, value, border):
            self.owner = None
            self.value = value
            # Top, Bottom, Left, Right
            self.border = border
            # print(self.border)

    def get_owner(self):
        return self.owner

    def get_border(self):
        return self.border

    def get_value(self):
        return self.value

    def set_owner(self, owner):
        self.owner = owner

    def is_closed(self):
        closed = True
        if (not self.border['top'].is_set()) or (not self.border['bottom'].is_set()) or (not self.border['left'].is_set()) or (not self.border['right'].is_set()):
            closed = False
        # for l in self.border:
        #     print(l)
        #     if not l.is_set():
        #         closed = False
        #         break
        return closed
