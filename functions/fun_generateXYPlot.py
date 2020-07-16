from matplotlib.dates import date2num
import pandas as pd
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

def generateXYPlot(inputData,XY_plot,fitTrend,title,fname,plot_or_save):
    fig, ax = plt.subplots(figsize=(5, 5), dpi=100)
    ax.plot(inputData[XY_plot[0]], inputData[XY_plot[1]], label=[XY_plot[0],' vs. ',XY_plot[1]],markersize=1,marker='+',linestyle = 'None')
    ax.set_xlabel(XY_plot[0])  # Add an x-label to the axes.
    ax.set_ylabel(XY_plot[1])  # Add a y-label to axes
    ax.set_title(title)  # Add a title to the axes.
    plt.grid(True)
    ax.autoscale(enable=True, axis='both', tight=True)
    if fitTrend=='linear':
        xLims = [inputData[XY_plot[0]].min(), inputData[XY_plot[0]].max()]
        fit = poly.polyfit(inputData[XY_plot[0]],inputData[XY_plot[1]], 1)
        ax.plot(xLims,poly.polyval(xLims,fit))
    elif fitTrend=='none':
        pass

    plt.tight_layout()
    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)
