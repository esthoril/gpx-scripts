from util import waypoints, format, calc, chart, point
import argparse

def arg_parser():
    parser = argparse.ArgumentParser(description="GPX options")
    parser.add_argument('-d', '--distance', action="store_true", help="Get gpx distance")
    parser.add_argument('-f', '--format', action="store_true", help="Format GPX file")
    parser.add_argument('-w', '--waypoints', help="Create waypoints file")
    parser.add_argument('-c', '--chart', help="Create elevation chart")
    parser.add_argument('-t', '--title', help="Output title")
    return parser

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = UI.MainWindow.MainWindow()
    win.show()
    return app.exec_()

if __name__ == "__main__":
    parser = arg_parser()
    args = parser.parse_args()
    print(args)

    if args.distance:
        distance.getDistance("output/tmp.gpx")

    if args.waypoints:
        waypoints.setMarkers(args.waypoints)

    if args.chart:
        asc = [1673,2219,1063,1635,2025,1505,1725,1606,1762,190,1425,2142,1419,1331,166,26,6]
        desc = [1281,651,2631,517,1680,2949,500,1376,1972,1507,690,2170,2707,1717,283,19,10]
        days = point.getList(args.chart)
        #asc, desc = [], []

        for day in days:
            g = calc.elevation(day)
            l = calc.elevation(day, up=False)
            asc.append(g)
            desc.append(l)
        chart.plotAll(days, asc, desc, title=args.title)


    if args.format:
        output = open('output/output.gpx', "w", encoding='UTF-8')
        input = open('output/tmp.gpx', "r", encoding='UTF-8')
        #format.cleanGPX1(input, output)  # rtept to trkpt
        #format.cleanGPX3(input, output)
        format.cleanGPX4(input, output)
        #createGPX(input, output)
        #createGPX2(input, output)
        #removeEle(input, output)
        #format.removeTime(input, output)
        #reverse(input, output)

        input.close()
        output.close()
