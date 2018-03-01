from src.Direction import Direction

class Car(object):
    """two """
    currentLocation = None
    drivingQueue = []
    iDNumber = None

    def __init__(self, location, iDNumber):
        self.currentLocation = location
        self.iDNumber = iDNumber

    def sendCarToLocation(end_location):
        xMovement = endLocation.row - self.currentLocation.row
        yMovement = endLocation.column - self.currentLocation.column
        if(xMovement > 0):
            for i in xMovement:
                self.drivingQueue.append(Direction.EAST)
        if(xMovement < 0):
            for i in xMovement:
                self.drivingQueue.append(Direction.WEST)
        if(yMovement > 0):
            for i in yMovement:
                self.drivingQueue.append(Direction.NORTH)
        if(yMovement > 0):
            for i in yMovement:
                self.drivingQueue.append(Direction.SOUTH)

    def getDistanceToIntersection(self, intersection):
        return abs(location.row - intersection.row) + abs(location.column - intersection.column)

    def canFinishRide(self, ride, timeLeft):
        distance = self.getDistanceToIntersection(ride.start_location)
        timeRequired = ride.end_time - ride.start_time

        frames = (distance + time) - timeLeft

        return frames > 0

    def getWeight(self, ride, timeLeft):
        if canFinishRide(ride, timeLeft):
            return 0

        distanceToRide = self.getDistanceToIntersection(ride.start_location)
        timeForRide = ride.end_time - ride.start_time

        return distanceToRide - timeForRide


    def move():
        if (self.drivingQueue != []):
            nextInstruction = self.drivingQueue[0]
            if(snextInstruction == Direction.NORTH):
                moveNorth()
            if(nextInstruction == Direction.EAST):
                moveEast()
            if(nextInstruction == Direction.SOUTH):
                moveSouth()
            if(nextInstruction == Direction.WEST):
                moveWest()

    def moveNorth():
        self.currentLocation.row += 1

    def moveEast():
        self.currentLocation.column += 1
    
    def moveSouth():
        self.currentLocation.row -= 1

    def moveWest():
        self.currentLocation.column -= 1
