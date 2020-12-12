"""
This module is used to tests our air quality module (that uses air_quality.csv)
"""
from unittest import TestCase
from kronos_package.air_quality import get_air_quality


class TestAirQuality(TestCase):
    def test_wrong_value_type(self):
        """
        Tests the air quality function with a wrong type input
        """
        res = get_air_quality(5)
        self.assertEqual(res, 'n.d.')

    def test_no_city(self):
        """
        Tests the air quality function with None as input
        """
        res = get_air_quality(None)
        self.assertEqual(res, 'n.d.')

    def test_right_input(self):
        """
        Tests the air quality function with a real case input, the result is
        tested using a regex. The regex will match any strings starting with any
        charter (the coloured circle emoji) a space and than a float number
        """
        res = get_air_quality("Roma")
        self.assertRegex(res, ".\s([0-9]*[.])?[0-9]+")
