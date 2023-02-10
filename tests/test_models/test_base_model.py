#!/usr/bin/env python3

import unittest
from datetime import datetime as dtime
from models import base_model

"""Base Model Unittest Module."""


class TestBaseModel(unittest.TestCase):
    """Represent the test model for Base Model."""

    def setUp(self):
        self.b1 = base_model.BaseModel()
        self.b2 = base_model.BaseModel()
        self.objs_dict = self.b1.to_dict()
        self.created_at = self.objs_dict['created_at']
        self.updated_at = self.objs_dict['updated_at']
        self.objs = self.b1.__dict__.copy()
        self.objs['__class__'] = self.b1.__class__.__name__
        self.objs['created_at'] = self.objs['created_at'].isoformat()
        self.objs['updated_at'] = self.objs['updated_at'].isoformat()
        self.b1.save()
        self.obj = self.b1.to_dict()
        self.update = self.obj['updated_at']
        self.create = self.obj['created_at']
        self.to_str = f'[BaseModel] ({self.b1.id}) {self.b1.__dict__}'

    def test_id(self):
        """Test if id is unique."""
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_dict_created_at(self):
        """Test if created_at is a str."""
        self.assertIsInstance(self.created_at, str)

    def test_dict_updated_at(self):
        """Test if updated_at is a str."""
        self.assertIsInstance(self.updated_at, str)

    def test_to_dict(self):
        """Test if to_dict return a dict."""
        self.assertIsInstance(self.objs_dict, dict)

    def test_class_name(self):
        """Test if __class__ is in dict return by to_dict."""
        self.assertIn("__class__", self.objs_dict.keys())

    def test_dtime_updated_at(self):
        """Test if updated_at is a datetime."""
        self.assertIsInstance(self.b1.updated_at, dtime)

    def test_dtime_created_at(self):
        """Test if updated_at is a datetime."""
        self.assertIsInstance(self.b1.created_at, dtime)

    def test_dtime_updated_at_on_save(self):
        """Test if updated_at is a updated on save."""
        self.assertNotEqual(self.update, self.updated_at)

    def test_dtime_created_at_on_save(self):
        """Test if created_at is a updated on save."""
        self.assertEqual(self.create, self.created_at)

    def test_inst_is_base_model(self):
        """Test if b1 is instance of BaseModel."""
        self.assertIsInstance(self.b1, base_model.BaseModel)

    def test_id_is_str(self):
        """Test if id is a str."""
        self.assertIsInstance(self.b1.id, str)

    def test_dict(self):
        """
        Test if instance.__dict.__ plus.
        __class__ : instance class_name equal to_dict.
        """
        self.assertEqual(self.objs, self.objs_dict)

    def test_to_str(self):
        """Test __str__ method of BaseModel."""
        self.assertEqual(self.to_str, str(self.b1))
