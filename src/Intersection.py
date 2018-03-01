class Intersection():
    row: int = None
    column: int = None

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    def distanceTo(self, other: "Intersection") -> int:
        return abs(self.row - other.row) + abs(self.column - other.column)