from functools import partial
from time import time

from TicTacToe import TicTacToe
from player import Player
from rules import check_winner_row, check_winner_column, check_winner_diagonal
from pynput.keyboard import Key, Listener


class TicTacToeGame(TicTacToe):
    """TicTacToeGame is the implementation of the tic tac toe game for a console enviroment
    We don't want to implement game behavior specific code here; just the interaction between
    players and the app.
    """

    def __init__(self, gridSize: int = 3):
        super().__init__(gridSize=gridSize)
        self._initialize()

    def _initialize(self):
        self.running = False
        self.SHOW_CURSOR = True
        self.CURSOR_POSITION = [0, 0]

    def start(self):
        print(f"\nTIC TAC TOE CONSOLE REALTIME\n")
        for _ in range(self.gridSize * 2):  # initialize the board
            print()
        listener = Listener(on_release=self.on_release)
        listener.start()

        self.running = True
        self.current_player = self.players[0]

    def end(self, message: str = ""):
        self.SHOW_CURSOR = False
        self.draw()
        print(f"Game Ended: {message}")
        self.running = False

    def process_keypress(self, key: Key):
        x, y = self.CURSOR_POSITION
        if key == Key.left:
            # check if position at end
            self.CURSOR_POSITION[1] = y - 1 if y - 1 != -1 else self.gridSize - 1
        if key == Key.right:
            self.CURSOR_POSITION[1] = y + 1 if y + 1 != self.gridSize else 0
        if key == Key.up:
            self.CURSOR_POSITION[0] = x - 1 if x - 1 != -1 else self.gridSize - 1
        if key == Key.down:
            self.CURSOR_POSITION[0] = x + 1 if x + 1 != self.gridSize else 0
        if key == Key.space:
            if self.place_symbol(self.current_player, x, y):
                curr_player_idx = self.players.index(self.current_player)
                if curr_player_idx == len(self.players) - 1:
                    self.current_player = self.players[0]
                else:
                    self.current_player = self.players[curr_player_idx + 1]

    def on_release(self, key: Key):
        if key in [Key.left, Key.right, Key.up, Key.down, Key.space]:
            self.process_keypress(key)
        if key == Key.esc:
            self.end("Stopped the game (ESC)")
            return False

    def update(self):
        self.SHOW_CURSOR = not self.SHOW_CURSOR
        if winning_symbol := self.check_winner():
            self.end(f"Player {winning_symbol} WON!")

    def draw(self):
        if not self.running:
            return
        print(f"\033[{self.gridSize * 2}A", end="")  # set cursor position to start

        self.board.draw()
        print(f"Current Player: {self.current_player.symbol}")

        if self.SHOW_CURSOR:
            x, y = self.CURSOR_POSITION
            print(f"\033[{self.gridSize * 2}A", end="")  # set cursor position to start

            # cursor movement of 0 still moves it by 1; do not print if no movement needed
            if x != 0:
                rowpos = x * 2
                print(f"\033[{rowpos}B", end="")  # set cursor position to row

            if y != 0:
                colpos = y * 4
                print(f"\r\033[{colpos}C|", end="")  # set cursor position to column
            else:
                print(f"\r|", end="")

            # set cursor position to end of grid and start of console column
            print(f"\r\033[{(self.gridSize - x + 1) * 2}B", end="")


# o | o | o
# - + - + -
# o | o | o
# - + - + -
# x | x | x


gridSize = 3  # the board size x by x
TIMESTEP = 0.25  # re draw every x seconds
START = time()


def main():
    global TIMESTEP, START, gridSize
    game = TicTacToeGame(gridSize)
    playerX = Player("X")
    playerO = Player("O")
    game.add_player(playerX)
    game.add_player(playerO)

    grid = game.board.grid
    game.add_rules(
        partial(check_winner_row, grid),
        partial(check_winner_column, grid),
        partial(check_winner_diagonal, grid),
    )

    game.start()
    while game.running:
        if (time() - START) > TIMESTEP:
            START = time()

            game.update()
            game.draw()


if __name__ == "__main__":
    main()
