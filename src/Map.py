class Map():
    """docstring for Map. take array containing height and width [h,y], it will also take a list of cars """
    height = None
    width = None
    carList = None
    timeFrame = 0

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def nextTimeFrame():
        self.timeFrame += 1
        for car in self.carList:
            car.move()

    def giveCarJob(carID, xAndYCoordinate):
        for car in self.carList:
            if (car.iDNumber == carID):
                car.sendCarToLocation(xAndYCoordinate)
