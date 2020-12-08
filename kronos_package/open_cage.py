"""
This module is used to retrieve coordinates data from the OpenCage service
"""

from opencage.geocoder import OpenCageGeocode

API_KEY = "864bcba3e38a48e5b32ec88864118779"  # key needed to call OpenCage api


def get_coordinates(place, verbosity=0):
    """
    Get coordinates for the given place
    :param place: Place name
    :param verbosity: Verbosity level
    :return: dictionary with place info
    """
    geocoder = OpenCageGeocode(API_KEY)
    results = geocoder.geocode(place,language='native', limit=1)
    if results and len(results):
        data = {
            "lat": results[0]["geometry"]["lat"],
            "lng": results[0]["geometry"]["lng"],
            "place": results[0]["formatted"],
            "city": results[0]['components']['city']
            if 'city' in results[0]['components'] else None,
            "flag": results[0]["annotations"]["flag"],
            "timezone": results[0]['annotations']['timezone']['name']
        }
        if verbosity > 0:
            print(u"Latitude: %f, Longitude: %f" % (data["lat"], data["lng"]))
            print(u"Detected City: %s %s  - %s" % (data["city"], data["flag"],
                                                   data["timezone"]))
        return data
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
