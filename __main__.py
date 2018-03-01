#!/bin/env python3

import sys
from src.Importer import Importer

if len(sys.argv) < 2:
    print("Usage: __main__.py <dataset> where <dataset> is the path to the desired data set")
    sys.exit()

importer = Importer(sys.argv[1])

rows, columns, vehicles, numRides, timelyBonus, timeSteps, rides = importer.importDataSet()

print("{} rows, {} columns, {} vehicles, {} rides, {} starting on time bonus, {} time steps.".format(
    rows, columns, vehicles, numRides, timelyBonus, timeSteps))
