from typing import List


def check_winner_row(grid: List[List[str]]) -> str:
    for row in grid:
        if row[0] == " ":
            continue
        if len(set(row)) == 1:
            return row[0]


def check_winner_column(grid: List[List[str]]) -> str:
    gridSize = len(grid)

    for y in range(gridSize):
        if grid[0][y] == " ":
            continue
        if len(set(grid[i][y] for i in range(gridSize))) == 1:
            return grid[0][y]


def check_winner_diagonal(grid: List[List[str]]) -> str:
    gridSize = len(grid)
    if grid[int(gridSize / 2)][int(gridSize / 2)] == " ":
        return
    if len(set(grid[i][i] for i in range(gridSize))) == 1:
        return grid[0][0]
    if len(set(grid[i][gridSize - i - 1] for i in range(gridSize))) == 1:
        return grid[0][gridSize - 1]


# can be added:
# custom rules
