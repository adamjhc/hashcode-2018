class Car(object):
    """two """
    coordinates = None
    drivingQueue = []
    def __init__(self, coordinates):
        super(Car, self).__init__()
        self.coordinates = coordinates

    def sendCarToLocation(xAndY):
        xMovement = xAndY[0] - coordinates[0]
        yMovement = yMovement[0] - coordinates[0]
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

    def move():
        if (self.drivingQueue != []):
            if(self.drivingQueue[0] == 1):
                self.coordinates[1] = self.coordinates[1] + 1
            if(self.drivingQueue[0] == 2):
                self.coordinates[0] = self.coordinates[0] + 1
            if(self.drivingQueue[0] == 3):
                self.coordinates[1] = self.coordinates[1] - 1
            if(self.drivingQueue[0] == 4):
                self.coordinates[0] = self.coordinates[0] - 1
