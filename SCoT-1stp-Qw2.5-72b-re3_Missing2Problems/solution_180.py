import math

def distance_lat_long(slat, slon, elat, elon):
    # Earth's radius in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    slat, slon, elat, elon = map(math.radians, [slat, slon, elat, elon])

    # Calculate the differences in coordinates
    dlat = elat - slat
    dlon = elon - slon

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(slat) * math.cos(elat) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = R * c
    return distance