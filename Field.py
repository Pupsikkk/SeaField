import random
from Ship import Ship


class Field:
    def __init__(self, size):
        self.size = size
        self.f = [[" "] * size for _ in range(size)]
        self.ship_tile = []
        self.busy_dots = []

    def draw_field(self):
        print("    " + "   ".join([f"{i + 1}" for i in range(self.size)]) + "   ")
        for i, item in enumerate(self.f):
            print(str(i + 1) + " | " + " | ".join(item) + " | ")

    def get_field(self):
        return self.f

    def add_ship(self, ship_body):
        for tile in ship_body:
            if tile.get_position in self.busy_dots:
                return False
        if self.ship_is_correct_on_field(ship_body):
            for tile in ship_body:
                x, y = tile.get_position
                self.f[x][y] = "O"
                self.add_busy_dots(tile)
            self.ship_tile.extend(ship_body)
            return True

    def ship_is_correct_on_field(self, ship_body):
        if (ship_body[0].get_position[0] < self.size and
                ship_body[0].get_position[0] < self.size and
                ship_body[len(ship_body) - 1].get_position[0] < self.size and
                ship_body[len(ship_body) - 1].get_position[1] < self.size):
            return True
        else:
            return False

    def add_busy_dots(self, dot):
        around_dots = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)]
        pos2 = dot.get_position
        for pos1 in around_dots:
            x = pos1[0] + pos2[0]
            y = pos1[1] + pos2[1]
            if self.size > x >= 0 and self.size > y >= 0:
                self.busy_dots.append([x, y])

    def create_random_field(self):
        def create_ship_with_some_length(length):
            nonlocal field
            counter = 0
            while not field.add_ship(Ship(random.randint(1, field.size),
                                          random.randint(1, field.size),
                                          length, random.randint(0, 1)).ship_body):
                counter += 1
                if counter == 100:
                    return False
            return True

        field = Field(self.size)
        while True:
            field.clear_field()
            indicate = True
            indicate = create_ship_with_some_length(3) and indicate
            indicate = create_ship_with_some_length(2) and indicate
            indicate = create_ship_with_some_length(2) and indicate
            for _ in range(4):
                indicate = create_ship_with_some_length(1) and indicate
            if indicate:
                break
        return field

    def clear_field(self):
        self.f = [[" "] * self.size for _ in range(self.size)]
        self.busy_dots = []
        self.ship_tile = []

