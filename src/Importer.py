from src.Ride import Ride
from src.Intersection import Intersection
import os.path

class Importer:
    filename = None

    def __init__(self, filename : str):
        self.filename = filename

    # Read the input from the input file
    def importDataSet(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as file:
                content = file.readlines()

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

                file.close()

                return R, C, F, N, B, T, rides
        else:
            return