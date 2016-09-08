from SudokuGenerator import SudokuGenerator


class Solver(SudokuGenerator):
    def __init__(self, n):
        """Constructor whitch creates SudokuGenerator object _obj and
            generate sudoku with n blank fields."""
        SudokuGenerator.__init__(self)
        self._obj = SudokuGenerator()
        self._obj.generate_sudoku(n)

    def solver_row_1(self, n):
        """Function solves n row of sudoku if ther's only 1 blank (0) field and returns 1.
            In other case returns 0 and does nothing."""
        num, flag = 0, 0
        for i in range(0, 9):
            if self._obj._board[n][i] == 0:
                flag += 1

        if flag > 1 or flag == 0:
#            print "exit row"
            return 0

        for i in range(1, 10):
            if not i in self._obj._board[n]:
                num = i

        for i in range(0, 9):
            if self._obj._board[n][i] == 0:
#                print "w kolumnie: ", i, "rzad: ", n, "wartosc: ", num, "row"
                self._obj._board[n][i] = num

        return 1

    def solver_col_1(self, n):
        """Function solves n col of sudoku if ther's only 1 blank (0) field and returns 1.
            In other case returns 0 and does nothing."""
        num, flag = 0, 0
        tmp = [self._obj._board[i][n] for i in range(0, 9)]
        for i in range(0, 9):
            if tmp[i] == 0:
                flag += 1

        if flag > 1 or flag == 0:
#            print "exit col"
            return 0

        for i in range(1, 10):
            if not i in tmp:
                num = i

        for i in range(0, 9):
            if tmp[i] == 0:
                self._obj._board[i][n] = num
#                print "w kolumnie: ", n, "rzad: ", i, "wartosc: ", num, "col"

        return 1

    def solver_squeres_1(self, n):
        """
        Given n equals to square 3x3 in this order:
                1   2   3
                4   5   6
                7   8   9.
        Function solves n square of sudoku if ther's only 1 blank field and returns 1.
            In other case returns 0 and does nothing."""
        num, plc, flag, tmp = 0, 0, 0, []
        for i in range((n / 3) * 3, (n / 3) * 3 + 3):
            for j in range((n % 3) * 3, (n % 3) * 3 + 3):
                tmp.append(self._obj._board[i][j])

        for i in range(0, 9):
            if tmp[i] == 0:
                flag += 1
                plc = i

        if flag > 1 or flag == 0:
#            print "exit sqr"
            return 0

        for i in range(1, 10):
            if not i in tmp:
                num = i

        self._obj._board[(n / 3) * 3 + plc / 3][(n % 3) * 3 + plc % 3] = num

        return 1

    def zeros_counter(self):
        """Simple function that count all zeroes on whole board."""
        n = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if self._obj._board[i][j] == 0:
                    n += 1
#        print "Number of zeros", n
        return n

    def solve(self):
        """Basic solving function that checks if ther's any 1 field empty
        row, col or square."""
        flag, zeros, counter = 0, self.zeros_counter(), 0
        for j in range(0, 10):
            for i in range(0, 9):
                if not self._obj.row_check(i):
#                    print "----ROW-----", i
                    flag += self.solver_row_1(i)
                if not self._obj.col_check(i):
#                    print "----COL-----", i
                    flag += self.solver_col_1(i)
                if not self._obj.squeres_check(i):
#                    print "---SQR------", i
                    flag += self.solver_squeres_1(i)
                counter += 1

tab = []
for j in range(0, 25):
    it = 0
    for i in range(0, 1000):
        t = Solver(j)
        t.solve()
        if t._obj.full_check():
            it += 1
    tab.append(float(it)/1000 * 100)

for i in range (0, 25):
    print "     n", i, "rozwiazane w: ", tab[i]," %"
