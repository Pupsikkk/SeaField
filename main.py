from Game import Game

while True:
    inp = ""
    while True:
        inp = input("Если хотите включить режим админа "
                    "(позволяет видеть поле бота)"
                    " введите 1, если нет -- 0: ")
        if inp == "0" or inp == "1":
            break
        else:
            print("Некорректный выбор! Попробуйте еще раз\n\n")
    inp = int(inp)
    new_game = Game(inp)
    new_game.start_game()
    inp = ""
    while True:
        inp = input("Если хотите сыграть снова введите 1, если нет -- 0: ")
        if inp == "0" or inp == "1":
            break
        else:
            print("Некорректный выбор! Попробуйте еще раз\n\n")
    if inp == "0":
        break
    print("\n"*30)
