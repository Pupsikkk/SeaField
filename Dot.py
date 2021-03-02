class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def get_position(self):
        return [self.x, self.y]
