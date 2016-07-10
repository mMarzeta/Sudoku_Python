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
        tmp = sum(sub_matrix, [])   #tricky convert from[x1,x2,x3][y1,y2,y3][z1,z2,z3] to
        it = 0                      #[x1,x2,x3,y1,y2,y3,z1,z2,z3]
        for i in range(1,10):
            if tmp.__contains__(i):
                it += 1
        if it == 9:
            return True
        else:
            return False

    def full_check(self):
        """Function that does full check _board. Uses other *_check() functions"""
        flag = 0    # flag++ for every *_check function that returns True

        for i in range(0, 9):
            if self.row_check(i):
                print "row: ", i
                flag += 1
            if self.col_check(i):
                print "col: ", i
                flag += 1

        for i in range (0, 3):
            for j in range (0, 3):
                if self.squeres_check(i, j):
                    print "squere: ", i, j
                    flag += 1

        print "flag: ", flag
        if flag == 27:
            return True
        else:
            return False