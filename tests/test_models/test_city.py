#!/usr/bin/env python3
"""This is the City Module."""
from models import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Implement unittest for City."""

    def setUp(self) -> None:
        """Set up City unittest."""
        self.c1 = City()

    def test_name(self):
        """Test if  City has attribute name."""
        self.assertTrue(hasattr(self.c1, 'name'))

    def test_name_empty(self):
        """Test attribute name is empty."""
        self.assertEqual(self.c1.name, '')

    def test_state_id(self):
        """Test if  City has attribute state_id."""
        self.assertTrue(hasattr(self.c1, 'state_id'))

    def test_state_id_empty(self):
        """Test attribute state_id is empty."""
        self.assertEqual(self.c1.state_id, '')

    def test_issubclass_base_model(self):
        """Test if City is subclass of BaseModel."""
        self.assertIsInstance(self.c1, BaseModel)
