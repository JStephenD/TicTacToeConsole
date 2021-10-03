from functools import partial
from game import TicTacToeGame
from player import Player
from rules import check_winner_column, check_winner_diagonal, check_winner_row


game = TicTacToeGame(gridSize=3)
playerX = Player("X")
playerO = Player("O")
game.add_player(playerX)
game.add_player(playerO)

game.board.grid = [["X", " ", " "], ["X", " ", " "], [" ", " ", " "]]

grid = game.board.grid
game.add_rules(
    partial(check_winner_row, grid),
    partial(check_winner_column, grid),
    partial(check_winner_diagonal, grid),
)

if winner := game.check_winner():
    print(f"{winner=}")
