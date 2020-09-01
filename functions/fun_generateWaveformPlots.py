from matplotlib.dates import date2num
import pandas as pd
import matplotlib.pyplot as plt

def generateWaveformPlot(inputData,TimeIndex,plotVariables,nrows,ncols,fname,plot_or_save):
    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(5, 5), dpi=100)
    ax.plot(inputData[TimeIndex], inputData[plotVariables])
    plt.grid(True)
    ax.autoscale(enable=True, axis='both', tight=True)
    plt.tight_layout()
    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)
