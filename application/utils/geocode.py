from math import radians, cos, sin, asin, sqrt
import geocoder
from typing import Optional, AnyStr


def distance_between_two_points(first_coordinates: tuple, second_coordinates: tuple) -> tuple:
    """
    Calculate the great circle distance between two pints
    on the Earth (specified in decimal degrees)
    :param first_coordinates: Coordinates (latitude, longitude) of first point
    :param second_coordinates: Coordinates (latitude, longitude) of second point
    :return: distance
    """
    lat1, lon1 = first_coordinates
    lat2, lon2 = second_coordinates
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # Haversina formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of Earth in kilometers is 6731
    km = 6371 * c
    # If distance in kilometres, round the value
    if km >= 1:
        return round(km, 1), 'km'
    else:
        # If distance is smaller than 1, return metres value
        metres = km * 1000
        return round(metres), 'm'


def get_address_by_coordinates(coordinates: tuple) -> Optional[AnyStr]:
    """
    Return address string value by coordinates
    :param coordinates: Coordinates (latitude, longitude)
    :return: string value
    """
    latitude = coordinates[0]
    longitude = coordinates[1]
    location = geocoder.yandex([latitude, longitude], method='reverse', lang='ru-RU', kind='house', apikey='4d16304f-12ba-4134-ac9b-f0da5028a1f4')
    if not location.json:
        return None
    return location.json.get('address')
