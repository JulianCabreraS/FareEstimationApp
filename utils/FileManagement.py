import csv
from classes.Trip import Trip, Point


# Validation of latitude and longitude
def checkvalid(lat, lng):
    return -90 <= lat <= 90 and -180 <= lng <= 180


def readfile():
    trips = {}
    try:
        with open('./files/paths.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                idtrip = int(row[0])
                lat = float(row[1])
                lng = float(row[2])
                timestamp = int(row[3])

                newpoint = Point(lat, lng, timestamp)
                if idtrip in trips:
                    temptrip: Trip = trips[idtrip]
                    temptrip.addPoint(newpoint)
                    trips[idtrip] = temptrip
                else:
                    trips[idtrip] = Trip(idtrip, newpoint)

            return trips
    except IOError:
        print("File not found.")
    except csv.Error:
        print("Incorrect data found.")
    except ValueError as ex:
        print("The application found incorrect information.")


def writefile(data: dict):
    try:
        with open('./files/output.csv', mode='w', encoding='UTF8', newline='') as csv_file:
            trip_writer = csv.writer(csv_file)
            print('id_ride', 'fare_estimate')
            for idtrip in data.keys():
                trip: Trip = data[idtrip]
                trip_writer.writerow([trip.tripid, "{:.2f}".format(trip.fare)])
                print("id_ride: {} fare_estimate: {:.2f} Record Written".format(trip.tripid, trip.fare))
    except IOError:
        print("Writer cannot open or write the file.")
