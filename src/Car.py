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

    def isAvailable(self) -> bool:
        return self.ride == None

    def addRide(self, ride: "Ride", currentTime: int) -> None:
        self.ride = ride
        if ride is not None:
            self.location = ride.endLocation

            distance: int = self.location.distanceTo(ride.startLocation)
            self.timeWhenAvailable = currentTime + distance + ride.distance()
        else:
            self.timeWhenAvailable = currentTime

    def update(self, currentTime: int, nextRide: "Ride") -> bool:
        # Take the ride if we are in the first time frame
        if currentTime == 0:
            self.addRide(nextRide, currentTime)
            return True

        if currentTime == self.timeWhenAvailable:
            self.previousRides.append(self.ride)

            self.addRide(nextRide, currentTime)
            return True

        return False

    def getSubmissionLine(self) -> str:
        line: str = str(len(self.previousRides))

        for ride in self.previousRides:
            line += " {:d}".format(ride.id)

        return line
