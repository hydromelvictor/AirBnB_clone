#!/usr/bin/python3
"""Test of Amenity Class """

from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """ Test Amenity Class """
    amenity = Amenity()

    def test_type_of_attrs(self):
        """ Check each attribute and your type """
        self.assertEqual(type(self.amenity.name), str)

    def test_docstring(self):
        """Test docstring into the class"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_subinstance(self):
        """Test inheritance from BaseModel and Amenity"""
        self.assertTrue(isinstance(self.amenity, Amenity))

    def test_name_attr(self):
        """ Test to check if class has attribute name """
        self.assertEqual(hasattr(self.amenity, "name"), True)


if __name__ == '__main__':
    unittest.main()
