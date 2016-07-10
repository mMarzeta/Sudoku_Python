from Board import Board
import random


class SudokuGenerator(Board):

    def generate_sudoku(self):
        """Function that fills board with random digits(1-9) in random fields until
        all fields are filled. Function fill field only if it is available, if not,
        another random numbers are generated"""
        while not self.is_finished():   #fill until all fields on _board are not empty
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self._board[row][col] == 0:
                self._board[row][col] = random.randint(0, 8)


t = Board()
t._board[0] = [1,2,3,4,5,6,7,8,9]
t.print_board()
print t.row_check(0)
