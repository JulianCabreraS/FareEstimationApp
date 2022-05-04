import unittest

from classes.Point import Point
from classes.Trip import Trip


class TestFareEstimation(unittest.TestCase):
    def test_MinimumFare(self):
        faketrip: Trip = Trip(1, Point(37.96666, 23.728308, 1405594957))
        faketrip.addPoint(Point(37.966627, 23.728263, 1405594966))
        faketrip.recalculateFare()
        self.assertEqual(faketrip.fare, 3.47)

    def test_Validate_Trip_Fare(self):
        faketrip: Trip = Trip(5, Point(37.96666, 23.728308, 1405594957))
        faketrip.addPoint(Point(37.966627, 23.728263, 1405594966))
        faketrip.addPoint(Point(37.966625, 23.728263, 1405594974))
        faketrip.addPoint(Point(37.966613, 23.728375, 1405594984))
        faketrip.addPoint(Point(37.961983, 23.723453,1405595169))
        faketrip.addPoint(Point(37.944328,23.671412,1405595455))
        faketrip.recalculateFare()
        self.assertEqual(faketrip.fare, 7.702377597881236)


if __name__ == '__main__':
    unittest.main()
