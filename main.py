import argparse
from open_cage import get_coordinates, InvalidPlaceError
from open_weather import get_weather, InvalidDataError
from opencage.geocoder import InvalidInputError, RateLimitExceededError, \
    UnknownError
from db_manager import open_and_create, add_weather_record, get_weather_history
from display_data import display_table
from air_quality import get_air_quality


def parse_arguments():
    """Parse the command arguments"""
    parser = argparse.ArgumentParser(
        description="Retrieve weather information for the given city",
        prog="kronos",
        epilog="Powered by OpenCage and OpenWeather")
    parser.add_argument('place', metavar='city', help='The chosen city')
    parser.add_argument('--verbose', '-v', action='count', default=0,
                        help="More verbosity")
    parser.add_argument("--version", action="version", version="kronos 1.0")
    parser.add_argument("--history", nargs='?', metavar='N rows', const=10,
                        type=int, help='Gives the local forecasts history '
                                       'for the given city')
    return parser.parse_args()


def throw_console_errors(message):
    """Show arguments' errors"""
    return argparse.ArgumentParser().error(message)


# Get the arguments from the command-line except the filename
arguments = parse_arguments()
verbosity = arguments.verbose
history = arguments.history
try:
    # Start the connection with the db
    open_and_create(verbosity)
    # Get place coordinates
    coordinates_data = get_coordinates(arguments.place, verbosity)
    if history:
        if verbosity > 1:
            print("Displaying history with a maximum of %f rows" % history)
        # Display the history for the given city
        rows = get_weather_history(coordinates_data["place"], history)
        display_table(rows)
    else:
        if verbosity > 1:
            print("Displaying results for the given place")
        # Get Weather data
        weather_data = get_weather(coordinates_data["lat"],
                                   coordinates_data["lng"])
        # Get air quality
        air_quality = get_air_quality(coordinates_data["city"])
        # Merging Results
        results = {**coordinates_data, **weather_data,
                   'air quality level': air_quality}
        # Displaying results
        display_table(
            {k: results[k] for k in ('place', 'weather', 'description',
                                     'temperature',
                                     'air quality level', 'icon')})
        # Storing results to build the forecasts history
        add_weather_record(results, verbosity)
except RateLimitExceededError:
    throw_console_errors('OpenCage rate limit has expired.'
                         ' Please try again later.')
except InvalidInputError:
    throw_console_errors('There was a problem with the provided input.')
except UnknownError:
    throw_console_errors('Unknown OpenCage error.')
except InvalidPlaceError as err:
    throw_console_errors(str(err))
except InvalidDataError as err:
    throw_console_errors(str(err))
