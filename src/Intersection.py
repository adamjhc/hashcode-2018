class Intersection():
    row: int
    column: int

    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

    def distanceTo(self, other: "Intersection") -> int:
        return abs(self.row - other.row) + abs(self.column - other.column)
