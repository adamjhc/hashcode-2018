class Intersection():
    row = None
    column = None

    def __init__(self, row: int, column: int) -> None:
        assert row >= 0
        assert column >= 0

        self.row = row
        self.column = column

    def distanceTo(self, other: "Intersection") -> int:
        return abs(self.row - other.row) + abs(self.column - other.column)
