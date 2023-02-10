#!/usr/bin/env python3
"""File storage Unittest module"""

from models import FileStorage
from models import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """Implement unittest for FileStorage"""
    def setUp(self):
        """Set up File storage unittest"""
        self.storage = FileStorage()
        self.base = BaseModel()
        self.storage.new(self.base)

    def test_all(self):
        """Test if the all method returns a dict"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test if new method adds new object to __objects"""
        self.assertIsNotNone(self.storage.all())
