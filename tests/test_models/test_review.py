#!/usr/bin/env python3

"""This is the Review Module."""
from models import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Implement unittest for Review."""

    def setUp(self) -> None:
        """Set up Review unittest."""
        self.r1 = Review()

    def test_text(self):
        """Test if  Review has attribute text."""
        self.assertTrue(hasattr(self.r1, 'text'))

    def test_text_empty(self):
        """Test attribute text is empty."""
        self.assertEqual(self.r1.text, '')

    def test_user_id(self):
        """Test if  Review has attribute user_id."""
        self.assertTrue(hasattr(self.r1, 'user_id'))

    def test_user_id_empty(self):
        """Test attribute user_id is empty."""
        self.assertEqual(self.r1.user_id, '')

    def test_place_id(self):
        """Test if  Review has attribute place_id."""
        self.assertTrue(hasattr(self.r1, 'place_id'))

    def test_place_id_empty(self):
        """Test attribute place_id is empty."""
        self.assertEqual(self.r1.place_id, '')

    def test_issubclass_base_model(self):
        """Test if Review is subclass of BaseModel."""
        self.assertIsInstance(self.r1, BaseModel)
