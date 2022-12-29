from point import *
import matplotlib.pyplot as plt

def createPlot(allPoints: list, path: list, title, name):
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_facecolor("white")
    plt.grid()
    for elem in path:
        a = elem[0]
        b = elem[1]

        ax.plot([allPoints[a].x, allPoints[b].x], [allPoints[a].y, allPoints[b].y], 'b.', linestyle="-")
    fig.savefig(name)
    

