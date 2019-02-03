# Access these directly when setting.
class Line:
    def __init__(self):
        self.selected = False

    def is_set(self):
        return self.selected

    def set(self):
        self.selected = True
