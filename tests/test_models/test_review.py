#!/usr/bin/python3
"""Unittest Review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test class Review"""

    def __init__(self, *args, **kwargs):
        """Test allows us to access methods of the base class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test if place_id is a str"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test if user_id is a str"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test if text is a str"""
        new = self.value()
        self.assertEqual(type(new.text), str)
