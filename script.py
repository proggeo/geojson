import json
import geojson
import math
from area import area

# for trees

file_name = 'trees_GeoCoo.json'

with open(file_name) as infile:
    json_file = json.load(infile)

# print json_file

# help(geojson.FeatureCollection)

my_feature_collection = geojson.FeatureCollection([])

for row in json_file:
    current_geometry = geojson.Point((row['lon'], row['lat']))
    current_area = area(current_geometry)
    current_area = math.pi * row['radius'] ** 2
    my_feature_collection["features"].append(geojson.Feature(geometry=current_geometry, properties={
                                             "radius": row['radius'], "area": current_area}))


# current_feature = geojson.Feature(geometry = geojson.Polygon([[(0,0),(1,1)]]))

# my_feature_collection["features"].append(current_feature)
# my_feature_collection["features"].append(current_feature)

# print my_feature_collection

print geojson.dumps(my_feature_collection)

with open(file_name + '.geojson', 'w') as outfile:
    geojson.dump(my_feature_collection, outfile)
