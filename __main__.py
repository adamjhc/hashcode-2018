#!/bin/env python3

import sys

from src.Importer import Importer
from src.Exporter import Exporter
from src.Car import Car
from src.Map import Map

if len(sys.argv) < 3:
    print("Usage: __main__.py <dataset> <outfile> where <dataset> is the path to the desired data set and <outfile> is the path to the output")
    sys.exit()

importer = Importer(sys.argv[1])

rows, columns, numCars, numRides, timelyBonus, timeSteps, rides = importer.importDataSet()

print("{} rows, {} columns, {} cars, {} rides, {} starting on time bonus, {} time steps.".format(
    rows, columns, numCars, numRides, timelyBonus, timeSteps))

rides.sort(key=lambda ride: ride.startTime, reverse=True)

# map = Map(rows,columns)

# while (map.timeFrame < timeSteps):
#     availableCars = map.getAvailableCars()
#     if(availableCars.length > 0):
#         for ride in sortedRides:
#             if(availableCars.length > 0):
#                 availableCars[0].giveJob()
#                 del availableCars[0]
#             sortedRides.remove(ride)
#     map.nextTimeFrame()

cars = []

for car in range(numCars):
    cars.append(Car())

for frame in range(timeSteps):
    for i, car in enumerate(cars):
        car.update(frame, rides[i])

exporter = Exporter(sys.argv[2])
exporter.setVehicles(cars)
exporter.exportSubmission()
