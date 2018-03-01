class Ride():
    startLocation = None
    endLocation = None
    startTime = None
    endTime = None

    def __init__(self, startLocation: int, endLocation: int, startTime: int, endTime: int) -> None:
        assert startTime >= 0
        assert endTime >= 0

        self.startLocation = startLocation
        self.endLocation = endLocation
        self.startTime = startTime
        self.endTime = endTime

    def distance(self) -> int:
        return self.startLocation.distanceTo(self.endLocation)
