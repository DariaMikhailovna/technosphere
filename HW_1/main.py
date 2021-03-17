from termcolor import colored


class Board:

    def __init__(self):
        self.grid = [['.', '.', '.'],
                     ['.', '.', '.'],
                     ['.', '.', '.']]

    def is_empty(self, row, column):
        return self.grid[row][column] == '.'

    def insert(self, row, column, key):
        self.grid[row][column] = key

    def show_grid(self):
        for i in range(3):
            print(colored(''.join(self.grid[i]), 'yellow'))

    def check_column(self, curr_column, key):
        return self.grid[0][curr_column] == \
               self.grid[1][curr_column] == \
               self.grid[2][curr_column] == key

    def check_row(self, curr_row, key):
        return self.grid[curr_row][0] ==\
               self.grid[curr_row][1] ==\
               self.grid[curr_row][2] == key

    def check_diagonals(self, key):
        return self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == key \
               or self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == key

    def is_full(self):
        return '.' not in [c for r in self.grid for c in r]


class TicTacGame:
    board = Board()
    dict = {'X': 'крестики', '0': 'нолики'}
    curr_key = 'X'

    def start_game(self):
        self.show_board()
        while True:
            curr_row, curr_column = self.get_input(self.curr_key)
            if not self.validate(curr_row, curr_column):
                continue
            self.board.insert(curr_row, curr_column, self.curr_key)
            self.board.show_grid()
            if self.check_winner(curr_row, curr_column):
                break
            if self.board.is_full():
                print(colored('Ничья', 'red'))
                break
            self.change_key()

    def validate(self, row, column):
        if not self.board.is_empty(row, column):
            print('Эта клетка занята, выберите другую')
            return False
        return True

    def change_key(self):
        self.curr_key = '0' if self.curr_key == 'X' else 'X'

    def show_board(self):
        self.board.show_grid()

    def get_input(self, key):
        print(f'Ходят {self.dict[key]}')
        row = self.read_number('ряда')
        column = self.read_number('строки')
        return row, column

    @staticmethod
    def read_number(text):
        while True:
            try:
                number = int(input(f"Введите номер {text} от 1 до 3: "))
            except ValueError:
                print('Строка и столбец должны быть цифрами')
            else:
                if 1 <= int(number) <= 3:
                    return number - 1
                else:
                    print('Строка и столбец должны быть цифрами от 1 до 3')

    def check_winner(self, curr_row, curr_column):
        if self.board.check_column(curr_column, self.curr_key)\
                or self.board.check_row(curr_row, self.curr_key) \
                or self.board.check_diagonals(self.curr_key):
            print(colored(f'Победили {self.dict[self.curr_key]}', 'red'))
            return True
        return False


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
