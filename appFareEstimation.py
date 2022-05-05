from classes.Trip import Trip
from utils.FileManagement import readfile, writefile


def fareEstimation():
    trips: dict = readfile()

    if not (trips is None):
        for idtrip in trips.keys():
            trip: Trip = trips[idtrip]
            trip.recalculateFare()

        writefile(trips)
    else:
        print("No valid values were found in the file. Review the input file.")


if __name__ == '__main__':
    fareEstimation()
