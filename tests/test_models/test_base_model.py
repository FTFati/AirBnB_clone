#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for BaseModel unittest
"""
import os
import unittest
from models.base_model import BaseModel



class TestBasemodel(unittest.TestCase):
    """
    Unittest for BaseModel
    """

    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
    def test_init(self):
        """
        Test for init
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Test for save method
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        current_updated_at = my_model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.created_at.isoformat())


    def test_str(self):
        """
        Test for string representation
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))
=======
"""Unnitest Module for (Basemodel class)"""
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Testing the TestBaseModel Class"""

    def test_init_attributes(self):
        """checks for init attributes"""

        B_m = BaseModel()
        self.assertTrue(hasattr(B_m, 'id'))
        self.assertTrue(hasattr(B_m, 'created_at'))
        self.assertTrue(hasattr(B_m, 'updated_at'))

    def test_init_with_kwargs(self):
        """checks for init attribute with kwargs"""

        D_t = datetime.today()
        dt_iso = D_t.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, D_t)
        self.assertEqual(bm.updated_at, D_t)

    def test_unique_id(self):
        """checks if ids are unique"""

        B_m1 = BaseModel()
        B_m2 = BaseModel()
        self.assertNotEqual(B_m1.id, B_m2.id)

    def test_string_representation(self):
        """checks string representation of instance"""

        B_m = BaseModel()
        B_m.id = "123456"
        bm_str = str(B_m)
        self.assertIn("[BaseModel] (123456)", bm_str)
        self.assertIn("'id': '123456'", bm_str)
        self.assertIn("'created_at': ", bm_str)
        self.assertIn("'updated_at': ", bm_str)

    def test_save(self):
        """test the save instance"""

        B_m = BaseModel()
        original_updated_at = B_m.updated_at
        B_m.save()
        self.assertNotEqual(original_updated_at, B_m.updated_at)

    def test_to_dict_attr(self):
        """test to dictionary attributes"""

        B_m = BaseModel()
        B_m.name = "Test Model"
        B_m.number = 100
        bm_dict = B_m.to_dict()
        self.assertIn('id', bm_dict)
        self.assertIn('created_at', bm_dict)
        self.assertIn('updated_at', bm_dict)
        self.assertIn('__class__', bm_dict)
        self.assertIn('name', bm_dict)
        self.assertIn('number', bm_dict)

    def test_to_dict_str_attr(self):
        """test dictionary strings"""

        B_m = BaseModel()
        bm_dict = B_m.to_dict()
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)
        self.assertNotIsInstance(bm_dict['created_at'], datetime)
        self.assertNotIsInstance(bm_dict['updated_at'], datetime)
>>>>>>> 6a5724425c5a7e0f6e96304e0db051f9e399b7f3


if __name__ == "__main__":
    unittest.main()
