import json
import geojson
import math
from area import area

# for first floor

file_name = 'firstFloorFunctionGeo.json'

with open(file_name) as infile:
    json_file = json.load(infile)

my_feature_collection = geojson.FeatureCollection([])

floor_functions = ["office", "cafe", "garage", "culture", "housing","ruin"]

for row in json_file:
	print row[1]
	floor_function = floor_functions[row[0]]
	coos = []
	for point in row[1]:
		coos.append((point['lng'], point['lat']))
	current_geometry = geojson.Polygon([coos])
	# print current_geometry
	current_area = area(current_geometry)
	my_feature_collection["features"].append(geojson.Feature(geometry=current_geometry, properties={
                                             "function": floor_function ,"area": current_area}))


print my_feature_collection

print geojson.dumps(my_feature_collection)

with open(file_name + '.geojson', 'w') as outfile:
    geojson.dump(my_feature_collection, outfile)
