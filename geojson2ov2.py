
# Converter to move Google Maps places to Tomtom myDrive cloud and devices
# Instructions:
# 1.- Export GeoJSON file using Google takeout selecting only Google Maps
# 2.- Convert the GeoJSON file to Tomtom OV2 format with this script
# 3.- Import the OV2 in Tomtom myDrive page in 'my places'
#
# Usage python geojson2ov2.py <infile.json> <outfile.ov2>
#
# Development dependencies documentation
# GeoJSON parser: https://pypi.python.org/pypi/geojson
# Tomtom SDK on OV2 format: https://www.tomtom.com/lib/doc/ttnavsdk3_manual.pdf
#
# OV2 writing tips from https://github.com/Mithrandir0x/flaskmap

import geojson
import struct
import sys

if len(sys.argv) != 3:
	print "Usage python geojson2ov2.py <infile.json> <outfile.ov2>"
	sys.exit(0)

try:
	data = open(sys.argv[1], 'r').read()
except:
	print "Error opening ", sys.argv[1]
	sys.exit(1)

geodata = geojson.loads(data)

try:
	ov2file = open(sys.argv[2], 'wb')
except:
	print "Error opening for writing ", sys.argv[2]

for place in geodata['features']:
	print "POI: ", place['properties']['Title']
	name = place['properties']['Title'].encode('ascii', 'ignore')
	pf = '<ci2l%ss\x00' % len(name)
	length = len(name) + 14
	longitude = int(float(place['geometry']['coordinates'][0]) * 100000)
	latitude = int(float(place['geometry']['coordinates'][1]) * 100000)
	ov2file.write(struct.pack(pf, chr(2), length, longitude, latitude, name))
	ov2file.write(chr(0))
