class Map(object):
    """docstring for Map. take array containing height and width [h,y], it will also take a list of cars """
    heightAndWidth = None
    carList = None
    timeFrame = 0
    def __init__(self, heightAndWidth):
        self.heightAndWidth = heightAndWidth


    def nextTimeFrame():
        self.timeFrame += 1
        for car in self.carList:
            car.move()

    def giveCarJob(carID, xAndYCoordinate):
        for car in self.carList:
            if (car.iDNumber == carID):
                car.sendCarToLocation(xAndYCoordinate)
