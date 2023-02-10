#!/usr/bin/env python3

import unittest
from datetime import datetime as dtime
from models import user, BaseModel

"""User Model Unittest Module."""


class TestBaseModel(unittest.TestCase):
    """Represent the test model for User Model."""

    def setUp(self):
        self.u1 = user.User()
        self.u2 = user.User()
        self.objs_dict = self.u1.to_dict()
        self.created_at = self.objs_dict['created_at']
        self.updated_at = self.objs_dict['updated_at']
        self.objs = self.u1.__dict__.copy()
        self.objs['__class__'] = self.u1.__class__.__name__
        self.objs['created_at'] = self.objs['created_at'].isoformat()
        self.objs['updated_at'] = self.objs['updated_at'].isoformat()
        self.u1.save()
        self.obj = self.u1.to_dict()
        self.update = self.obj['updated_at']
        self.create = self.obj['created_at']

    def test_id(self):
        """Test if id is unique."""
        self.assertNotEqual(self.u1.id, self.u2.id)

    def test_email(self):
        """Test if email exist."""
        self.assertTrue(hasattr(self.u1, 'email'))

    def test_email_empty(self):
        """Test if email is empty."""
        self.assertEqual(self.u1.email, '')

    def test_password(self):
        """Test if password exist."""
        self.assertTrue(hasattr(self.u1, 'password'))

    def test_password_empty(self):
        """Test if password is empty."""
        self.assertEqual(self.u1.password, '')

    def test_names(self):
        """Test if first and last names exist."""
        self.assertTrue(hasattr(self.u1, 'first_name'))
        self.assertTrue(hasattr(self.u1, 'last_name'))

    def test_names_empty(self):
        """Test if first and last names are empty."""
        self.assertEqual(self.u1.first_name, '')
        self.assertEqual(self.u1.last_name, '')

    def test_to_dict(self):
        """Test if to_dict return a dict."""
        self.assertIsInstance(self.objs_dict, dict)

    def test_class_name(self):
        """Test if __class__ is in dict return by to_dict."""
        self.assertIn("__class__", self.objs_dict.keys())

    def test_inst_is_base_model(self):
        """Test if u1 is instance of BaseModel."""
        self.assertIsInstance(self.u1, BaseModel)

    def test_id_is_str(self):
        """Test if id is a str."""
        self.assertIsInstance(self.u1.id, str)

    def test_dict(self):
        """
        Test if instance.__dict.__ plus.
        __class__ : instance class_name equal to_dict.
        """
        self.assertEqual(self.objs, self.objs_dict)
