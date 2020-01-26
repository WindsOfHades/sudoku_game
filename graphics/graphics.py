import pygame
from graphics.board import Board
from graphics.colors import Colors
from utils import load_config


class GraphicalGame:
    def __init__(self, puzzle):
        pygame.font.init()
        pygame.display.set_caption("Sudoko")
        config = load_config()
        width = config["graphics"]["width"]
        height = config["graphics"]["height"]
        self._win = pygame.display.set_mode((width, height))
        self._board = Board(puzzle, 9, 9, width, width)

    def redraw_window(self):
        self._win.fill(Colors.WHITE)
        # fnt = pygame.font.SysFont("comicsans", 40)
        # text = fnt.render("Time: ", 1, Colors.BLACK)
        # win.blit(text, (540 - 160, 560))
        self._board.draw(self._win)

    def game_loop(self):
        keep_running = True
        key = None

        while keep_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    card_detected = self._board.detect_card(pos)
                    if card_detected:
                        self._board.select(card_detected[0], card_detected[1])
                        key = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        key = 1
                    if event.key == pygame.K_2:
                        key = 2
                    if event.key == pygame.K_3:
                        key = 3
                    if event.key == pygame.K_4:
                        key = 4
                    if event.key == pygame.K_5:
                        key = 5
                    if event.key == pygame.K_6:
                        key = 6
                    if event.key == pygame.K_7:
                        key = 7
                    if event.key == pygame.K_8:
                        key = 8
                    if event.key == pygame.K_9:
                        key = 9
                    if event.key == pygame.K_RETURN:
                        if self._board.insert_number() is False:
                            print("Wrong")
                        else:
                            print("Correct")
                        key = None
                        if self._board.is_filled():
                            print("Game Over")

            if self._board.selected_card and key is not None:
                self._board.insert_draft(key)

            self.redraw_window()
            pygame.display.update()
        pygame.quit()
