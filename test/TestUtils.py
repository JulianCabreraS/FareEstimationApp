import unittest

from utils.Distance import haversine
from utils.FileManagement import checkvalid


class TestUtils(unittest.TestCase):
    def test_check_LatLNg_isValid(self):
        self.assertTrue(checkvalid(30, 30))

    def test_checkN_LatLNg_isNotValid(self):
        self.assertFalse(checkvalid(30, 181))

    def test_haversine(self):
        self.assertEqual(haversine(52.2296756, 21.0122287, 52.406374, 16.9251681), 278.4581750754194)


if __name__ == '__main__':
    unittest.main()
