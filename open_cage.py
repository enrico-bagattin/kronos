"""
This module is used to retrieve coordinates data from the OpenCage service
"""

from opencage.geocoder import OpenCageGeocode

API_KEY = "864bcba3e38a48e5b32ec88864118779"  # key needed to call OpenCage apis


def get_coordinates(place):
    """
    Get coordinates for the given place
    :param place: Place name
    :return: dictionary with place info
    """
    geocoder = OpenCageGeocode(API_KEY)
    results = geocoder.geocode(place)
    if results and len(results):
        return {
            "lat": results[0]["geometry"]["lat"],
            "lng": results[0]["geometry"]["lng"],
            "city": results[0]["formatted"],
            "flag": results[0]["annotations"]["flag"],
            "timezone": results[0]['annotations']['timezone']['name']
        }
    else:
        raise InvalidPlaceError(place)


class InvalidPlaceError(BaseException):
    """
    The provided place was not valid.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value) + " is not a valid place."
