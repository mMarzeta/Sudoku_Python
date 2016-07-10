class Board:
    def __init__(self):
        """Simple constructor that fill all fields on _board with 0."""
        self._board = [[0 for col in range(9)] for row in range(9)]

    def print_board(self):
        """Function that prints _board."""
        for i in range(9):
            if i % 3 == 0:
                print " - - - - - - - - - - - - "
            for j in range(9):
                if j % 3 == 0:
                    print "|",
                print self._board[i][j],
            print "|"
        print " - - - - - - - - - - - - "

    def is_finished(self):
        """Function that check if _board is done. 0 equals to blank field."""
        for i in range(9):
            if 0 in self._board[i]:
                return False
            else:
                return True

    def row_check(self, row): #remember that we count from 0
        """Function that checks if "row" on _board is correctly filled"""
        tmp, it = self._board[row], 0
        for i in range(1,10):
            if tmp.__contains__(i):
                it += 1
        if it == 9:
            return True
        else:
            return False

    def col_check(self, col): #remember that we count from 0
        """Function that checks if "col" on _board is correctly filled"""
        tmp, it = [item[col] for item in self._board], 0
        for i in range(1,10):
            if tmp.__contains__(i):
                it += 1
        if it == 9:
            return True
        else:
            return False

    def squeres_check(self, x, y): #count from 1
        """Function that checks if 3x3 square is correctly. X and Y are counted from 1 to 3.
            11  12  13
            21  22  23
            31  32  33"""
        sub_matrix = [self._board[i][x * 3 - 3: x * 3] for i in range(y * 3 - 3, y * 3)]
        print sub_matrix

    def test_function1(self):
        """Function that tests if constructor works properly."""
        tmp = 0
        for i in range(9):
            for j in range(9):
                if self._board[i][j] == 0:
                    tmp += 1
        assert tmp == 81, 'Error in constructor. Number of fields with 0 does not' \
                          ' equal to 81 (all fields).'

t = Board()
t._board = [[2,9,3,4,6,5,7,8,1], [1,0,0,0,2,0,0,0,8], [3,0,0,0,0,3,0,0,7], [4,0,0,0,5,0,0,0,6],
               [5,0,0,4,0,3,0,0,2], [9,0,0,4,0,0,2,0,3], [8,0,1,0,0,8,0,0,4], [7,0,0,1,0,3,0,0,5],
               [6,0,0,8,0,0,0,0,9]]
t.print_board()
print t.row_check(0)
print t.col_check(8)
t.squeres_check(1, 2)