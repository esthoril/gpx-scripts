from math import sin, cos, sqrt, atan2, radians

class Point:
    def __init__(self, index, lat, lon, elevation):
        self.index = index
        self.lat = lat
        self.lon = lon
        self.elevation = elevation

    def distance(self, other):
        R = 6373.0 # approximate radius of earth in km
        lat1 = radians(self.lat)
        lon1 = radians(self.lon)
        lat2 = radians(other.lat)
        lon2 = radians(other.lon)
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c

    def ascent(self, other):
        gain = other.elevation-self.elevation
        return max(gain, 0)

    def descent(self, other):
        loss = self.elevation-other.elevation
        return max(loss, 0)

    def __str__(self):
        return f"{self.index} ({self.lat:.3f}, {self.lon:.3f}) {self.elevation} m"


def getList(file):
    lists = []
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()

            if line.startswith('<trk>'):
                lists.append([])

            # Check distances
            if line.startswith('<trkpt'):
                parts = line.split('"')
                lat = float(parts[1])
                lon = float(parts[3])
                elevation = float((line.split("<ele>")[1]).split("</ele>")[0])
                lists[-1].append(Point(i, lat, lon, elevation))

    return lists