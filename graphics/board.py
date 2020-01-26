import pygame
from graphics.colors import Colors
from graphics.card import Card
from solver import Solver


class Board:
    def __init__(self, puzzle, rows, cols, width, height):
        self._rows = rows
        self._cols = cols
        self._width = width
        self._height = height
        self._selected_card_position = None
        self._model = None
        self._puzzle = puzzle
        self._solver = Solver(puzzle)
        self._cards = [[
            Card(puzzle[i][j], i, j, width, height) for j in range(cols)
        ] for i in range(rows)]

    @property
    def selected_card(self):
        return self._selected_card_position

    def draw(self, win):
        self._draw_lines(win)
        self._draw_cards(win)

    def insert_draft(self, draft_number):
        row, col = self._selected_card_position
        self._cards[row][col].temp_value = draft_number

    def insert_number(self):
        row, col = self._selected_card_position
        # check selected position has a draft
        if self._cards[row][col].has_temp_value():
            # check if selected position is empty
            # else set the value and update the model
            if self._cards[row][col].value == 0:
                self._cards[row][col].value = self._cards[row][col].temp_value
                self._update_model()

            # now check if the model is solvable
            if self._solver.validate_number(
                    self._cards[row][col].value,
                (row, col)) and self._solver.solve():
                return True
            # else clear the card value and draft value update the model and return False
            else:
                self._cards[row][col].value = 0
                self._cards[row][col].temp_value = 0
                self._update_model()
                return False

    def detect_card(self, position):
        gap = self._width / 9
        if position[0] < self._width and position[1] < self._height:
            x = position[0] // gap
            y = position[1] // gap
            return (int(y), int(x))
        else:
            None

    def select(self, row, column):
        self._deselect_cards()
        self._cards[row][column]._selected = True
        self._selected_card_position = (row, column)

    def is_filled(self):
        for i in range(self._rows):
            for j in range(self._cols):
                if self._cards[i][j].value == 0:
                    return False
        return True

    def _deselect_cards(self):
        for i in range(self._rows):
            for j in range(self._cols):
                self._cards[i][j]._selected = False

    def _draw_lines(self, win):
        gap = self._width / 9
        for i in range(self._rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, Colors.BLACK, (0, i * gap),
                             (self._width, i * gap), thick)
            pygame.draw.line(win, Colors.BLACK, (i * gap, 0),
                             (i * gap, self._height), thick)

    def _draw_cards(self, win):
        for i in range(self._rows):
            for j in range(self._cols):
                self._cards[i][j].draw(win)

    def _update_model(self):
        self._model = [[self._cards[i][j].value for j in range(self._cols)]
                       for i in range(self._rows)]
