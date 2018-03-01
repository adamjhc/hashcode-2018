#!/bin/env python3

import sys

from src.Importer import Importer
from src.Ride import Ride
from src.Car import Car

if len(sys.argv) < 2:
    print("Usage: __main__.py <dataset> where <dataset> is the path to the desired data set")
    sys.exit()

importer = Importer(sys.argv[1])

rows, columns, numCars, numRides, timelyBonus, timeSteps, rides = importer.importDataSet()

print("""{} rows
{} columns
{} cars
{} rides
{} starting on time bonus
{} time steps
""".format(rows, columns, numCars, numRides, timelyBonus, timeSteps))

rides.sort(key=lambda ride: ride.startTime, reverse=True)

cars = []

for car in range(numCars):
    cars.append(Car())

i = 0
for frame in range(timeSteps):
    for car in cars:
        if car.update(frame, rides[i]):
            i += 1

for car in cars:
    print(car.previousRides)
