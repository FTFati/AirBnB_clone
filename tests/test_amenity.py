#!/usr/bin/python3
"""Test Amenity module"""
from models.amenity import Amenity
import unittest


class Test_Amenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def Test_Initialisation(self):
        """Test initialisation"""

        AM = Amenity()
        self.assertEqual("", AM.name)

    def Test_Assignments(self):
        """Test assignments"""

        AM = Amenity()
        AM.name = "Morocco"
        self.assertEqual("Morocco", AM.name)

    def Test_inherited_attributes(self):
        """test inherited attributes"""

        AM = Amenity()
        self.assertTrue(hasattr(AM, "id"))
        self.assertTrue(hasattr(AM, "created_at"))
        self.assertTrue(hasattr(AM, "updated_at"))

    def Test_representation_str(self):
        AM = Amenity()
        AM.id = "12345"
        AM.name = "WIWI"
        amenity_str = (
                "[Amenity] (12345) {'id': '123', 'created_at': " +
                repr(AM.created_at) + ", 'updated_at': " +
                repr(AM.updated_at) + ", 'name': 'WIWI'}"
                )
        self.assertEqual(amenity_str, str(AM))


if __name__ == "__main__":
    unittest.main()
