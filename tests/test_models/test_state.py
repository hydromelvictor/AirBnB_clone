#!/usr/bin/python3
"""Test of State Class """

from models.state import State
import unittest


class TestState(unittest.TestCase):
    """ Test State Class """
    state = State()

    def test_docstring(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(State.__doc__)

    def test_instance_State(self):
        """Check if obj is instance of State"""
        self.assertIsInstance(self.state, State)

    def test_attr_cls(self):
        """ Check if exists attributes into State class """
        self.assertEqual(hasattr(self.state, "name"), True)

    def test_type_of_attrs(self):
        """ Check each attribute and validates your type """
        self.assertEqual(type(self.state.name), str)


if __name__ == '__main__':
    unittest.main()
