class Player:
    def __init__(self, symbol: str = "X"):
        self.symbol = symbol

    def __str__(self) -> str:
        return self.symbol


# can be added
# player info: name | wins | losses |
