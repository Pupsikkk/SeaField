from Dot import Dot


class Ship:
    def __init__(self, x, y, length, isVertical):
        self.ship_body = []
        for i in range(length):
            self.ship_body.append(Dot(x + i * isVertical - 1, y + i * (not isVertical) - 1))

    @property
    def get_body(self):
        return self.ship_body
