from Board import Board
import random


class SudokuGenerator(Board):
    def __init__(self):
        """Simple contructor need by class hierarchy."""
        Board.__init__(self)

    def generate_basic_sudoku(self):
        """Function that fills board with numbers makes correct sudoku combination."""
        k, n = 1, 1
        for i in range(9):
            k = n
            for j in range(9):
                if k <= 9:
                    self._board[i][j] = k
                    k += 1
                else:
                    k = 1
                    self._board[i][j] = k
                    k += 1
            n = k + 3
            if k == 10:
                n = 4
            if n > 9:
                n = n % 9 + 1

    def row_swap(self, x, y):
        """Function that swaps x row with y row."""
        tmp = self._board[x]
        self._board[x] = self._board[y]
        self._board[y] = tmp

    def col_swap(self, x, y):
        """Function that swaps x column with y column."""
        tmp = [item[x] for item in self._board]
        for i in range(0, 9):
            self._board[i][x] = self._board[i][y]
            self._board[i][y] = tmp[i]

    def group_row_swap(self, x, y):
        """Function swaps group of 3 rows with another one. X and Y are in range(1,3)"""
        for i in range(0, 3):
            self.row_swap(x * 3 + i, y * 3 + i)

    def group_col_swap(self, x, y):
        """Function swaps group of 3 columns with another one. X and Y are in range(1,3)"""
        for i in range(0, 3):
            self.col_swap(x * 3 + i, y * 3 + i)

    def sudoku_shuffle(self):
        """Function does randomisation of generated sudoku"""
        for i in range(0, 2):
            x = random.randint(0, 8)
            if x <= 2:
                y = random.randint(0, 2)
                if y == x:
                    while y == x:
                        y = random.randint(0, 2)
            elif x <= 5:
                y = random.randint(3, 5)
                if y == x:
                    while y == x:
                        y = random.randint(3, 5)
            elif x <= 8:
                y = random.randint(6, 8)
                if y == x:
                    while y == x:
                        y = random.randint(6, 8)
            self.row_swap(x, y)
            self.col_swap(x, y)

    def remover(self, N):
        """Function removes random field in sudoku by overwriting them with 0.
            N parameter is number of fields to remove and have to be <= 81."""
        if N > 81:
            raise ValueError('Incorrect input number. 81 is maximum')
        i, x, y = 0, random.randint(0, 8), random.randint(0, 8)
        while i < N:
            if self._board[x][y] != 0:
                self._board[x][y] = 0
            elif self._board[x][y] == 0:
                while self._board[x][y] == 0:
                    x = random.randint(0, 8)
                    y = random.randint(0, 8)
                self._board[x][y] = 0
            i += 1

    def generate_sudoku(self, n):
        """Most important function in SudokuGenerator.
            Generate shuffled sudoku with blank fields."""
        self.generate_basic_sudoku()
        self.sudoku_shuffle()
        self.remover(n)
        #self.print_board()
