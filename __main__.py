#!/bin/env python3

"""
For a specific dataset use:
$ __main__.py <dataset> <outfile>
where
 - <dataset> is the path to the desired input data set file
 - <outfile> is the path to the output file
"""

import sys
from typing import Dict, List, Tuple
from src.Importer import Importer
from src.Exporter import Exporter
from src.Car import Car
from src.Ride import Ride

datasets: Dict[str, str]

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

    cars: List[Car] = [Car() for _ in range(numCars)]

    score: int = 0
    i: int = 0
    for frame in range(timeSteps):
        for index, car in enumerate(cars):
            if i < len(rides):
                nextRide: "Ride" = rides[i]
            else:
                nextRide: "Ride" = None

            currentRide: "Ride" = car.ride

            if car.update(frame, nextRide):
                i += 1

                # Scoring
                if currentRide is not None and frame < currentRide.endTime:
                    score += currentRide.distance()
                    if frame - currentRide.distance() == currentRide.startTime:
                        score += timelyBonus

    print("Score: {:d}".format(score))
    print("Outputting to {}".format(outfile))
    exporter = Exporter(outfile)
    exporter.setVehicles(cars)
    exporter.exportSubmission()
