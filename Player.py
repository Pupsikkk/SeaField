import random
from Field import Field


class Player:
    def __init__(self, game, isBot):
        self.size = game.size
        self.game = game
        self.isBot = isBot
        self.player_field = self.choose_field() if not isBot else Field(self.game.size).create_random_field()
        self.enemy_field = Field(game.size)

    def shoot(self):
        inp_list = []
        if not self.isBot:
            while True:
                inp_list.clear()
                inp_list = input("Введите координаты выстрела: ").split()
                if len(inp_list) != 2:
                    print("Введите две координаты\n")
                    continue
                elif not (inp_list[0].isdigit() and inp_list[1].isdigit()):
                    print("Вводите числа\n")
                    continue
                elif not (1 <= int(inp_list[0]) <= self.size and 1 <= int(inp_list[1]) <= self.size):
                    print("Не выходите за грани поля\n")
                    continue
                else:
                    break
        else:
            inp_list = [0, 0]
            inp_list[0] = random.randint(0, self.size)
            inp_list[1] = random.randint(0, self.size)
        return [int(inp_list[0]) - 1, int(inp_list[1]) - 1]

    def choose_field(self):
        print("Выберите поле для игры")
        rnd_field = ''
        while True:
            rnd_field = Field(self.game.size).create_random_field()
            rnd_field.draw_field()
            choose = input("Введите 1 если согласны, 0 если нет:")
            if choose == "0":
                continue
            elif choose == "1":
                break
            else:
                print("\nВведите 0 или 1 (без пробелов)\n")
                continue
        return rnd_field
