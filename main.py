import argparse
from solver import Solver
import utils
from graphics.graphics import GraphicalGame


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text",
                        action="store_true",
                        default=False,
                        help="Run in text mode")
    args = parser.parse_args()
    board = utils.generate_board()

    if args.text:
        solver = Solver(board)
        solver.print_board()
        print('*' * 60, "SOLUTION", '*' * 60)
        solver.solve()
        solver.print_board()
        return

    GraphicalGame(board).game_loop()


if __name__ == "__main__":
    main()
