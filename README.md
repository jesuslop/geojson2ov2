# geojson2ov2

Converter to move Google Maps places to Tomtom myDrive cloud and devices

Instructions:

* Export GeoJSON file using Google takeout selecting only Google Maps
* Convert the GeoJSON file to Tomtom OV2 format with this script
* Import the OV2 in Tomtom myDrive page in 'my places'

Usage python geojson2ov2.py <infile.json> <outfile.ov2>

Development dependencies documentation

* GeoJSON parser: https://pypi.python.org/pypi/geojson
* Tomtom SDK on OV2 format: https://www.tomtom.com/lib/doc/ttnavsdk3_manual.pdf

CREDITS:
	OV2 writing tips from https://github.com/Mithrandir0x/flaskmap

