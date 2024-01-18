class Game:
    matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def __init__(self):
        self.player = "X"

    def start(self):
        while True:
            self.play(self.player)
            self.print_matrix()
            if self.check_game_over():
                play_again = input("Хотите сыграть еще раз? (Введите 'да' или 'нет'): ")
                while play_again.lower() not in ['да', 'нет']:
                    print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")
                    play_again = input("Хотите сыграть еще раз? (Введите 'да' или 'нет'): ")

                if play_again.lower() == 'нет':
                    print("Игра завершена. До свидания!")
                    break
                else:
                    self.start()

    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(self.matrix[i][j], end='  ')
            print()

    def play(self, player):
        print(f"Ходит игрок {player}!")
        while True:
            try:
                i = int(input("Введите номер строки: "))
                j = int(input("Введите номер столбца: "))
                if 1 <= i <= 3 and 1 <= j <= 3 and self.matrix[i - 1][j - 1] == "-":
                    self.matrix[i - 1][j - 1] = player
                    if self.player == "X":
                        self.player = "O"
                    else:
                        self.player = "X"
                    break
                else:
                    print("Введенные данные неверны! Повторите ввод.")
            except ValueError:
                print("Ошибка! Введите целое число.")

    def check_game_over(self):
        for i in range(len(self.matrix)):
            check_symbol = self.matrix[i][0]
            for j in range(1, len(self.matrix[0])):
                if self.matrix[i][j] != check_symbol or self.matrix[i][j] == "-":
                    break
            else:
                print(f"Игра окончена! Победил игрок {check_symbol}")
                return True

        for j in range(len(self.matrix[0])):
            check_symbol = self.matrix[0][j]
            for i in range(1, len(self.matrix)):
                if self.matrix[i][j] != check_symbol or self.matrix[i][j] == "-":
                    break
            else:
                print(f"Игра окончена! Победил игрок {check_symbol}")
                return True

        check_symbol = self.matrix[0][0]
        for i in range(1, len(self.matrix)):
            if self.matrix[i][i] != check_symbol or self.matrix[i][i] == "-":
                break
        else:
            print(f"Игра окончена! Победил игрок {check_symbol}")
            return True

        check_symbol = self.matrix[0][2]
        for i in range(1, len(self.matrix)):
            if (self.matrix[i][len(self.matrix) - 1 - i] != check_symbol or
                    self.matrix[i][len(self.matrix) - 1 - i] == "-"):
                break
        else:
            print(f"Игра окончена! Победил игрок {check_symbol}")
            return True

        all_write = True
        for i in range(len(self.matrix)):
            for j in range(1, len(self.matrix[0])):
                if self.matrix[i][j] == "-":
                    all_write = False
        if all_write:
            print(f"Игра окончена! Ничья!")
            return True

        return False


game = Game()
game.start()
