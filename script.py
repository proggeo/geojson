import json
import geojson
import math
from area import area

# for houses

file_name = 'housesGeo.json'

with open(file_name) as infile:
    json_file = json.load(infile)

my_feature_collection = geojson.FeatureCollection([])

for row in json_file:
    # print row
    coos = []
    for point in row:
        coos.append((point['lng'], point['lat']))
    current_geometry = geojson.Polygon([coos])
    # print current_geometry
    current_area = area(current_geometry)
    my_feature_collection["features"].append(geojson.Feature(geometry=current_geometry, properties={
        "area": current_area}))


print my_feature_collection

print geojson.dumps(my_feature_collection)

with open(file_name + '.geojson', 'w') as outfile:
    geojson.dump(my_feature_collection, outfile)
