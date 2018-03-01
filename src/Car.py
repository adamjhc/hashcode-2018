from src.Direction import Direction
from src.Ride import Ride
from src.Intersection import Intersection


class Car():
    location: "Intersection" = None
    ride = None
    previousRides = []
    timeWhenAvailable = None

    def __init__(self, id: int):
        self.location = Intersection(0, 0)
        self.id = id

    def isAvailable(self):
        return ride == None

    def addRide(self, ride, currentTime):
        self.ride = ride
        location = ride.endLocation

        distance: int = self.location.distanceTo(ride.startLocation)
        return currentTime + distance + ride.time()

    def update(self, currentTime, nextRide):
        if currentTime == self.timeWhenAvailable:
            previousRides.append(ride.id)
            self.addRide(nextRide)

            # def canFinishRide(self, ride: "Ride", timeLeft: int) -> int:
            #     distance: int = self.currentLocation.distanceTo(ride.startLocation)

            #     frames: int = (distance + ride.time()) - timeLeft

            #     return frames > 0

            # def getWeight(self, ride: "Ride", timeLeft: int) -> int:
            #     if self.canFinishRide(ride, timeLeft):
            #         return 0

            #     distanceToRide = self.currentLocation.distanceTo(ride.startLocation)

            #     return distanceToRide - ride.time()

            # def move(self):
            #     if (self.drivingQueue != []):
            #         nextInstruction = self.drivingQueue[0]
            #         if(nextInstruction == Direction.NORTH):
            #             self.moveNorth()
            #         if(nextInstruction == Direction.EAST):
            #             self.moveEast()
            #         if(nextInstruction == Direction.SOUTH):
            #             self.moveSouth()
            #         if(nextInstruction == Direction.WEST):
            #             self.moveWest()

            # def moveNorth(self):
            #     self.currentLocation.row += 1

            # def moveEast(self):
            #     self.currentLocation.column += 1

            # def moveSouth(self):
            #     self.currentLocation.row -= 1

            # def moveWest(self):
            #     self.currentLocation.column -= 1

    def getSubmissionLine(self) -> str:
        line: str = str(len(self.previousRides))

        for ride in self.previousRides:
            line += " {:d}".format(ride.id)

        return line
