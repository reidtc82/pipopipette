# Access these directly when setting.
class Line:
    def __init__(self, id):
        self.selected = False
        self.id = id

    def is_set(self):
        return self.selected

    def set(self):
        self.selected = True

    def get_id(self):
        return self.id
