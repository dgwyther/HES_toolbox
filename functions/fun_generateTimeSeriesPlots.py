from matplotlib.dates import date2num
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
from dateutil import parser

def generateTimeSeriesPlot(inputData,TimeIndex,timeseries_plots,lines_or_marks,title,fname,plot_or_save,**keyword_parameters):
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=100)  # pyplot uses inches (WTF) and scales by a dpi. so figsize*dpi should be in pixels
    x0=date2num(pd.to_datetime(inputData[TimeIndex].max())-datetime.timedelta(days=14))
    x1=date2num(pd.to_datetime(inputData[TimeIndex].max()))
    if lines_or_markers=='markers':
        for var in timeseries_plots:
            ax.plot(inputData[TimeIndex], inputData[var], label=var,markersize=1,marker='.',linestyle = 'None')
    elif lines_or_markers=='lines':
        for var in timeseries_plots:
            ax.plot(inputData[TimeIndex], inputData[var], label=var,linestyle = 'solid')  

    ax.axvspan(x0,x1, alpha=0.5, color='red')
    ax.set_xlabel('time')  # Add an x-label to the axes.
    ax.set_ylabel(r'Microstrain ($\mu \epsilon$)')  # Add a y-label to the axes.
    ax.set_title(title)  # Add a title to the axes.
    ax.legend(loc=(1.05, 0.5), edgecolor='None', markerscale=1.8)
    plt.grid(True)
    ax.autoscale(enable=True, axis='both', tight=True)
    if ('axisLims' in keyword_parameters):
        x0=parser.parse(keyword_parameters['axisLims'][0])
        x1=parser.parse(keyword_parameters['axisLims'][1])
        y0=keyword_parameters['axisLims'][2]
        y1=keyword_parameters['axisLims'][3]
        ax.set_xlim([x0,x1])
        ax.set_ylim([y0,y1])
    if ('xAxisLims' in keyword_parameters):
        x0=parser.parse(keyword_parameters['xAxisLims'][0])
        x1=parser.parse(keyword_parameters['xAxisLims'][1])
        ax.set_xlim([x0,x1])
    if ('yAxisLims' in keyword_parameters):
        y0=keyword_parameters['yAxisLims'][0]
        y1=keyword_parameters['yAxisLims'][1]
        ax.set_ylim([y0,y1])
    if (('axisLims','xAxisLims',) not in keyword_parameters):
        ax.set_xlim([x0,x1])
    if ('annotate' in keyword_parameters):
        annotation_text=keyword_parameters['annotate']
        annotate_x1=date2num(parser.parse(keyword_parameters['annotatePointXY'][0]))
        annotate_y1=keyword_parameters['annotatePointXY'][1]
        annotate_x2=date2num(parser.parse(keyword_parameters['annotateTextXY'][0]))
        annotate_y2=keyword_parameters['annotateTextXY'][1]
        ax.annotate(annotation_text,
                xy=(annotate_x1, annotate_y1), xycoords='data',
                xytext=(annotate_x2, annotate_y2), textcoords='data',
                arrowprops=dict(arrowstyle="->"),
                horizontalalignment='right', verticalalignment='bottom')
    fig.autofmt_xdate(rotation=45)
    plt.tight_layout()
    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)
        plt.close()

def generateTimeSeriesPlotZoomed(inputData,TimeIndex,timeseries_plots,title,fname,plot_or_save,**keyword_parameters):
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=100)  # pyplot uses inches (WTF) and scales by a dpi. so figsize*dpi should be in pixels
    x0=date2num(pd.to_datetime(inputData[TimeIndex].max())-datetime.timedelta(days=14))
    x1=date2num(pd.to_datetime(inputData[TimeIndex].max()))
    for var in timeseries_plots:
        ax.plot(inputData[TimeIndex], inputData[var], label=var,markersize=1,marker='.',linestyle = 'None')

    ax.set_xlabel('time')  # Add an x-label to the axes.
    ax.set_ylabel(r'Microstrain ($\mu \epsilon$)')  # Add a y-label to the axes.
    ax.set_title(title)  # Add a title to the axes.
    ax.legend(loc=(1.05, 0.5), edgecolor='None', markerscale=1.8)
    plt.grid(True)
    if ('axisLims' in keyword_parameters):
        x0=parser.parse(keyword_parameters['axisLims'][0])
        x1=parser.parse(keyword_parameters['axisLims'][1])
        y0=keyword_parameters['axisLims'][2]
        y1=keyword_parameters['axisLims'][3]
        ax.set_xlim([x0,x1])
        ax.set_ylim([y0,y1])
    if ('xAxisLims' in keyword_parameters):
        x0=parser.parse(keyword_parameters['xAxisLims'][0])
        x1=parser.parse(keyword_parameters['xAxisLims'][1])
        ax.set_xlim([x0,x1])
    if ('yAxisLims' in keyword_parameters):
        y0=keyword_parameters['yAxisLims'][0]
        y1=keyword_parameters['yAxisLims'][1]
        ax.set_ylim([y0,y1])
    if (('axisLims','xAxisLims',) not in keyword_parameters):
        ax.set_xlim([x0,x1])
    if ('annotate' in keyword_parameters):
        annotation_text=keyword_parameters['annotate']
        annotate_x1=date2num(parser.parse(keyword_parameters['annotatePointXY'][0]))
        annotate_y1=keyword_parameters['annotatePointXY'][1]
        annotate_x2=date2num(parser.parse(keyword_parameters['annotateTextXY'][0]))
        annotate_y2=keyword_parameters['annotateTextXY'][1]
        ax.annotate(annotation_text,
                xy=(annotate_x1, annotate_y1), xycoords='data',
                xytext=(annotate_x2, annotate_y2), textcoords='data',
                arrowprops=dict(arrowstyle="->"),
                horizontalalignment='right', verticalalignment='bottom')
    fig.autofmt_xdate(rotation=45)
    plt.tight_layout()
    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)
        plt.close()

def generateTimeSeriesMinMaxAvg(inputData,TimeIndex,timeseries_plots_min, timeseries_plots_max,timeseries_plots_avg,beards,title,xAxisName,yAxisName,fname,plot_or_save,**keyword_parameters):
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
    for ii,var in enumerate(timeseries_plots_min):
        if beards==True:
            ax.fill_between(inputData[TimeIndex], inputData[timeseries_plots_max[ii]], inputData[timeseries_plots_min[ii]], alpha=0.5)
        else:
            ax.plot(inputData[TimeIndex], inputData[timeseries_plots_max[ii]], label=None,markersize=1,marker='.',linestyle = 'solid',color=(0.8, 0.8, 0.8))
            ax.plot(inputData[TimeIndex], inputData[timeseries_plots_min[ii]], label=None,markersize=1,marker='.',linestyle = 'solid',color=(0.8, 0.8, 0.8))

    for ii,var in enumerate(timeseries_plots_avg):
        colour=next(ax._get_lines.prop_cycler)['color']
        ax.plot(inputData[TimeIndex], inputData[timeseries_plots_avg[ii]], label=var,markersize=1,marker='None',linestyle = 'solid',color=colour)

    ax.set_title(title)  # Add a title to the axes.
    ax.set_ylabel(xAxisName)
    ax.set_ylabel(yAxisName)
    ax.legend(loc=(1.05, 0.5), edgecolor='None', markerscale=1.8)
    if ('axisLims' in keyword_parameters):
        x0=parser.parse(keyword_parameters['axisLims'][0])
        x1=parser.parse(keyword_parameters['axisLims'][1])
        y0=keyword_parameters['axisLims'][2]
        y1=keyword_parameters['axisLims'][3]
        ax.set_xlim([x0,x1])
        ax.set_ylim([y0,y1])
    if ('xAxisLims' in keyword_parameters):
        x0=parser.parse(keyword_parameters['xAxisLims'][0])
        x1=parser.parse(keyword_parameters['xAxisLims'][1])
        ax.set_xlim([x0,x1])
    if ('yAxisLims' in keyword_parameters):
        y0=keyword_parameters['yAxisLims'][0]
        y1=keyword_parameters['yAxisLims'][1]
        ax.set_ylim([y0,y1])
    if (('axisLims','xAxisLims',) not in keyword_parameters):
        ax.set_ylim(bottom=0)
    if ('annotate' in keyword_parameters):
        for ii,var in enumerate(keyword_parameters['annotate']):
            annotation_text=var
            annotate_x1=date2num(parser.parse(keyword_parameters['annotatePointXY']['time'][ii]))
            annotate_y1=keyword_parameters['annotatePointXY']['height'][ii]
            annotate_x2=date2num(parser.parse(keyword_parameters['annotateTextXY']['time'][ii]))
            annotate_y2=keyword_parameters['annotateTextXY']['height'][ii]
            ax.annotate(annotation_text,
                    xy=(annotate_x1, annotate_y1), xycoords='data',
                    xytext=(annotate_x2, annotate_y2), textcoords='data',
                    arrowprops=dict(arrowstyle="->"),
                    horizontalalignment='center', verticalalignment='bottom')
    plt.grid(True)
    fig.autofmt_xdate(rotation=45)
    plt.tight_layout()
    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)
        plt.close()

def generateTimeSeriesSubplots(inputData,TimeIndex,timeseries_plots,nRows,nCols,xAxisName='',yAxisName='',fname='text.png',plot_or_save='save',**keyword_parameters):
## generateTimeSeriesSubplots wants input timeseries plot lists and the number of rols and cols:
    fig, axs = plt.subplots(nRows, nCols, figsize=(10, 4.8), dpi=100)
    for ii, var in enumerate(timeseries_plots):
        axs[ii].plot(inputData[TimeIndex], inputData[var], label=var,markersize=1,marker='.',linestyle = 'solid')
        axs[ii].set_title(var)
        axs[ii].set_xlabel(xAxisName)  # Add an x-label to the axes.
        axs[ii].set_ylabel(yAxisName)  # Add a y-label to the axes.
        axs[ii].grid(True)
        if ('axisLims' in keyword_parameters):
            x0=parser.parse(keyword_parameters['axisLims'][0])
            x1=parser.parse(keyword_parameters['axisLims'][1])
            y0=keyword_parameters['axisLims'][2]
            y1=keyword_parameters['axisLims'][3]
            axs[ii].set_xlim([x0,x1])
            axs[ii].set_ylim([y0,y1])
        if ('xAxisLims' in keyword_parameters):
            x0=parser.parse(keyword_parameters['xAxisLims'][0])
            x1=parser.parse(keyword_parameters['xAxisLims'][1])
            axs[ii].set_xlim([x0,x1])
        if ('yAxisLims' in keyword_parameters):
            y0=keyword_parameters['yAxisLims'][0]
            y1=keyword_parameters['yAxisLims'][1]
            axs[ii].set_ylim([y0,y1])
        if ('annotate' in keyword_parameters):
            annotation_text=keyword_parameters['annotate']
            annotate_x1=date2num(parser.parse(keyword_parameters['annotatePointXY'][0]))
            annotate_y1=keyword_parameters['annotatePointXY'][1]
            annotate_x2=date2num(parser.parse(keyword_parameters['annotateTextXY'][0]))
            annotate_y2=keyword_parameters['annotateTextXY'][1]
            ax.annotate(annotation_text,
                    xy=(annotate_x1, annotate_y1), xycoords='data',
                    xytext=(annotate_x2, annotate_y2), textcoords='data',
                    arrowprops=dict(arrowstyle="->"),
                    horizontalalignment='right', verticalalignment='bottom')
        

    fig.autofmt_xdate(rotation=45)
    plt.tight_layout()

    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)
        plt.close()


def generateTimeSeriesDisplaced(inputData,TimeIndex,timeseries_plots,dispFactor,dispRef,title,xAxisName,yAxisName,fname='test.png',plot_or_save='save',**keyword_parameters):
## generateTimeSeriesDisplaced makes time series plots and offsets them vertically.
# The vertical offset is set as a constant value (dispFactor). The normalisation can be chosen (dispRef), with a choice of 'initial' referencing all to the initial value (and excluding any initial Null values e.g. NaN).
# define axis limits with axisLims=[1,2,3,4] where these are the x_min,x_max,y_min,y_max
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=100)
    for ii, var in enumerate(timeseries_plots):
        if dispRef=='initial':
            offsetFactor = dispFactor
            offsetRef = inputData[var].loc[~inputData[var].isnull()].iloc[0]
        x0=inputData[TimeIndex].min()
        x1=inputData[TimeIndex].max()
        colour=next(ax._get_lines.prop_cycler)['color']
        ax.plot(inputData[TimeIndex],offsetFactor*(len(timeseries_plots)-ii-1)+inputData[var]-offsetRef, label=var,markersize=1,marker='None',linestyle = 'solid',color=colour)
        ax.plot([x0,x1], [(dispFactor*ii),(dispFactor*ii)], label=None,linestyle = 'solid',color=(0.8, 0.8, 0.8))
        ax.set_xlabel(xAxisName)  # Add an x-label to the axes.
        ax.set_ylabel(yAxisName)  # Add a y-label to the axes.
        ax.grid(False)
        plt.tight_layout()

    ax.set_title(title)
    ax.legend(loc=(1.05, 0.5), edgecolor='None', markerscale=1.8)
    if ('axisLims' in keyword_parameters):
        x0=parser.parse(keyword_parameters['axisLims'][0])
        x1=parser.parse(keyword_parameters['axisLims'][1])
        y0=keyword_parameters['axisLims'][2]
        y1=keyword_parameters['axisLims'][3]
        ax.set_xlim([x0,x1])
        ax.set_ylim([y0,y1])
    if ('xAxisLims' in keyword_parameters):
        x0=parser.parse(keyword_parameters['xAxisLims'][0])
        x1=parser.parse(keyword_parameters['xAxisLims'][1])
        ax.set_xlim([x0,x1])
    if ('yAxisLims' in keyword_parameters):
        y0=keyword_parameters['yAxisLims'][0]
        y1=keyword_parameters['yAxisLims'][1]
        ax.set_ylim([y0,y1])
    if (('axisLims','xAxisLims',) not in keyword_parameters):
        ax.set_xlim([x0,x1])
    if ('annotate' in keyword_parameters):
        annotation_text=keyword_parameters['annotate']
        annotate_x1=date2num(parser.parse(keyword_parameters['annotatePointXY'][0]))
        annotate_y1=keyword_parameters['annotatePointXY'][1]
        annotate_x2=date2num(parser.parse(keyword_parameters['annotateTextXY'][0]))
        annotate_y2=keyword_parameters['annotateTextXY'][1]
        ax.annotate(annotation_text,
                xy=(annotate_x1, annotate_y1), xycoords='data',
                xytext=(annotate_x2, annotate_y2), textcoords='data',
                arrowprops=dict(arrowstyle="->"),
                horizontalalignment='right', verticalalignment='bottom')

    plt.grid(True,axis='x')
    fig.autofmt_xdate(rotation=45)
    plt.tight_layout()

    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)
        plt.close()

def generateTimeSeriesDisplacedMinMaxAvg(inputData,TimeIndex,timeseries_plots_min, timeseries_plots_max,timeseries_plots_avg,beards,dispFactor,dispRef,title='',xAxisName='',yAxisName='',fname='test.png',plot_or_save='plot',**keyword_parameters):
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
# dispFactor = value to offset vertically
# dispRef = method to offset by. e.g. 'initial' references to initial value.
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=100)
    for ii,var in enumerate(timeseries_plots_avg):
        if dispRef=='initial':
            offsetFactor = dispFactor
            if ('resetOffset' in keyword_parameters):
                resetDates=keyword_parameters['resetOffset']
                offsetRef = np.zeros(inputData[var].size)
                for tt,ttdate in enumerate(resetDates):
                    if tt==0:        
                        if inputData[var].loc[inputData[TimeIndex]==ttdate].isna().bool(): #if date is nan
                            offsetRef[(inputData[TimeIndex]<ttdate)]= inputData[var].loc[~inputData[var].isnull()].iloc[0]
                            offsetRef[(inputData[TimeIndex]>=ttdate)]=inputData[var].bfill().loc[inputData[TimeIndex]==ttdate]
                        else:
                            offsetRef[(inputData[TimeIndex]<ttdate)]= inputData[var].loc[~inputData[var].isnull()].iloc[0]
                            offsetRef[(inputData[TimeIndex]>=ttdate)]= inputData[var].loc[inputData[TimeIndex]==ttdate]
                    else:
                        if inputData[var].loc[inputData[TimeIndex]==ttdate].isna().bool(): #if date is nan
                            offsetRef[ inputData[TimeIndex] >=resetDates[tt]] = inputData[var].bfill().loc[inputData[TimeIndex]==ttdate]
                        else:
                            offsetRef[ inputData[TimeIndex] >=resetDates[tt]] = inputData[var].loc[inputData[TimeIndex]==ttdate]
            elif ('resetOffset' not in keyword_parameters):
                offsetRef = inputData[var].loc[~inputData[var].isnull()].iloc[0]
        if beards==True:
            ax.fill_between(inputData[TimeIndex], offsetFactor*(len(timeseries_plots_max)-ii-1)+inputData[timeseries_plots_max[ii]]-offsetRef, offsetFactor*(len(timeseries_plots_min)-ii-1)+inputData[timeseries_plots_min[ii]]-offsetRef, alpha=0.5)
        else:
            ax.plot(inputData[TimeIndex], offsetFactor*(len(timeseries_plots_max)-ii-1)+inputData[timeseries_plots_max[ii]]-offsetRef, label=None,markersize=1,marker='.',linestyle = 'solid',color=(0.8, 0.8, 0.8))
            ax.plot(inputData[TimeIndex], offsetFactor*(len(timeseries_plots_min)-ii-1)+inputData[timeseries_plots_min[ii]]-offsetRef, label=None,markersize=1,marker='.',linestyle = 'solid',color=(0.8, 0.8, 0.8))

    for ii,var in enumerate(timeseries_plots_avg):
        if dispRef=='initial':
            offsetFactor = dispFactor
            if ('resetOffset' in keyword_parameters):
                resetDates=keyword_parameters['resetOffset']
                offsetRef = np.zeros(inputData[var].size)
                for tt,ttdate in enumerate(resetDates):
                    if tt==0:        
                        if inputData[var].loc[inputData[TimeIndex]==ttdate].isna().bool(): #if date is nan
                            offsetRef[(inputData[TimeIndex]<ttdate)]= inputData[var].loc[~inputData[var].isnull()].iloc[0]
                            offsetRef[(inputData[TimeIndex]>=ttdate)]=inputData[var].bfill().loc[inputData[TimeIndex]==ttdate]
                        else:
                            offsetRef[(inputData[TimeIndex]<ttdate)]= inputData[var].loc[~inputData[var].isnull()].iloc[0]
                            offsetRef[(inputData[TimeIndex]>=ttdate)]= inputData[var].loc[inputData[TimeIndex]==ttdate]
                    else:
                        if inputData[var].loc[inputData[TimeIndex]==ttdate].isna().bool(): #if date is nan
                            offsetRef[ inputData[TimeIndex] >=resetDates[tt]] = inputData[var].bfill().loc[inputData[TimeIndex]==ttdate]
                        else:
                            offsetRef[ inputData[TimeIndex] >=resetDates[tt]] = inputData[var].loc[inputData[TimeIndex]==ttdate]
            elif ('resetOffset' not in keyword_parameters):
                offsetRef = inputData[var].loc[~inputData[var].isnull()].iloc[0]
        x0=inputData[TimeIndex].min()
        x1=inputData[TimeIndex].max()
        colour=next(ax._get_lines.prop_cycler)['color']
        ax.plot(inputData[TimeIndex], offsetFactor*(len(timeseries_plots_avg)-ii-1)+inputData[timeseries_plots_avg[ii]]-offsetRef, label=var,markersize=1,marker='None',linestyle = 'solid',color=colour)
        ax.plot([x0,x1], [(dispFactor*ii),(dispFactor*ii)], label=None,linestyle = 'solid',color=(0.8, 0.8, 0.8))
        if ('resetOffset' in keyword_parameters):
            resetDates=keyword_parameters['resetOffset']
            for tt,ttdate in enumerate(resetDates):
                ax.axvline(x=parser.parse(ttdate),color='black')
    ax.set_xlabel(xAxisName)  # Add an x-label to the axes.
    ax.set_ylabel(yAxisName)  # Add a y-label to the axes.
    ax.set_title(title)  # Add a title to the axes.
    if ('axisLims' in keyword_parameters):
        x0=parser.parse(keyword_parameters['axisLims'][0])
        x1=parser.parse(keyword_parameters['axisLims'][1])
        y0=keyword_parameters['axisLims'][2]
        y1=keyword_parameters['axisLims'][3]
        ax.set_xlim([x0,x1])
        ax.set_ylim([y0,y1])
    if ('xAxisLims' in keyword_parameters):
        x0=parser.parse(keyword_parameters['xAxisLims'][0])
        x1=parser.parse(keyword_parameters['xAxisLims'][1])
        ax.set_xlim([x0,x1])
    if ('yAxisLims' in keyword_parameters):
        y0=keyword_parameters['yAxisLims'][0]
        y1=keyword_parameters['yAxisLims'][1]
        ax.set_ylim([y0,y1])
    if (('axisLims','xAxisLims',) not in keyword_parameters):
        ax.set_xlim([x0,x1])
    if ('annotate' in keyword_parameters):
        annotation_text=keyword_parameters['annotate']
        annotate_x1=date2num(parser.parse(keyword_parameters['annotatePointXY'][0]))
        annotate_y1=keyword_parameters['annotatePointXY'][1]
        annotate_x2=date2num(parser.parse(keyword_parameters['annotateTextXY'][0]))
        annotate_y2=keyword_parameters['annotateTextXY'][1]
        ax.annotate(annotation_text,
                xy=(annotate_x1, annotate_y1), xycoords='data',
                xytext=(annotate_x2, annotate_y2), textcoords='data',
                arrowprops=dict(arrowstyle="->"),
                horizontalalignment='right', verticalalignment='bottom')
    ax.legend(loc=(1.05, 0.5), edgecolor='None', markerscale=1.8)
    plt.grid(True,axis='x')
    fig.autofmt_xdate(rotation=45)
    plt.tight_layout()
    

    
    
    
    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)
        plt.close()
