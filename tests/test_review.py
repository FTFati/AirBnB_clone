#!/usr/bin/python3
"""Test module for Review Class"""
from models.review import Review
import unittest


class Test_Review(unittest.TestCase):
    """review test class"""

    def Test_initialisation(self):

        Rv = Review()
        self.assertEqual("", Rv.place_id)
        self.assertEqual("", Rv.text)
        self.assertEqual("", Rv.user_id)

    def Test_inherited_attributes(self):

        Rv = Review()
        self.assertTrue(hasattr(Rv, "id"))
        self.assertTrue(hasattr(Rv, "created_at"))
        self.assertTrue(hasattr(Rv, "updated_at"))


if __name__ == "__main__":
    unittest.main()
