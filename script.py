import json
import geojson
import math
from area import area

# for cars

file_name = 'cars_GeoCoo.json'

with open(file_name) as infile:
    json_file = json.load(infile)

my_feature_collection = geojson.FeatureCollection([])

for row in json_file:
	# print row
	coos = []
	coos.append((row['a']['lon'], row['a']['lat']))
	coos.append((row['b']['lon'], row['b']['lat']))
	coos.append((row['c']['lon'], row['c']['lat']))
	coos.append((row['d']['lon'], row['d']['lat']))
	coos.append((row['a']['lon'], row['a']['lat']))
	current_geometry = geojson.Polygon([coos])
	print current_geometry
	current_area = area(current_geometry)
	my_feature_collection["features"].append(geojson.Feature(geometry=current_geometry, properties={
                                             "area": current_area}))


print my_feature_collection

print geojson.dumps(my_feature_collection)

with open(file_name + '.geojson', 'w') as outfile:
    geojson.dump(my_feature_collection, outfile)
