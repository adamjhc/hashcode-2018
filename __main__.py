#!/bin/env python3

"""
For a specific dataset use:
$ __main__.py <dataset> <outfile>
where
 - <dataset> is the path to the desired input data set file
 - <outfile> is the path to the output file
"""

import sys
from src.Importer import Importer
from src.Exporter import Exporter
from src.Car import Car

datasets: dict

if len(sys.argv) < 3:
    datasets = {
        "./inputsets/a_example.in": "./submissions/a_example.out",
        "./inputsets/b_should_be_easy.in": "./submissions/b_should_be_easy.out",
        "./inputsets/c_no_hurry.in": "./submissions/c_no_hurry.out",
        "./inputsets/d_metropolis.in": "./submissions/d_metropolis.out",
        "./inputsets/e_high_bonus.in": "./submissions/e_high_bonus.out"
    }
else:
    datasets = {
        sys.argv[1]: sys.argv[2]
    }

for infile in datasets.keys():
    outfile: str = datasets[infile]

    print()
    print()
    print("------------------------------------------------------------")
    print()
    print()
    print("Running on dataset: {}".format(infile))

    importer: "Importer" = Importer(infile)

    rows, columns, numCars, numRides, timelyBonus, timeSteps, rides = importer.importDataSet()

    print("""Metadata:
\t{} rows
\t{} columns
\t{} cars
\t{} rides
\t{} starting on time bonus
\t{} time steps""".format(rows, columns, numCars, numRides, timelyBonus, timeSteps))

    rides.sort(key=lambda ride: (ride.startTime, ride.distance()), reverse=False)

    cars = []

    for car in range(numCars):
        cars.append(Car())

    i = 0
    for frame in range(timeSteps):
        for index, car in enumerate(cars):
            if i > len(rides) - 1:
                break
            if car.update(frame, rides[i]):
                i += 1

    print("Outputting to {}".format(outfile))
    exporter = Exporter(outfile)
    exporter.setVehicles(cars)
    exporter.exportSubmission()
