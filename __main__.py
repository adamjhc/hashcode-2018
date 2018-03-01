#!/bin/env python3

import sys
from src.Ride import Ride
from src.Importer import Importer
from src.Map import Map

if len(sys.argv) < 2:
    print("Usage: __main__.py <dataset> where <dataset> is the path to the desired data set")
    sys.exit()

importer = Importer(sys.argv[1])

rows, columns, cars, numRides, timelyBonus, timeSteps, rides = importer.importDataSet()

print("{} rows, {} columns, {} cars, {} rides, {} starting on time bonus, {} time steps.".format(
    rows, columns, cars, numRides, timelyBonus, timeSteps))

map = Map(rows, columns)

# not sure if works
sortedRides = sorted(rides, key=Ride.startTime)

# map = Map(rows,columns)

# # not sure if works
# sortedRides = sorted(rides, key=Ride.startTime)

# while (map.timeFrame < timeSteps):
#     availableCars = map.getAvailableCars()
#     if(availableCars.length > 0):
#         for ride in sortedRides:
#             if(availableCars.length > 0):
#                 availableCars[0].giveJob()
#                 del availableCars[0]
#             sortedRides.remove(ride)
#     map.nextTimeFrame()

i = 0
for frame in range(timeSteps):
    for car in range(cars):
        if car.isAvailable():
            car.addRide(sortedRides[i])
            i += 1
        else:
            if frame == car.timeWhenAvailable:
                car.update(frame, sortedRides[i])
                i += 1
