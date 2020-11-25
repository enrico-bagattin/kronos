from sys import argv
from open_cage import get_coordinates, InvalidPlaceError
from open_weather import get_weather, InvalidDataError
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError

# Get the arguments from the command-line except the filename
arguments = argv[1:]
if len(arguments) > 0:
    try:
        # Get place coordinates
        coordinates_data = get_coordinates(arguments[0])
        print(u"lat: %f; lng: %f; %s %s  - %s" % (
            coordinates_data["lat"], coordinates_data["lng"], coordinates_data["description"], coordinates_data["flag"],
            coordinates_data["timezone"]))
        # Get Weather data
        weather_data = get_weather(coordinates_data["lat"], coordinates_data["lng"])
        print(u"%s  %s - %s %s°C" % (
            weather_data["icon"], weather_data["weather"], weather_data["description"], weather_data["temperature"]))
    except RateLimitExceededError:
        print('OpenCage rate limit has expired. Please try again later.')
    except InvalidInputError:
        print('There was a problem with the provided input.')
    except UnknownError:
        print('Unknown OpenCage error.')
    except InvalidPlaceError as err:
        print(err)
    except InvalidDataError as err:
        print(err)
else:
    print("Please specify a place argument.")
