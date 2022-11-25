#!/usr/bin/python3
"""Test of Place Class """

from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """ Test Place Class """
    place = Place()

    def test_docstring(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Place.__doc__)

    def test_subinstance(self):
        """Test if it is instance of Place"""
        self.assertIsInstance(self.place, Place)

    def test_attrs(self):
        """ Tests attributes """
        self.assertEqual(hasattr(self.place, "number_bathrooms"), True)
        self.assertEqual(hasattr(self.place, "longitude"), True)
        self.assertEqual(hasattr(self.place, "city_id"), True)
        self.assertEqual(hasattr(self.place, "user_id"), True)
        self.assertEqual(hasattr(self.place, "name"), True)
        self.assertEqual(hasattr(self.place, "latitude"), True)
        self.assertEqual(hasattr(self.place, "number_rooms"), True)
        self.assertEqual(hasattr(self.place, "amenity_ids"), True)
        self.assertEqual(hasattr(self.place, "max_guest"), True)
        self.assertEqual(hasattr(self.place, "price_by_night"), True)
        self.assertEqual(hasattr(self.place, "description"), True)

    def test_type_of_attrs(self):
        """ test type of each attribute into Place Class """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.amenity_ids), list)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.name), str)


if __name__ == '__main__':
    unittest.main()
