from src.Ride import Ride
from src.Intersection import Intersection
import os.path

# Read the input from the input file
def importDataSet(filename):
    if os.path.isfile(filename):
        with open(filename) as f:
            content = f.readlines()

            R, C, F, N, B, T = list(map(int, content[0].split(" ")))

            rides = []

            lines = iter(content)
            next(lines)
            for line in lines:
                a, b, x, y, s, f = list(map(int, line.split(" ")))

                start = Intersection(a, b)
                end = Intersection(x, y)
                ride = Ride(start, end, s, f)
                rides.append(ride)

            return R, C, F, N, B, T, rides
    else:
        return