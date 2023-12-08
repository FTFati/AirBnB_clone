#!/usr/bin/python3
"""
Unit test for BaseModel
"""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from io import StringIO
import sys

class TestBaseModel(unittest.TestCase):
    """
    Tests attributes of the base model
    """

    def test_basic(self):
        """First test"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    def set_Up(self):
        """Second test"""
        pass

    def test_datetime(self):
        """Third test"""
        pass
    
    def test_datetime(self):
        """Fourth test"""
        pass


if __name__ == '__main__':
    unittest.main()
