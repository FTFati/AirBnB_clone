#!/usr/bin/python3
"""Test module for State Class"""
from models.state import State
import unittest


class Test_State(unittest.TestCase):
    """state test class"""

    def Test_initialisation(self):

        St = State()
        self.assertEqual("", St.name)

    def Test_inherited_attributes(self):

        St = State()
        self.assertTrue(hasattr(St, "id"))
        self.assertTrue(hasattr(St, "created_at"))
        self.assertTrue(hasattr(St, "updated_at"))


if __name__ == "__main__":
    unittest.main()
