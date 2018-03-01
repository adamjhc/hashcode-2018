class Map():
    """docstring for Map. take array containing height and width [h,y], it will also take a list of cars """
    heightAndWidth = None
    carList: list = []
    timeFrame: int = 0

<<<<<<< HEAD
    def __init__(self, heightAndWidth, numberOfCars):
        self.heightAndWidth = heightAndWidth
        for i in numberOfCars:
            carList.append(Car(Intersection(0,0), 1)
    def nextTimeFrame():
=======
    def __init__(self, heightAndWidth):
        self.heightAndWidth = heightAndWidth

    def nextTimeFrame(self):
>>>>>>> 5153dce8ff2996600257aab3105b34298e3fc409
        self.timeFrame += 1
        for car in self.carList:
            car.move()

    def giveCarJob(self, carID: int, location: "Location"):
        for car in self.carList:
            if (car.id == carID):
                car.sendCarToLocation(location)
