#!/usr/bin/env python3

"""This is the Place Module."""
from models import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Implement unittest for Place."""

    def setUp(self) -> None:
        """Set up Place unittest."""
        self.p1 = Place()

    def test_name(self):
        """Test if  Place has attribute name."""
        self.assertTrue(hasattr(self.p1, 'name'))

    def test_name_empty(self):
        """Test attribute name is empty."""
        self.assertEqual(self.p1.name, '')

    def test_description(self):
        """Test if  Place has attribute description."""
        self.assertTrue(hasattr(self.p1, 'description'))

    def test_description_empty(self):
        """Test attribute description is empty."""
        self.assertEqual(self.p1.description, '')

    def test_number_rooms(self):
        """Test if  Place has attribute number_rooms."""
        self.assertTrue(hasattr(self.p1, 'number_rooms'))

    def test_number_rooms_zero(self):
        """Test attribute number_rooms is zero."""
        self.assertEqual(self.p1.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test if  Place has attribute number_bathrooms."""
        self.assertTrue(hasattr(self.p1, 'number_bathrooms'))

    def test_number_bathroomsrooms_zero(self):
        """Test attribute number_bathrooms is zero."""
        self.assertEqual(self.p1.number_bathrooms, 0)

    def test_max_guest(self):
        """Test if  Place has attribute max_guest."""
        self.assertTrue(hasattr(self.p1, 'max_guest'))

    def test_max_guest_zero(self):
        """Test attribute max_guest is zero."""
        self.assertEqual(self.p1.max_guest, 0)

    def test_price_by_night(self):
        """Test if  Place has attribute price_by_night."""
        self.assertTrue(hasattr(self.p1, 'price_by_night'))

    def test_price_by_night_zero(self):
        """Test attribute price_by_night is zero."""
        self.assertEqual(self.p1.price_by_night, 0)

    def test_longitude(self):
        """Test if  Place has attribute longitude."""
        self.assertTrue(hasattr(self.p1, 'longitude'))

    def test_longitude_zero(self):
        """Test attribute longitude is zero."""
        self.assertEqual(self.p1.longitude, 0.0)

    def test_latitude(self):
        """Test if  Place has attribute latitude."""
        self.assertTrue(hasattr(self.p1, 'latitude'))

    def test_latitude_zero(self):
        """Test attribute latitude is zero."""
        self.assertEqual(self.p1.latitude, 0.0)

    def test_user_id(self):
        """Test if  Place has attribute user_id."""
        self.assertTrue(hasattr(self.p1, 'user_id'))

    def test_user_id_empty(self):
        """Test attribute user_id is empty."""
        self.assertEqual(self.p1.user_id, '')

    def test_city_id(self):
        """Test if  Place has attribute city_id."""
        self.assertTrue(hasattr(self.p1, 'city_id'))

    def test_city_id_empty(self):
        """Test attribute city_id is empty."""
        self.assertEqual(self.p1.city_id, '')

    def test_amenity_ids(self):
        """Test if  Place has attribute amenity_ids."""
        self.assertTrue(hasattr(self.p1, 'amenity_ids'))

    def test_amenity_ids_empty(self):
        """Test attribute amenity_ids is empty list."""
        self.assertEqual(self.p1.amenity_ids, [])

    def test_issubclass_base_model(self):
        """Test if Place is subclass of BaseModel."""
        self.assertIsInstance(self.p1, BaseModel)
