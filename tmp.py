# Construct one file from multiple gpx files

file = 'european-walking-route-e10.gpx'

def appendfile(file, fhand):
  fh = open(file, encoding="utf8")
  for i, item in enumerate(fh):
    item = item.replace('<trk>',  '\n  <trk>')
    item = item.replace('<trkseg>',  '    <trkseg>\n      ')
    item = item.replace(' /><trkpt',  '/>\n      <trkpt')
    item = item.replace(' /></trkseg>', '/>\n    </trkseg>\n')
    
    item = item.replace('    <trkseg>', '')
    item = item.replace('    </trkseg>', '')
    
    
    fhand.write(item)

#
# Create merged file
#
def makeFile(file):
  fhand = open('tmp.gpx','w') # Create new file
  appendfile(file, fhand)
  
  
makeFile(file)