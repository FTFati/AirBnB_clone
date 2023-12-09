#!/usr/bin/python3
"""Defines unittests for console.py"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand_prompt(unittest.TestCase):
    """testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class ConsoleTestCase(unittest.TestCase):
    """testing errors"""

    def check_json(self, classname, id):
        keyname = classname+"."+id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertIn(keyname, saved_data)
        self.assertEqual(saved_data[keyname]["id"], id)
        self.assertEqual(saved_data[keyname]["__class__"], classname)


if __name__ == '__main__':
    unittest.main()
