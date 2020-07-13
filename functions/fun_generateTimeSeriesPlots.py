from matplotlib.dates import date2num
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def generateTimeSeriesPlot(inputData,TimeIndex,timeseries_plots,title,fname,plot_or_save):
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=100)  # pyplot uses inches (WTF) and scales by a dpi. so figsize*dpi should be in pixels
    x0=date2num(pd.to_datetime(inputData[TimeIndex].max())-datetime.timedelta(days=14))
    x1=date2num(pd.to_datetime(inputData[TimeIndex].max()))
    for var in timeseries_plots:
        ax.plot(inputData[TimeIndex], inputData[var], label=var,markersize=1,marker='.',linestyle = 'None')

    ax.axvspan(x0,x1, alpha=0.5, color='red')
    ax.set_xlabel('time')  # Add an x-label to the axes.
    ax.set_ylabel(r'Microstrain ($\mu \epsilon$)')  # Add a y-label to the axes.
    ax.set_title(title)  # Add a title to the axes.
    ax.legend(loc=(1.05, 0.5), edgecolor='None', markerscale=1.8)
    plt.grid(True)
    ax.autoscale(enable=True, axis='both', tight=True)
    plt.tight_layout()
    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)

def generateTimeSeriesPlotZoomed(inputData,TimeIndex,timeseries_plots,title,fname,plot_or_save):
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=100)  # pyplot uses inches (WTF) and scales by a dpi. so figsize*dpi should be in pixels
    x0=date2num(pd.to_datetime(inputData[TimeIndex].max())-datetime.timedelta(days=14))
    x1=date2num(pd.to_datetime(inputData[TimeIndex].max()))
    for var in timeseries_plots:
        ax.plot(inputData[TimeIndex], inputData[var], label=var,markersize=1,marker='.',linestyle = 'None')

    ax.set_xlim([x0,x1])
    ax.set_xlabel('time')  # Add an x-label to the axes.
    ax.set_ylabel(r'Microstrain ($\mu \epsilon$)')  # Add a y-label to the axes.
    ax.set_title(title)  # Add a title to the axes.
    ax.legend(loc=(1.05, 0.5), edgecolor='None', markerscale=1.8)
    plt.grid(True)
    plt.tight_layout()
    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)