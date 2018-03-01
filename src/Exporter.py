import os.path

class Exporter:
    filename: str
    vehicles: list

    def __init__(self, filename: str):
        self.filename = filename
        self.vehicles = []

    def setVehicles(self, vehicles: list):
        self.vehicles = vehicles

    # Export the output to a file
    def exportSubmission(self):
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
