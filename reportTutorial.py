import time # this module allows interaction with the current
import pandas as pd
import plotly.graph_objects as go
import plotly
import datetime
import numpy as np
from fpdf import FPDF

# load some of our own local functions - in this tutorial it is just the 3 types of plots.
from functions.fun_generateTimeSeriesPlots import generateTimeSeriesPlot
from functions.fun_generateTimeSeriesPlots import generateTimeSeriesMinMaxAvg
from functions.fun_generateTimeSeriesPlots import generateTimeSeriesDisplacedMinMaxAvg


# define some things in the Config file.
SS_filename = '../SampleData/HE602_3680_RV50_CCB_SB_SensorStats.dat'
output_name = str(f"{datetime.datetime.now():%Y_%m_%d}"+'.tutorial.draft.pdf')
logo_path = 'assets/logo.png' ## This logo is obviously not necessary, but I've built the PDF class to expect a logo in the top corner.
title = 'Tutorial PDF'
author = 'Tutorial made on the: '+f"{datetime.datetime.now():%d-%b-%Y}" # note that these can be set blank e.g. author = ''

# Load data from a *.dat file
print('loading data from '+SS_filename)
print('this does the same as the loadData function')
df_SS = pd.read_csv(SS_filename,header=1, skiprows=[2,3], na_values='NAN')
df_SS=df_SS.astype({'TIMESTAMP': 'datetime64'})
colNamesSS = list(df_SS.columns)

print('define data in a dictionary (defined as ''name'':''definition'')')
print('could also load this data from a file, as in loadAliasTable function')
aliasTableName = {
    "TIMESTAMP":"TIMESTAMP",
    "RECORD":"record",
    "L_SB_HJ3_B1_Min":"L_SB_HJ3_B1_Min",
"L_SB_HJ3_B2_Min":"L_SB_HJ3_B2_Min",
"L_SB_HJ3_B3_Min":"L_SB_HJ3_B3_Min",
"L_SB_HJ3_B123_Min":"L_SB_HJ3_B123_Min",
"DF_SB_HJ3_B1_Min":"DF_SB_HJ3_B1_Min",
"DF_SB_HJ3_B2_Min":"DF_SB_HJ3_B2_Min",
"DF_SB_HJ3_B3_Min":"DF_SB_HJ3_B3_Min",
"L_SB_HJ3_B1_Avg":"L_SB_HJ3_B1_Avg",
"L_SB_HJ3_B2_Avg":"L_SB_HJ3_B2_Avg",
"L_SB_HJ3_B3_Avg":"L_SB_HJ3_B3_Avg",
"L_SB_HJ3_B123_Avg":"L_SB_HJ3_B123_Avg",
"DF_SB_HJ3_B1_Avg":"DF_SB_HJ3_B1_Avg",
"DF_SB_HJ3_B2_Avg":"DF_SB_HJ3_B2_Avg",
"DF_SB_HJ3_B3_Avg":"DF_SB_HJ3_B3_Avg",
"L_SB_HJ3_B1_Max":"L_SB_HJ3_B1_Max",
"L_SB_HJ3_B2_Max":"L_SB_HJ3_B2_Max",
"L_SB_HJ3_B3_Max":"L_SB_HJ3_B3_Max",
"L_SB_HJ3_B123_Max":"L_SB_HJ3_B123_Max",
"DF_SB_HJ3_B1_Max":"DF_SB_HJ3_B1_Max",
"DF_SB_HJ3_B2_Max":"DF_SB_HJ3_B2_Max",
"DF_SB_HJ3_B3_Max":"DF_SB_HJ3_B3_Max",
"microS2T20_Min(7)":"S_SB_HJ3_S1D_Min",
"microS2T20_Min(8)":"S_SB_HJ3_S1V_Min",
"microS2T20_Max(7)":"S_SB_HJ3_S1D_Max",
"microS2T20_Max(8)":"S_SB_HJ3_S1V_Max",
"microS2T20_Avg(7)":"S_SB_HJ3_S1D_Avg",
"microS2T20_Avg(8)":"S_SB_HJ3_S1V_Avg"
}

print('apply alias table')
print('this is the same as in the applyAliasTable function')
df_SS.rename(columns=aliasTableName, inplace=True)

# # Trim data
print('do some trimming of data using method used in removeVariableBetweenDates function')
trimVariable=['L_SB_HJ3_B123_Min','L_SB_HJ3_B123_Max','L_SB_HJ3_B123_Avg',
              'L_SB_HJ3_B2_Min','L_SB_HJ3_B2_Max','L_SB_HJ3_B2_Avg',
              'L_SB_HJ3_B3_Min','L_SB_HJ3_B3_Max','L_SB_HJ3_B3_Avg',
              'DF_SB_HJ3_B1_Min','DF_SB_HJ3_B1_Max','DF_SB_HJ3_B1_Avg',
              'DF_SB_HJ3_B2_Min','DF_SB_HJ3_B2_Max','DF_SB_HJ3_B2_Avg',
              'DF_SB_HJ3_B3_Min','DF_SB_HJ3_B3_Max','DF_SB_HJ3_B3_Avg']
trimStart=  ['2020-SEP-15 16:00']
trimEnd=    ['2020-SEP-15 16:15']
# df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd) ## The lines below make up this function.
for ii,var in enumerate(trimVariable):
    for r in range(0,len(trimStart)):
        mask = (df_SS["TIMESTAMP"]>=trimStart[r]) & (df_SS["TIMESTAMP"]<=trimEnd[r])
        df_SS[var] = df_SS[var].where(~mask, other=np.NaN)

# # Realign data
print('now re-align some variables by shifting data vertically beyond a specified date')
variablesToRealign=['S_SB_HJ3_S1D_Avg','S_SB_HJ3_S1D_Min','S_SB_HJ3_S1D_Max',
                    'S_SB_HJ3_S1V_Avg','S_SB_HJ3_S1V_Min','S_SB_HJ3_S1V_Max']
shiftTimes=['2020-SEP-16 01:30','2020-SEP-16 01:30','2020-SEP-16 01:30',
            '2020-SEP-18 01:30','2020-SEP-18 01:30','2020-SEP-18 01:30']
shiftValues=[64.4, 64.4, 64.4,
             17.3, 17.3, 17.3]
# joinOffsetData(df_SS,"TIMESTAMP",variablesToRealign,shiftTimes,shiftValues) ## The lines below make up this function call.
for r,var in enumerate(variablesToRealign):
    mask = (df_SS["TIMESTAMP"]>=shiftTimes[r])
    df_SS[var].where(~mask, other=df_SS[var]+shiftValues[r],inplace=True)

# # Add NaN in any time gaps
print ('now add NaN to any time gaps')
# df_SS=addNANGaps(df_SS,"TIMESTAMP",'5Min') ## This function call is equivalent to the lines below.
df_SS = df_SS.set_index("TIMESTAMP").asfreq('5Min').reset_index()

print('now start making plots.')
print('we will make a time series plot, a beard plot and a displaced beard plot.')

print('first the time series plot')
print('we define what and how we want to plot in the config file, like below.')
NoTimeSeriesPlots = 1
timeseries_plot1 = ["A116_BattV_Avg","BattV_Avg"]
keyword_parameters_ts1={'addHighlight':'None',
                     'yAxisName':'Voltage (V)',
                     'xAxisName':'',
                     'yAxisLims':'None',
                     'xAxisLims':'None', #['2020-8-27 09:00','2020-8-27 12:30']
                     'annotate': 'None',
                     'annotatePointXY': {'time':['26-07-2020 15:40'],'height':[15]},
                     'annotateTextXY': {'time':['26-07-2020 15:40'],'height':[10]},
                     'xTickFormat':['%d-%m','weekly'],
                     'plot_or_save':'save'
                    }
caption_timeseries1=''
for ii in range(1,NoTimeSeriesPlots+1):
    fcn_keywordparameters=eval('keyword_parameters_ts'+str(ii))
    generateTimeSeriesPlot(inputData=df_SS,
                            TimeIndex="TIMESTAMP",
                            timeseries_plots=eval('timeseries_plot'+str(ii)),
                            lines_or_markers='lines',
                            title='',
                            fname='test_timeseries'+str(ii)+'.png',
                            **fcn_keywordparameters)

print('now we will plot a beard plot.')
print('like before, define plot settings in the config file.')
NoTimeSeriesWithBeards=1
timeseries_plots_min1=[ 'L_SB_HJ3_B1_Min',
                        'L_SB_HJ3_B2_Min',
                        'L_SB_HJ3_B3_Min',
                        'L_SB_HJ3_B123_Min']
timeseries_plots_max1=[ 'L_SB_HJ3_B1_Max',
                        'L_SB_HJ3_B2_Max',
                        'L_SB_HJ3_B3_Max',
                        'L_SB_HJ3_B123_Max']
timeseries_plots_avg1=[ 'L_SB_HJ3_B1_Avg',
                        'L_SB_HJ3_B2_Avg',
                        'L_SB_HJ3_B3_Avg',
                        'L_SB_HJ3_B123_Avg']
title_Beards1='Bearing Loads (Minimum, Average & Maximum)'
yAx_Beards1='Bearing load (t)'
keyword_parameters1={'yAxisLims':'None',
                     'xAxisLims':'None', #['2020-8-27 09:00','2020-8-27 12:30']
                     'annotate': 'None',
                     'annotatePointXY': {'time':['26-07-2020 15:40'],'height':[15]},
                     'annotateTextXY': {'time':['26-07-2020 15:40'],'height':[10]},
                     'xTickFormat':['%d-%m','weekly'],
                     'plot_or_save':'save'
                    }
caption_Beards1=''
for ii in range(1,NoTimeSeriesWithBeards+1):
    fcn_keywordparameters=eval('keyword_parameters'+str(ii))
    generateTimeSeriesMinMaxAvg(inputData=df_SS,
                                TimeIndex="TIMESTAMP",
                                timeseries_plots_min=eval('timeseries_plots_min'+str(ii)),
                                timeseries_plots_max=eval('timeseries_plots_max'+str(ii)),
                                timeseries_plots_avg=eval('timeseries_plots_avg'+str(ii)),
                                beards=True,
                                title=eval('title_Beards'+str(ii)),
                                xAxisName='',
                                yAxisName=eval('yAx_Beards'+str(ii)),
                                fname='test_timeseriesBeards'+str(ii)+'.png',
                                **fcn_keywordparameters)

print('now plot the displaced beard plots.')
# you will notice that when you plot this, you can't see any lines!
# try changing 'plot_or_save' to 'plot', then use the zoom/pan tool to explore the data.
# you might also notice that the ticks aren't showing when you zoom - this is because you've changed the 'xTickFormat' - trying changing back to 'auto'
# now look for the location of 'bad' data. Looks like two locations:
# 26-AUG-2020 07:50 to 07:55 for both datasets AND
# 25-AUG-2020 11:45 to 11:50 for both datasets.
# now try adding a remove line for this data.
# hint: should have this structure:
# trimVariable=['variable1_Min','variable1_Max','variable1_Avg',
#               'variable2_Min','variable2_Max','variable2_Avg',
#               'variable3_Min','variable3_Max','variable3_Avg']
# trimStart=  [  '2020-SEP-15 16:00',
#                '2020-AUG-day hh:mm'] # and you can have multiple start/end dates
# trimEnd=    [  '2020-SEP-15 16:15',
#                '2020-AUG-26 hh:mm']

NoTimeSeriesDisplacedMinMaxAvg=1
timeseries_plots_displaced_min1=[   'S_SB_HJ3_S1D_Min',
                                    'S_SB_HJ3_S1V_Min']
timeseries_plots_displaced_max1=[   'S_SB_HJ3_S1D_Max',
                                    'S_SB_HJ3_S1V_Max']
timeseries_plots_displaced_avg1=[   'S_SB_HJ3_S1D_Avg',
                                    'S_SB_HJ3_S1V_Avg']
dispFactorMMA1=25
dispRefMMA1='initial'
title_dispMMA1='Strain (Vibrating Wire Sensor Group 2 - Min, Avg, Max, '+str(dispFactorMMA1)+'ue offset, temperature corrected)'
yAx_dispMMA1=r'Microstrain ($\mu \epsilon$)'
keyword_parametersDisp1={'yAxisLims':'None', #[-50,400],
                         'xAxisLims':'None', #['2020-8-27 09:00','2020-8-27 12:30']
                         'xTickFormat':['%d-%m','weekly'],
                         'plot_or_save':'save'
                         }
for ii in range(1,NoTimeSeriesDisplacedMinMaxAvg+1):
    fcn_keywordparameters=eval('keyword_parametersDisp'+str(ii))
    generateTimeSeriesDisplacedMinMaxAvg(inputData=df_SS,
                                            TimeIndex="TIMESTAMP",
                                            timeseries_plots_min=eval('timeseries_plots_displaced_min'+str(ii)),
                                            timeseries_plots_max=eval('timeseries_plots_displaced_max'+str(ii)),
                                            timeseries_plots_avg=eval('timeseries_plots_displaced_avg'+str(ii)),
                                            beards=True,
                                            dispFactor=eval('dispFactorMMA'+str(ii)),
                                            dispRef=eval('dispRefMMA'+str(ii)),
                                            title=eval('title_dispMMA'+str(ii)),
                                            xAxisName='',
                                            yAxisName=eval('yAx_dispMMA'+str(ii)),
                                            fname='test_timeseriesDisplacedMinMaxAvg'+str(ii)+'.png',
                                            **fcn_keywordparameters)


print('load the ''class'' file from ClassPDF.py')
from functions.ClassPDF import ClassPDF

## COMPILE PDF
print('some standard commands are necessary, such as initialising the ClassPDF object.')
pdf = ClassPDF(logo_path=logo_path,title=title,author=author)
pdf.set_title(title) # change metadata title
pdf.set_author(author) # change metadata author

#import template file
print('the below section is mostly capturing the ''template'' file.')
pdf.print_sectionHeader(1, 'First section') #make a section header
pdf.print_text('here are some notes, that can be added here, or defined in the config file and called here.') #add text. can also be used for captions.
pdf.print_sectionHeader(2, '2nd section')
for ii in range(1,NoTimeSeriesPlots+1):
    pdf.print_timeSeriesPlot('test_timeseriesBeards'+str(ii)+'.png',190,eval('caption_Beards'+str(ii)))
pdf.print_sectionHeader(3, '3rd section')
for ii in range(1,NoTimeSeriesWithBeards+1):
    pdf.print_timeSeriesPlot('test_timeseriesBeards'+str(ii)+'.png',190,eval('caption_Beards'+str(ii)))
pdf.print_sectionHeader(4, '4th section')
for ii in range(1,NoTimeSeriesDisplacedMinMaxAvg+1):
    pdf.print_timeSeriesPlot('test_timeseriesDisplacedMinMaxAvg'+str(ii)+'.png',190,'')


print('making PDF')
pdf.output(output_name, 'F')
