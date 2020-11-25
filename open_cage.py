from opencage.geocoder import OpenCageGeocode

API_KEY = "864bcba3e38a48e5b32ec88864118779"  # key needed to call OpenCage apis


def get_coordinates(place):
    """
    Get coordinates for the given place
    :param place: Place name
    :return: json with place info
    """
    geocoder = OpenCageGeocode(API_KEY)
    results = geocoder.geocode(place)

    return {
        "lat": results[0]["geometry"]["lat"],
        "lng": results[0]["geometry"]["lng"],
        "description": results[0]["formatted"],
        "flag": results[0]["annotations"]["flag"],
        "timezone": results[0]['annotations']['timezone']['name']
    }


