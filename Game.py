from Player import Player


class Game:
    def __init__(self, admin_option):
        self.admin_option = admin_option
        self.size = 6
        self.player = Player(self, 0)
        self.bot = Player(self, 1)
        self.isPlayerTurn = True

    def turn(self, player, enemy):
        if not player.isBot:
            first_field = player.player_field
            second_field = player.enemy_field
            print(("    " + "   ".join([f"{i + 1}" for i in range(self.size)]) + "         ") * 2)
            counter = 1
            for first, second in zip(first_field.get_field(), second_field.get_field()):
                print(str(counter) + " | " + " | ".join(first) + " |       " +
                      str(counter) + " | " + " | ".join(second) + " | ")
                counter += 1
        else:
            if self.admin_option:
                print("\n\n\nBOT field below\n\n")
                first_field = player.player_field
                second_field = player.enemy_field
                print(("    " + "   ".join([f"{i + 1}" for i in range(self.size)]) + "         ") * 2)
                counter = 1
                for first, second in zip(first_field.get_field(), second_field.get_field()):
                    print(str(counter) + " | " + " | ".join(first) + " |       " +
                          str(counter) + " | " + " | ".join(second) + " | ")
                    counter += 1
                print("\n\nBOT field behind\n\n\n")

        while True:
            shoot = player.shoot()
            if enemy.player_field.f[shoot[0]][shoot[1]] == "O" or enemy.player_field.f[shoot[0]][shoot[1]] == " ":
                ship_is_shooted = False
                # print([i.get_position for i in enemy.player_field.ship_tile])
                for i in enemy.player_field.ship_tile:
                    if i.get_position == shoot:
                        if player.isBot:
                            print("\nПротивник попал: ", shoot[0] + 1, shoot[1] + 1, "\n\n")
                        enemy.player_field.f[shoot[0]][shoot[1]] = "X"
                        player.enemy_field.f[shoot[0]][shoot[1]] = "X"
                        enemy.player_field.ship_tile.remove(i)
                        ship_is_shooted = True
                        break
                if not ship_is_shooted:
                    if player.isBot:
                        print("\nПротивник промахнулся: ", shoot[0] + 1, shoot[1] + 1, "\n\n")
                    enemy.player_field.f[shoot[0]][shoot[1]] = "•"
                    player.enemy_field.f[shoot[0]][shoot[1]] = "•"
                break
            else:
                if not player.isBot:
                    print("\nВы сюда уже стреляли\n\n")
                continue

    @staticmethod
    def end_game_check(enemy):
        if len(enemy.player_field.ship_tile) == 0:
            return True
        return False

    def start_game(self):
        while True:
            if self.isPlayerTurn:
                self.turn(self.player, self.bot)
                if self.end_game_check(self.bot):
                    print("\n\nВы победили!!!\n\n")
                    break
            else:
                self.turn(self.bot, self.player)
                if self.end_game_check(self.player):
                    print("\n\nВы проиграли!!!\n\n")
                    break
            self.isPlayerTurn = not self.isPlayerTurn
