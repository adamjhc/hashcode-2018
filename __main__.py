#!/bin/env python3

import sys
from src.ImportDataSet import read_input

if len(sys.argv) > 0:
    R, C, F, N, B, T, rides = read_input(sys.argv[0])