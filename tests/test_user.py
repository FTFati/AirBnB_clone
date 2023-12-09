#!/usr/bin/python3
"""Test module for User Class"""
from models.user import User
import unittest


class Test_User(unittest.TestCase):
    """user test class"""

    def Test_initialisation(self):

        Us = User()
        self.assertEqual("", Us.email)
        self.assertEqual("", Us.password)
        self.assertEqual("", Us.first_name)
        self.assertEqual("", Us.last_name)

    def Test_inherited_attributes(self):

        Us = User()
        self.assertTrue(hasattr(Us, "id"))
        self.assertTrue(hasattr(Us, "created_at"))
        self.assertTrue(hasattr(Us, "updated_at"))


if __name__ == "__main__":
    unittest.main()
