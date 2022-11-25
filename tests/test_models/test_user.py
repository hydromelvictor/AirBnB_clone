#!/usr/bin/python3
"""Test of User Class """

from models.user import User
import datetime
import unittest
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Test User Class """
    user = User()
    user.name = "Miguel"

    def test_type_of_attrs(self):
        """ Check each attribute and your type """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.last_name), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.password), str)
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_docstring(self):
        """Test docstring into the class"""
        self.assertIsNotNone(User.__doc__)

    def test_subinstance(self):
        """Test inheritance for BaseModel and User"""
        self.assertTrue(isinstance(self.user, User))

    def test_passwd_attr(self):
        """ Tests if exists password attr into User """
        self.assertTrue(hasattr(self.user, 'password'))

    def test_fname_attr(self):
        """ Tests if exists first_name attr into User """
        self.assertTrue(hasattr(self.user, 'first_name'))

    def test_lname_attr(self):
        """ Tests if exists last_name attr into User """
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_inherits_attrs(self):
        """ Tests if class User inherits attributes from BaseModel """
        self.assertTrue(hasattr(self.user, 'name'))
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_email_attr(self):
        """ Tests if exists email attr into User """
        self.assertTrue(hasattr(self.user, 'email'))


if __name__ == '__main__':
    unittest.main()
