#!/usr/bin/python3
"""module unit tests for the console.py file"""
from console import HBNBCommand
import unittest
from io import StringIO


class Test_Console(unittest.TestCase):
    """
    Test cases for HBNBCommand console (console.py).
    """

    def setUp(self):
        """Set up test cases"""
        self.console = HBNBCommand()
        self.output = StringIO()

    def tearDown(self):
        """Clean up test cases"""
        self.output.close()

    def test_quit(self):
        """Test the quit command"""
        self.assertTrue(self.console.onecmd('quit'))

    def test_eof(self):
        """Test the EOF (ctrl+D) command"""
        self.assertTrue(self.console.onecmd('EOF'))

    def test_emptyline(self):
        """Test for the empty line input"""
        self.assertIsNone(self.console.onecmd(''))


if __name__ == '__main__':
    unittest.main()
