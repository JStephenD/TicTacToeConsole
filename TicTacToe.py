from typing import Callable, List
from player import Player
from board import TicTacToeBoard
from enum import Enum, auto


class TicTacToe:
    def __init__(self, gridSize: int = 3):
        self.gridSize = gridSize
        self.players: List[Player] = []
        self.rules: List[Callable] = []
        self.board = TicTacToeBoard(self.gridSize, self.gridSize)

    def add_player(self, player: Player):
        self.players.append(player)

    def add_rules(self, *rules: Callable):
        for rule in rules:
            self.rules.append(rule)

    def place_symbol(self, player: Player, x: int, y: int):
        if result := self.board.set_cell(player, x, y):
            return result

    def check_winner(self):
        for rule in self.rules:
            if winner := rule():
                return winner


# this class is for the basic representation of the game in of itself
# customization, such as for this mini project, is done through inheriting this class
# and putting it in the context of a console application.
# which means, for GUI application, inherit this class and customize the GUI behaviors,
# not necessarily the Game behavior themselves.
