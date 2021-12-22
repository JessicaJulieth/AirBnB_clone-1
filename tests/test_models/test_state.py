#!/usr/bin/python3
"""State class unitTest"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test class for State"""

    def __init__(self, *args, **kwargs):
        """Test allows us to access methods of the base class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test if name 3 is a string"""
        new = self.value()
        self.assertEqual(type(new.name), str)
