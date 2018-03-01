class Ride():
    id: int
    startLocation: "Intersection"
    endLocation: "Intersection"
    startTime: int
    endTime: int

    def __init__(self, id: int, startLocation: int, endLocation: int, startTime: int, endTime: int) -> None:
        assert startTime >= 0
        assert endTime >= 0

        self.id = id
        self.startLocation = startLocation
        self.endLocation = endLocation
        self.startTime = startTime
        self.endTime = endTime

    def distance(self) -> int:
        return self.startLocation.distanceTo(self.endLocation)
