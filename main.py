import argparse
from open_cage import get_coordinates, InvalidPlaceError
from open_weather import get_weather, InvalidDataError
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError


def parse_arguments():
    """Parse the command arguments"""
    parser = argparse.ArgumentParser(
        description="Retrieve weather information for the given city",
        prog="kronos",
        epilog="Powered by OpenCage and OpenWeather")
    parser.add_argument('place', metavar='city', help='The chosen city')
    parser.add_argument('--verbose', '-v', action='count', default=0, help="More verbose")
    parser.add_argument("--version", action="version", version="kronos 1.0")
    return parser.parse_args()


def throw_console_errors(message):
    """Show arguments' errors"""
    return argparse.ArgumentParser().error(message)


# Get the arguments from the command-line except the filename
arguments = parse_arguments()
try:
    # Get place coordinates
    coordinates_data = get_coordinates(arguments.place)
    print(u"lat: %f; lng: %f; %s %s  - %s" % (
        coordinates_data["lat"], coordinates_data["lng"], coordinates_data["description"], coordinates_data["flag"],
        coordinates_data["timezone"]))
    # Get Weather data
    weather_data = get_weather(coordinates_data["lat"], coordinates_data["lng"])
    print(u"%s  %s - %s %s°C" % (
        weather_data["icon"], weather_data["weather"], weather_data["description"], weather_data["temperature"]))
except RateLimitExceededError:
    throw_console_errors('OpenCage rate limit has expired. Please try again later.')
except InvalidInputError:
    throw_console_errors('There was a problem with the provided input.')
except UnknownError:
    throw_console_errors('Unknown OpenCage error.')
except InvalidPlaceError as err:
    throw_console_errors(str(err))
except InvalidDataError as err:
    throw_console_errors(str(err))
