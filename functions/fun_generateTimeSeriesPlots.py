from matplotlib.dates import date2num
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def generateTimeSeriesPlot(inputData,TimeIndex,timeseries_plots,lines_or_marks,title,fname,plot_or_save):
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=100)  # pyplot uses inches (WTF) and scales by a dpi. so figsize*dpi should be in pixels
    x0=date2num(pd.to_datetime(inputData[TimeIndex].max())-datetime.timedelta(days=14))
    x1=date2num(pd.to_datetime(inputData[TimeIndex].max()))
    if lines_or_markers=='markers':
        for var in timeseries_plots:
            ax.plot(inputData[TimeIndex], inputData[var], label=var,markersize=1,marker='.',linestyle = 'None')
    elif lines_or_markers='lines':
        for var in timeseries_plots:
            ax.plot(inputData[TimeIndex], inputData[var], label=var,linestyle = 'solid')  
            
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

inputData = df_SS
TimeIndex = "TIMESTAMP"
timeseries_plots_minmax=['SensorRel_Min(1)','SensorRel_Max(1)']
timeseries_plots_avg=['test']

title='test'
fname='test'
plot_or_save='plot'

def generateTimeSeriesMinMaxAvg(inputData,TimeIndex,timeseries_plots_min, timeseries_plots_max,timeseries_plots_avg,beards,title,fname,plot_or_save):
## generateTimeSeriesMinMaxAvg wants 3 input timeseries plot lists, with the following formats:
# timeseries_plots_min = [  'var1_min',
#                           'var2_min',
#                           'var3_min']
# timeseries_plots_max = [  'var1_max',
#                           'var2_max',
#                           'var3_max']
# timeseries_plots_avg = [  'var1_avg',
#                           'var2_avg',
#                           'var3_avg']
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=100)
    for ii,var in enumerate(timeseries_plots_minmax):
        if beards==True:
        ax.fill_between(inputData[TimeIndex], inputData[timeseries_plots_max[ii]], inputData[timeseries_plots_min[ii]], alpha=0.2)
        else:
        ax.plot(inputData[TimeIndex], inputData[timeseries_plots_max[ii]], label=None,markersize=1,marker='.',linestyle = 'solid',color=(0.8, 0.8, 0.8))
        ax.plot(inputData[TimeIndex], inputData[timeseries_plots_min[ii]], label=None,markersize=1,marker='.',linestyle = 'solid',color=(0.8, 0.8, 0.8))

    for var in timeseries_plots_avg:
        colour=next(ax._get_lines.prop_cycler)['color']
        ax.plot(inputData[TimeIndex], tempo, label=var,markersize=1,marker='.',linestyle = 'solid',color=colour)

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

def generateTimeSeriesSubplots(inputData,TimeIndex,timeseries_plots,nRows,nCols,fname,plot_or_save):
## generateTimeSeriesSubplots wants input timeseries plot lists and the number of rols and cols:
    fig, axs = plt.subplots(nRows, nCols, figsize=(10, 4.8), dpi=100)
    for ii, var in enumerate(timeseries_plots):
        axs[ii].plot(inputData[TimeIndex], inputData[var], label=var,markersize=1,marker='.',linestyle = 'solid',color=(0.8, 0.8, 0.8))
        axs[ii].set_title(var)
        axs[ii].set_xlabel('time')  # Add an x-label to the axes.
        axs[ii].set_ylabel(r'Microstrain ($\mu \epsilon$)')  # Add a y-label to the axes.
        axs[ii].grid(True)

    plt.tight_layout()

    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)


def generateTimeSeriesDisplaced(inputData,TimeIndex,timeseries_plots,dispFactor,dispRef,fname,plot_or_save):
## generateTimeSeriesDisplaced makes time series plots and offsets them vertically.
# The vertical offset is set as a constant value (dispFactor). The normalisation can be chosen (dispRef), with a choice of 'initial' referencing all to the initial value (and excluding any initial Null values e.g. NaN).
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=100)
    for ii, var in enumerate(timeseries_plots):
        if dispRef=='initial':
            offsetFactor = dispFactor
            offsetRef = inputData[var].loc[~inputData[var].isnull()].iloc[0]
        x0=inputData[TimeIndex].min()
        x1=inputData[TimeIndex].max()
        colour=next(ax._get_lines.prop_cycler)['color']
        ax.plot(inputData[TimeIndex],(offsetFactor*ii)+inputData[var]-offsetRef, label=var,markersize=1,marker='.',linestyle = 'solid',color=colour)
        ax.plot([x0,x1], [(dispFactor*ii),(dispFactor*ii)], label=None,linestyle = 'solid',color=(0.8, 0.8, 0.8))
        ax.set_xlabel('time')  # Add an x-label to the axes.
        ax.set_ylabel('Relative displacement')  # Add a y-label to the axes.
        ax.grid(False)
        plt.tight_layout()

    ax.set_title('Displacement with offset of '+str(offsetFactor))
    ax.legend(loc=(1.05, 0.5), edgecolor='None', markerscale=1.8)
    ax.set_xlim([x0,x1])
    plt.tight_layout()

    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)

