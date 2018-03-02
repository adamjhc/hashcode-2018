class Intersection():
    def __init__(self, row: int, column: int) -> None:
        self.row: int = row
        self.column: int = column

    def distanceTo(self, other: "Intersection") -> int:
        return abs(self.row - other.row) + abs(self.column - other.column)
