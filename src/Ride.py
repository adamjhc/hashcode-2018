from src.Intersection import Intersection

class Ride():
    def __init__(self, id: int, startLocation: "Intersection", endLocation: "Intersection", startTime: int, endTime: int) -> None:
        assert startTime >= 0
        assert endTime >= 0

        self.id: int = id
        self.startLocation: "Intersection" = startLocation
        self.endLocation: "Intersection" = endLocation
        self.startTime: int = startTime
        self.endTime: int = endTime

    def distance(self) -> int:
        return self.startLocation.distanceTo(self.endLocation)
