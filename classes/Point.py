class Point:
    def __init__(self, newlat, newlng, newtimestamp):
        self.lat = newlat
        self.lng = newlng
        self.timestamp = newtimestamp
        self.speed = 0.0
        self.fare = 0.0

    def __str__(self):
        return f' [Point: {self.lat}, {self.lng} Timestamp: {self.timestamp} Speed: {self.speed}] '
