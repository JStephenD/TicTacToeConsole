from player import Player


class Board:
    def __init__(self, sizeX: int, sizeY: int):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = [[" " for _ in range(self.sizeY)] for _ in range(sizeX)]


class TicTacToeBoard(Board):
    def set_cell(self, obj: Player, x: int, y: int):
        if self.grid[x][y] != " ":
            return
        self.grid[x][y] = obj.symbol
        return True

    def draw(self):
        for x in range(self.sizeX * 2 - 1):
            if x % 2 == 0:
                row = self.grid[int(x / 2)]
                print(" | ".join([cell for cell in row]))
            else:
                dashes = "-" * self.sizeX
                print(" + ".join(dashes))


# can be added:
# Board instance for GUI app
