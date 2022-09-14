"""
Expected input per line
date (DD/MM/YYY), day, lat, lon, label

01/09/2019, 6, 46.03029, 7.09349, 1629.3, Arpette campsite
02/09/2019, 7, 46.04584, 6.99447, 1328.8, Le Peuty campsite
"""

def setMarkers(input):
	output = open('waypoints.txt', 'w')
	with open(input, encoding="utf8") as f:
		for i, item in enumerate(f):
			setMarker(item, output)

def setMarker(item, output):
	item = item.strip()
	parts = item.split(',')
	output.write('<Placemark><name>Day {} - {}</name><styleUrl>#icon-31-nodesc</styleUrl><Point><coordinates>{},{},{}</coordinates></Point></Placemark>\n'
		.format(parts[1], parts[5], parts[3], parts[2], parts[4]))
