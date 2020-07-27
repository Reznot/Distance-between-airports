import csv
from math import sin, cos, sqrt, asin, radians

data = []


def haversine(dep_lat, dep_lon, arrival_lat, arrival_lon):
    R = 6372.8  # Earth radius in km

    dlat = radians(arrival_lat - dep_lat)
    dlon = radians(arrival_lon - dep_lon)

    a = sin(dlat / 2) ** 2 + cos(radians(dep_lat)) * cos(radians(arrival_lat)) * sin(dlon / 2) ** 2
    return round(R * 2 * asin(sqrt(a)), 2)


with open('Flight Distance Test.csv', 'r+') as f:
    csv_data = csv.reader(f)
    headers = next(csv_data)
    print(headers)

    for row in csv_data:
        print(haversine(float(row[3]), float(row[4]), float(row[5]), float(row[6])))

# print(*data, sep='\n')
