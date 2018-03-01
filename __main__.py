#!/bin/env python3

import sys
from src.Import import importDataSet

if len(sys.argv) < 2:
    print("Usage: __main__.py <dataset> where <dataset> is the path to the desired data set")
    sys.exit()

rows, columns, vehicles, rides, timelyBonus, timeSteps, rides = importDataSet(sys.argv[1])

print("{} rows, {} columns, {} vehicles, {} rides, {} starting on time bonus, {} time steps.".format(rows, columns, vehicles, rides, timelyBonus, timeSteps))
