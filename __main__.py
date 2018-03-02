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
            if not car.isAvailable(frame):
                # Nothing to do if the car is in transit
                continue

            currentRide: "Ride" = car.ride

            if i < len(rides):
                j: int = 0
                nextRide: "Ride" = rides[i]

                # Don't take a ride which the car cannot complete in time
                while frame + nextRide.distance() > timeSteps or frame + nextRide.distance() > nextRide.endTime:
                    j += 1
                    if i + j < len(rides):
                        nextRide: "Ride" = rides[i+j]
                    else:
                        nextRide: "Ride" = None
                        break

                if nextRide is not None:
                    if j > 0:
                        # swap rides[i] with rides[i+j]
                        swapRide: "Ride" = rides[i]
                        rides[i] = rides[i+j]
                        rides[i+j] = swapRide
                    i += 1

                car.update(frame, nextRide)

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
