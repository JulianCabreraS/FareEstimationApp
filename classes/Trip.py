import operator
import time
from utils.Distance import haversine
import utils.constant


class Point:
    def __init__(self, newlat, newlng, newtimestamp):
        self.lat = newlat
        self.lng = newlng
        self.timestamp = newtimestamp
        self.speed = 0.0
        self.fare = 0.0

    def __str__(self):
        return f' [Point: {self.lat}, {self.lng} Timestamp: {self.timestamp} Speed: {self.speed}] '


class Trip:

    def __init__(self, newtripid, newpoint):
        self.tripid = newtripid
        self.points = [newpoint]
        self.filteredPoints = [newpoint]
        self.fare = 0

    def addPoint(self, point: Point):
        self.points.append(point)

    def orderPoints(self):
        nestlist = sorted(self.points, key=operator.itemgetter(1))
        self.points = nestlist

    def recalculateFare(self):

        self.points.sort(key=lambda x: x.timestamp)

        origin: Point = self.points[0]
        self.filteredPoints.append(origin)
        for index in range(1, len(self.points)):
            destination: Point = self.points[index]
            distance = haversine(origin.lat, origin.lng, destination.lat, destination.lng)
            hours = (destination.timestamp - origin.timestamp) / 3600

            if hours == 0:
                destination.speed = 101
            else:
                destination.speed = distance / hours

            if destination.speed < 100:

                if destination.speed <= 10:
                    destination.fare = hours * utils.constant.IDLE_FARE
                else:
                    result = time.localtime(destination.timestamp)
                    if 0 < result.tm_hour < 5:
                        destination.fare = distance * utils.constant.MORNING_FARE
                    else:
                        destination.fare = distance * utils.constant.ALLDAY_FARE
                self.filteredPoints.append(destination)
                self.fare = self.fare + destination.fare

                origin: Point = self.points[index]

    def __str__(self):
        return f'Idtrip: {self.tripid} : \nFare = {self.fare} \nPoints:\n  {[str(point) for point in self.filteredPoints]}'

    def printFilterPoints(self):
        print(f'Idtrip: {self.tripid} : \nFare = {self.fare}')
        for point in self.filteredPoints:
            print(str(point))

    def printPoints(self):
        print(f'Idtrip: {self.tripid} : \nFare = {self.fare}')
        for point in self.points:
            print(str(point))
