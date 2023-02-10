#!/usr/bin/env python3

"""This is the State Module."""
from models import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Implement unittest for State."""

    def setUp(self) -> None:
        """Set up State unittest."""
        self.s1 = State()

    def test_name(self):
        """Test if  State has attribute name."""
        self.assertTrue(hasattr(self.s1, 'name'))

    def test_name_empty(self):
        """Test attribute name is empty."""
        self.assertEqual(self.s1.name, '')

    def test_issubclass_base_model(self):
        """Test if State is subclass of BaseModel."""
        self.assertIsInstance(self.s1, BaseModel)
