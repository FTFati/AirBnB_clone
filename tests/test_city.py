#!/usr/bin/python3
"""Test module for City Class"""
from models.city import City
import unittest


class Test_City(unittest.TestCase):
    """Test cases for city class"""

    def Test_initialisation(self):

        Ct = City()
        self.assertEqual("", City.name)
        self.assertEqual("", City.state_id)

    def Test_assignments(self):

        Ct = City()
        Ct.state_id = "123456"
        Ct.name = "Morocco"
        self.assertEqual("123456", Ct.state_id)
        self.assertEqual("Morocco", Ct.name)

    def Test_inherited_attributes(self):

        Ct = City()
        self.assertTrue(hasattr(Ct, "id"))
        self.assertTrue(hasattr(Ct, "created_at"))
        self.assertTrue(hasattr(Ct, "updated_at"))


if __name__ == "__main__":
    unittest.main()
