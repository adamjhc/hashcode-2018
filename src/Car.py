from typing import List
from src.Direction import Direction
from src.Ride import Ride
from src.Intersection import Intersection

class Car():
    location: "Intersection"
    ride: "Ride"
    previousRides: List[int]
    timeWhenAvailable: int

    def __init__(self):
        self.location = Intersection(0, 0)
        self.ride = None
        self.previousRides = []
        self.timeWhenAvailable = 0

    def isAvailable(self) -> bool:
        return self.ride == None

    def addRide(self, ride: "Ride", currentTime: int) -> None:
        self.ride = ride
        self.location = ride.endLocation

        distance: int = self.location.distanceTo(ride.startLocation)
        self.timeWhenAvailable = currentTime + distance + ride.distance()

    def update(self, currentTime: int, nextRide: "Ride") -> bool:
        # Take the ride if we are in the first time frame
        if currentTime == 0:
            self.addRide(nextRide, currentTime)
            return True

        if currentTime == self.timeWhenAvailable:
            self.previousRides.append(self.ride.id)


            self.addRide(nextRide, currentTime)
            return True

        return False

    def getSubmissionLine(self) -> str:
        line: str = str(len(self.previousRides))

        for rideId in self.previousRides:
            line += " {:d}".format(rideId)

        return line
