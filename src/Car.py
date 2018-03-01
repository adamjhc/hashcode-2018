class Car(object):
    """two """
    currentLocation = None
    drivingQueue = []
    iDNumber = None

    def __init__(self, location, iDNumber):
        self.currentLocation = location
        self.iDNumber = iDNumber

    def sendCarToLocation(end_location):
        xMovement = endLocation.x - self.currentLocation.x
        yMovement = endLocation.y - self.currentLocation.y
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
            # drive north
            if(self.drivingQueue[0] == 1):
                self.coordinates[1] = self.coordinates[1] + 1

            # drive east
            if(self.drivingQueue[0] == 2):
                self.coordinates.x = self.coordinates.x + 1

            # drive south
            if(self.drivingQueue[0] == 3):
                self.coordinates[1] = self.coordinates[1] - 1

            # drive west
            if(self.drivingQueue[0] == 4):
                self.coordinates.x = self.coordinates.x - 1
