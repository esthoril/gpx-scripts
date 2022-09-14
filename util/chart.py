import matplotlib.pyplot as plt
import numpy as np

from util import point

TITLE = "Traumpfad 2022"
FILE = 'E:/Hiking/2022 Dream Path - Munich-Venice/gpx/dreampath-2022/__dreampath2022_clean.gpx'

ASC = [1673,2219,1063,1635,2025,1505,1725,1606,1762,190,1425,2142,1419,1331,166,26,6]
DESC = [1281,651,2631,517,1680,2949,500,1376,1972,1507,690,2170,2707,1717,283,19,10]


def plotDay(day, total=0, ax=None):
    '''
    Plot elevation graph of single day
    '''
    point, previous = None, None
    dist, elev = [], []
    for p in day:
        point = p
        if previous:
            d = point.distance(previous)*1000 # m
            total += d
        dist.append(total/1000)
        elev.append(p.elevation)
        previous = p
    #print(f"Distance: {total/1000:.1f} km")
    plt.plot(dist, elev) if ax is None else ax.plot(dist, elev)
    return total


def plotChartPerDay(days, ax=None):
    '''
    Plot elevation graph per day for each day
    '''
    if ax is None:
        fig, ax = plt.subplots(figsize=(18,8))
    for i, day in enumerate(days):
        #print(f"Plotting day {i+1}")
        plotDay(day, ax=ax)
    ax.set_ylabel('Elevation (m)')
    ax.set_xlabel('Distance (km)')
    for i in range(10,60,10):
        ax.axvline(x=i, ymin=0.02, ymax=0.98, ls='--', lw=.5, color='#444')
    if ax is None:
        ax.set_title(TITLE)
        plt.show()


def plotChartTotal(days, ax=None):
    '''
    Plot total elevation graph
    '''
    if ax is None:
        fig, ax = plt.subplots(figsize=(18,8))
    t = 0
    for i, day in enumerate(days):
        ax.text(t/1000+1, -92, (i+1), fontsize=8)
        t = plotDay(day, total=t, ax=ax)
        if i<len(days)-1:
            ax.axvline(x=t/1000, ymin=0.02, ymax=0.98, ls='--', lw=.5, color='#444')
    ax.set_ylabel('Elevation (m)')
    ax.set_xlabel('Distance (km)')
    if ax is None:
        ax.set_title(TITLE)
        plt.show()


def elevationBars(asc=[], desc=[], ax=None):
    '''
    Plot daily ascent and descent as bar graph
    '''
    WIDTH = 0.4
    if ax is None:
        fig, ax = plt.subplots(figsize=(18,8))
    ticks = [i+1 for i, _ in enumerate(asc)]
    x = np.arange(1,len(ticks)+1)
    asc_ = ax.bar(x - WIDTH/2, asc, WIDTH, label="Ascent")
    desc_ = ax.bar(x + WIDTH/2, desc, WIDTH, label="Descent")

    for list in [asc_, desc_]:
        ax.bar_label(list, padding=3, fontsize=8)

    ax.set_ylabel("Elevation gain/loss (m)")
    ax.set_ylim(0, max(asc + desc)+300)
    ax.set_xticks(ticks)
    ax.legend()
    ax.axhline(y=1500, ls='--', lw=.5, color='#444')
    if ax is None:
        ax.set_title(f'{TITLE} - daily elevation')
        plt.show()


def plotAll(days, asc, desc, title=None):
    fig, axes = plt.subplots(figsize=(9,9), nrows=3, ncols=1)
    plotChartPerDay(days, ax=axes[0])
    plotChartTotal(days, ax=axes[1])
    elevationBars(asc, desc, ax=axes[2])
    fig.suptitle(title)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    days = point.getList(FILE)
    #for i, p in enumerate(days):
    #    print(f"Day {i+1} : {len(p)} points")

    #plotChartPerDay(days)
    #plotChartTotal(days)
    #elevationBars(ASC, DESC)

    plotAll(days, ASC, DESC, title=TITLE)
