import sys

def cleanGPX1(input, output):
    for line in input:
        parts = line.split('/>')

        for p in parts:
            p += '></trkpt>\n'
            p = p.replace('rtept', 'trkpt')
            #output.write('      <trkpt' + p + '\n')
            output.write('      ' + p)

def cleanGPX2(input, output):
    for i, item in enumerate(input):
        item = item.strip()
        if '<trkpt' in item or '<rtept' in item:
            item = item.replace('<trkpt','').replace('</trkpt>','');
            item = item.replace('<rtept','').replace('</rtept>','');
            item = item.strip()
            ele = input.readline().strip()
            str = '<trkpt {}{}</trkpt>'.format(item, ele)
            #<trkpt lat="51.28116" lon="4.04812"></trkpt>
            output.write(str)
            output.write('\n')

def cleanGPX3(input, output):
    data = input.read()
    line = data.replace("<trkpt", "\n      <trkpt")
    output.write(line)

def cleanGPX4(input, output):
    """
    <trkpt lat="49.797484875" lon="5.070662498">
      <ele>232.23</ele>
    </trkpt>

    <trkpt lat="49.797484875" lon="5.070662498"><ele>232.23</ele></trkpt>
    """
    point = ""
    for line in input:
        line_ = line.strip()
        if line_.startswith("<trkpt"):
            point += f"      {line_}"
        elif line_.startswith("<ele>"):
            point += line_
        elif line_ == "</trkpt>":
            point += f"{line_}\n"
            output.write(point)
            point = ""
        else:
            output.write(f"{line}\n")

def createHeader():
    str = ""
    str += '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    srt += '<gpx version="1.1" creator="Mapometer.com" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">\n'
    str += '  <metadata>\n'
    str += '    <name></name>\n'
    str += '    <desc></desc>\n'
    str += '  </metadata>\n'
    return str

def createFooter():
    return '</gpx>'

def createGPX(input, output):
    output.write(createHeader())

    output.write('  <trk>\n')
    output.write('    <trkseg>\n')
    for line in input:
        parts = line.split(",")
        output.write('      <trkpt lat="{}", lon="{}"></trkpt>\n'.format(parts[0].strip(), parts[1].strip()))
    output.write('    </trkseg>\n')
    output.write('  </trk>\n')

    output.write(createFooter())

def createGPX2(input, output):
    for line in input:
        parts = line.strip().split(",")
        output.write('      <trkpt lat="{}", lon="{}"><ele>{}</ele></trkpt>\n'.format(parts[0].strip(), parts[1].strip(), parts[2].strip()))

def removeTime(input, output):
    row = ''
    for line in input:
        if '<trkpt' in line:
            row = line.strip()
        elif '<ele>' in line:
            row += line.strip()
            row += '</trkpt>'
            output.write('      ' + row + '\n')
        else:
            continue

def removeEle(input, output):
    for line in input:
        if '<trkpt' in line:
            line = line.strip()
            line += '</trkpt>\n'
            output.write('      ' + line)

def reverse(input, output):
    list = []
    for i, item in enumerate(input):
        item = item.strip()
        if '<trkpt' in item or '<rtept' in item:
            item = item.replace('<trkpt','').replace('</trkpt>','');
            item = item.replace('<rtept','').replace('</rtept>','');
            list.append(item);

    list.reverse()

    for item in list:
        output.write('\n      <trkpt' + item + '</trkpt>')
