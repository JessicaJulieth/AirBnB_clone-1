#!/usr/bin/python3
"""Unittest place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test class for Place"""

    def __init__(self, *args, **kwargs):
        """Test allows us to access methods of the base class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test if city id is a str"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test if user id is a str"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test if name is a str"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test if description is a str"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test if number_rooms is a int"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Test if number bathtooms is a int"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Test if max guest is a int"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Test if price by night is a int"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Test if latitude is a float"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Test if longitude is a float"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Test if amenity ids is a list"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
