class Solver:
    def __init__(self, board):
        self._board = board

    def validate_number(self, number, position):
        # can place in row
        for i in range(len(self._board[0])):
            if self._board[position[0]][i] == number and position[1] != i:
                return False

        # can place in column
        for j in range(len(self._board)):
            if self._board[j][position[1]] == number and position[0] != j:
                return False

        # can place in box
        box_x = position[1] // 3
        box_y = position[0] // 3

        for box_row in range(box_y * 3, box_y * 3 + 3):
            for box_column in range(box_x * 3, box_x * 3 + 3):
                if self._board[box_row][box_column] == number and (
                        box_row, box_column) != position:
                    return False

        return True

    def solve(self):
        position = self._find_empty_position()
        if not position:
            return True
        else:
            row, column = position

        for number in range(1, 10):
            if self.validate_number(number, position):
                self._board[row][column] = number
                if self.solve():
                    return True
                self._board[row][column] = 0
        return False

    def print_board(self):
        for row_number in range(len(self._board)):
            Solver._print_row_separator(row_number)

            for column in range(len(self._board[0])):
                Solver._print_column_separator(column)
                if column == 8:
                    print(self._board[row_number][column])
                else:
                    print(f"{self._board[row_number][column]} ", end="")

    def _find_empty_position(self):
        for x in range(len(self._board)):
            for y in range(len(self._board[0])):
                if self._board[x][y] == 0:
                    return (x, y)

    @staticmethod
    def _print_row_separator(row_number):
        if row_number % 3 == 0 and row_number != 0:
            print('-' * 20)

    @staticmethod
    def _print_column_separator(column_number):
        if column_number % 3 == 0 and column_number != 0:
            print('|', end="")
