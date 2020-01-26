import pygame
from graphics.colors import Colors


class Card:
    def __init__(self, value, row, col, width, height):
        self._value = value
        self._temp_value = 0
        self._row = row
        self._col = col
        self._width = width
        self._height = height
        self._selected = False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def temp_value(self):
        return self._temp_value

    @temp_value.setter
    def temp_value(self, val):
        self._temp_value = val

    def has_temp_value(self):
        return True if self._temp_value != 0 else False

    def draw(self, win):
        draft_fnt = pygame.font.SysFont("comicsans", 30)
        solid_fnt = pygame.font.SysFont("comicsans", 40)

        gap = self._width / 9
        x = self._col * gap
        y = self._row * gap

        if self._temp_value != 0 and self._value == 0:
            text = draft_fnt.render(str(self._temp_value), 1, Colors.GRAY)
            win.blit(text, (x + 5, y + 5))
        elif not (self._value == 0):
            text = solid_fnt.render(str(self.value), 1, Colors.BLACK)
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y +
                            (gap / 2 - text.get_height() / 2)))

        if self._selected:
            pygame.draw.rect(win, Colors.RED, (x, y, gap, gap), 3)
