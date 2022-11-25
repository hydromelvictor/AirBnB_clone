#!/usr/bin/python3
"""Test of Review Class """

from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """ Test Review Class """
    review = Review()

    def test_docstring(self):
        """Test docstring for Review class"""
        self.assertIsNotNone(Review.__doc__)

    def test_instance_Review(self):
        """Test if it is instance of Review"""
        self.assertIsInstance(self.review, Review)

    def test_attr_cls(self):
        """ check for attributes into the class Review """
        self.assertEqual(hasattr(self.review, "text"), True)
        self.assertEqual(hasattr(self.review, "place_id"), True)
        self.assertEqual(hasattr(self.review, "user_id"), True)

    def test_type_of_attrs(self):
        """ check each attribute validating by type """
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)


if __name__ == '__main__':
    unittest.main()
