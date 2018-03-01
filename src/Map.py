class Map():
    """docstring for Map. take array containing height and width [h,y], it will also take a list of cars """
    heightAndWidth = None
    carList: list = []
    timeFrame: int = 0

    def __init__(self, heightAndWidth, numberOfCars):
        self.heightAndWidth = heightAndWidth
        for i in numberOfCars:
            carList.append(Car(Intersection(0,0), 1)
    def nextTimeFrame():
        self.timeFrame += 1
        for car in self.carList:
            car.move()

    def giveCarJob(self, carID: int, location: "Location"):
        for car in self.carList:
            if (car.id == carID):
                car.sendCarToLocation(location)
