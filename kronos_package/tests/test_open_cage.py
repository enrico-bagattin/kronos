"""
This module is used to tests open cage module
"""
from unittest import TestCase
from kronos_package.open_cage import get_coordinates, InvalidPlaceError
from opencage.geocoder import InvalidInputError


class TestOpenCage(TestCase):
    def test_wrong_value_type(self):
        """
        Tests the get coordinates function with a wrong type input
        """
        self.assertRaises(InvalidInputError, get_coordinates, 5)

    def test_not_existing_city(self):
        """
        Tests the get coordinates function with a wrong input
        """
        self.assertRaises(InvalidPlaceError, get_coordinates,
                          'IAmDefinitelyANotExistingCity')

    def test_usual_case(self):
        """
        Tests a usual case input
        """
        self.assertIs(type(get_coordinates('Rome')), dict)
