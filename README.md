#### main.py

Main script to call other scripts. For example

* _format.py_
* _waypoints.py_
* _chart.py_ `python main.py --chart "E:/Hiking/2022 Dream Path - Munich-Venice/gpx/dreampath-2022/__dreampath2022_clean.gpx" --title "Traumpfad 2022"`

_test_ folder contains some example .gpx files

#### format.py

Convert and clean gpx files

#### chart.py

Create graph of daily elevation of your gpx file, either as 3 subplots or as separate plots. \
In your input .gpx file:
* Each day or section should be in `<trk><\trk>` tags
* Each datapoint should be in format `      <trkpt lat="47.760641" lon="11.573948"><ele>688.730469</ele></trkpt>`

(You can use the `gpx.py` script to convert your gpx file to the proper format)

<img src='img/traumpfad2022.png' width=720/>