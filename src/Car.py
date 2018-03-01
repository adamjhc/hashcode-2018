from src.Direction import Direction
from src.Ride import Ride
from src.Intersection import Intersection

class Car(object):
    """two """
    currentLocation: "Intersection" = None
    drivingQueue: list = []
    id: int = None

    def __init__(self, location: "Intersection", id: int):
        self.currentLocation = location
        self.id = id

    def sendCarToLocation(self, location: "Intersection"):
        xMovement: int = location.row - self.currentLocation.row
        yMovement: int = location.column - self.currentLocation.column

        if(xMovement > 0):
            for i in xMovement:
                self.drivingQueue.append(2)
        if(xMovement < 0):
            for i in xMovement:
                self.drivingQueue.append(4)
        if(yMovement > 0):
            for i in yMovement:
                self.drivingQueue.append(1)
        if(yMovement > 0):
            for i in yMovement:
                self.drivingQueue.append(3)

    def canFinishRide(self, ride: "Ride", timeLeft: int) -> int:
        distance: int = self.currentLocation.distanceTo(ride.startLocation)

        frames: int = (distance + ride.time()) - timeLeft

        return frames > 0

    def getWeight(self, ride: "Ride", timeLeft: int) -> int:
        if self.canFinishRide(ride, timeLeft):
            return 0

        distanceToRide = self.currentLocation.distanceTo(ride.startLocation)

        return distanceToRide - ride.time()


    def move(self):
        if (self.drivingQueue != []):
            nextInstruction = self.drivingQueue[0]
            if(nextInstruction == Direction.NORTH):
                self.moveNorth()
            if(nextInstruction == Direction.EAST):
                self.moveEast()
            if(nextInstruction == Direction.SOUTH):
                self.moveSouth()
            if(nextInstruction == Direction.WEST):
                self.moveWest()

    def moveNorth(self):
        self.currentLocation.row += 1

    def moveEast(self):
        self.currentLocation.column += 1

    def moveSouth(self):
        self.currentLocation.row -= 1

    def moveWest(self):
        self.currentLocation.column -= 1
