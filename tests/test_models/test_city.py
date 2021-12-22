#!/usr/bin/python3
"""Unittest City"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Test class for Cit"""

    def __init__(self, *args, **kwargs):
        """Test allows us to access methods of the base class """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test type of obj_City"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test type of obj_City is a str"""
        new = self.value()
        self.assertEqual(type(new.name), str)
