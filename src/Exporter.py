import os.path
from typing import List
from src.Car import Car

class Exporter:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.vehicles: List[Car] = []

    def setVehicles(self, vehicles: list) -> None:
        self.vehicles = vehicles

    # Export the output to a file
    def exportSubmission(self) -> None:
        if len(self.vehicles) > 0:
            with open(self.filename, 'w') as file:
                for v in self.vehicles:
                    file.write("{}\n".format(v.getSubmissionLine()))
                    # getSubmissionLine should return a string with the following format:
                    # <n> <ride 1 id> <ride 2 id> ... <ride n id>
                    # So there should be a number, n followed by n integers denoting the ride IDs that the vehicle performs
                file.close()
        else:
            print("No vehicles given to Exporter.")
