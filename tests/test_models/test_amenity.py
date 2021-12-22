#!/usr/bin/python3
""" Unittest Amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Test for Amenity class """

    def __init__(self, *args, **kwargs):
        """ Test allows us to access methods of the base class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Checks if is equal to str """
        new = self.value()
        self.assertEqual(type(new.name), str)
