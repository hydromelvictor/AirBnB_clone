#!/usr/bin/python3
"""Test of City Class """

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """ Test City Class """
    city = City()

    def test_type_of_attrs(self):
        """ Check each attribute and your type """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_docstring(self):
        """ Test docstring into the class """
        self.assertIsNotNone(City.__doc__)

    def test_subinstance(self):
        """ Test inheritance for BaseModel and City """
        self.assertTrue(isinstance(self.city, City))

    def test_name_attr(self):
        """ Test to check if class has attribute name and state_id """
        self.assertEqual(hasattr(self.city, "name"), True)
        self.assertEqual(hasattr(self.city, "state_id"), True)


if __name__ == '__main__':
    unittest.main()
