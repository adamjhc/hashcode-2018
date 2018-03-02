from typing import List
from src.Direction import Direction
from src.Ride import Ride
from src.Intersection import Intersection

class Car():
    def __init__(self):
        self.location: "Intersection" = Intersection(0, 0)
        self.ride: "Ride" = None
        self.previousRides: List[Ride] = []
        self.timeWhenAvailable: int = 0

    def isAvailable(self, currentTime) -> bool:
        return currentTime == 0 or currentTime >= self.timeWhenAvailable

    def addRide(self, ride: "Ride", currentTime: int) -> None:
        self.ride = ride
        if ride is not None:
            distance: int = self.location.distanceTo(ride.startLocation)
            self.timeWhenAvailable = currentTime + distance + ride.distance()

            self.location = ride.endLocation
        else:
            self.timeWhenAvailable = currentTime

    def update(self, currentTime: int, nextRide: "Ride") -> None:
        if self.isAvailable(currentTime):
            if self.ride is not None:
                self.previousRides.append(self.ride)

            self.addRide(nextRide, currentTime)

    def getSubmissionLine(self) -> str:
        line: str = str(len(self.previousRides))

        for ride in self.previousRides:
            line += " {:d}".format(ride.id)

        return line

    def distanceTo(self, location: "Intersection") -> int:
        return self.location.distanceTo(location)
