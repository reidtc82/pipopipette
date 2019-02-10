class Manager:
    def __init__(self):
        self.lock_io = False
        
    def lock_input(self):
        self.lock_io = True

    def unlock_input(self):
        self.lock_io = False
