from classes.Trip import Trip
from utils.FileManagement import importfile, writefile

trips: dict = importfile()
for idtrip in trips.keys():
    trip: Trip = trips[idtrip]
    trip.recalculateFare()

writefile(trips)










