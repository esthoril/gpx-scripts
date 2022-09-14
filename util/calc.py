"""
Calculate distance between points in GPX file
"""

from math import sin, cos, sqrt, atan2, radians, ceil

def elevation(days, up=True):
    n = len(days)
    res = 0
    for i in range(n-1):
        t = days[i].ascent(days[i+1]) if up else days[i].descent(days[i+1])
        if t > 3:
            res += t

    return ceil(res)


# Calculate distance between two points
def distance(point1, point2):
    R = 6373.0 # approximate radius of earth in km
    lat1 = radians(point1[0])
    lon1 = radians(point1[1])
    lat2 = radians(point2[0])
    lon2 = radians(point2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def getDistance(file):
    total_distance = 0
    point = None
    WAYPOINT = 15.0
    index = 1

    fh = open(file, encoding="utf8")
    for i, item in enumerate(fh):
        if '<trkpt' in item:
            parts = item.split('"')
            lat = float(parts[1])
            lon = float(parts[3])
            new_point = [lat, lon]

            if point is not None:
                step = calc_distance(point, new_point)
                total_distance += step
                if total_distance > WAYPOINT*index:
                    index += 1
                    print(item)


            point = new_point

    print("Total distance:", round(total_distance*100)/100, "km")
