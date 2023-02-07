#!/usr/bin/env python3

"""Test suit for BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class"""

    def setUp(self):
        """setup method for unittest"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()
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
        """Test for unique id"""
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_id_is_str(self):
        """Test type of id (str)"""
        self.assertIsInstance(self.b1.id, str)

