import pandas as pd
import plotly.graph_objects as go
import plotly
import datetime
import numpy as np
from fpdf import FPDF

#own functions
from functions.fun_removeBetweenDates import removeBetweenDates
from functions.fun_removeVariableBetweenDates import removeVariableBetweenDates
from functions.fun_loadData import loadData
from functions.fun_applyAliasTable import applyAliasTable
from functions.fun_generateTimeSeriesPlots import generateTimeSeriesPlot
from functions.fun_generateTimeSeriesPlots import generateTimeSeriesPlotZoomed
from functions.fun_generateTimeSeriesPlots import generateTimeSeriesMinMaxAvg
from functions.fun_generateTimeSeriesPlots import generateTimeSeriesSubplots
from functions.fun_generateTimeSeriesPlots import generateTimeSeriesDisplaced
from functions.fun_generateTimeSeriesPlots import generateTimeSeriesDisplacedMinMaxAvg
from functions.fun_generateXYPlot import generateXYPlot
from functions.fun_generateInvNormPlot import generateInvNormPlot
from functions.fun_readAliasCSV import readAliasCSV
from functions.fun_addNANGaps import addNANGaps

# DEFINE TEMPLATE AND CONFIG FILE:
configFile = 'reportConfig_CCB_NB.py'
templateFile = 'reportTemplate_CCB_NB.py'

########################### No edits below. ##############################

#import config file
exec(open(configFile).read())

# Load data
if 'SS_filename' in locals():
    df_SS,colNamesSS = loadData(SS_filename,"TIMESTAMP")
if 'SRES_filename' in locals():
    df_SRES,colNamesSRES = loadData(SRES_filename,"TIMESTAMP")

# Alias data
if loadAlias=='csv':
    aliasTable_FromCSV=readAliasCSV(aliasTablePath)
    applyAliasTable(df_SS,aliasTable_FromCSV)
elif loadAlias=='dict':
    applyAliasTable(df_SS,aliasTable)
    
    
# Trim data
trimVariable=['S_NB_HJ3_S2B_Min','S_NB_HJ3_S2B_Avg','S_NB_HJ3_S2B_Max']
trimStart=  ['2020-JUL-26 13:20',
            '2020-JUL-26 13:50',
            '2020-JUL-26 14:30',
            '2020-JUL-26 14:50',
            '2020-JUL-26 15:10',
            '2020-AUG-4 08:40',
            '2020-AUG-6 10:10',
            '2020-AUG-6 10:20']
trimEnd=    ['2020-JUL-26 13:30',
            '2020-JUL-26 14:00',
            '2020-JUL-26 14:50',
            '2020-JUL-26 15:05',
            '2020-JUL-26 15:20',
            '2020-AUG-4 08:50',
            '2020-AUG-06 10:20',
            '2020-AUG-06 10:30']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['S_NB_HJ3_S1H_Min','S_NB_HJ3_S1H_Avg','S_NB_HJ3_S1H_Max']
trimStart=  ['2020-AUG-06 14:00']
trimEnd=    ['2020-AUG-06 14:10']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['S_NB_HJ3_S2D_Min','S_NB_HJ3_S2D_Avg','S_NB_HJ3_S2D_Max']
trimStart=  ['2020-AUG-07 01:15']
trimEnd=    ['2020-AUG-07 01:25']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['S_NB_HJ3_S1V_Min','S_NB_HJ3_S1V_Avg','S_NB_HJ3_S1V_Max']
trimStart=  ['2020-AUG-06 14:00']
trimEnd=    ['2020-AUG-06 14:10']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['S_NB_HJ3_S3H_Min','S_NB_HJ3_S3H_Avg','S_NB_HJ3_S3H_Max']
trimStart=  ['2020-AUG-06 14:15']
trimEnd=    ['2020-AUG-06 14:25']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)



trimVariable=['S_NB_HJ3_C3H_Min','S_NB_HJ3_C3H_Avg','S_NB_HJ3_C3H_Max']
trimStart=  ['2020-AUG-6 14:25',
            '2020-AUG-7 16:05',
            '2020-AUG-08 00:25',
            '2020-AUG-08 00:40',
            '2020-AUG-08 06:30',
            '2020-AUG-08 06:55',
            '2020-AUG-08 07:15',
            '2020-AUG-08 22:00',
            '2020-AUG-08 22:35',
            '2020-AUG-09 10:15',
            '2020-AUG-09 19:45',
            '2020-AUG-09 23:10',
            '2020-AUG-10 00:20',
            '2020-AUG-10 00:40',
            '2020-AUG-10 01:25',
            '2020-AUG-10 02:05',
            '2020-AUG-10 02:35']
trimEnd=    ['2020-AUG-6 14:35',
            '2020-AUG-7 16:15',
            '2020-AUG-08 00:35',
            '2020-AUG-08 01:10',
            '2020-AUG-08 06:40',
            '2020-AUG-08 07:05',
            '2020-AUG-08 07:25',
            '2020-AUG-08 22:15',
            '2020-AUG-08 23:00',
            '2020-AUG-09 10:30',
            '2020-AUG-09 19:55',
            '2020-AUG-09 23:40',
            '2020-AUG-10 00:35',
            '2020-AUG-10 00:55',
            '2020-AUG-10 01:35',
            '2020-AUG-10 02:10',
            '2020-AUG-10 02:40']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)



# Add NaN in any time gaps
if 'SS_filename' in locals():
    df_SS=addNANGaps(df_SS,"TIMESTAMP",'5Min')

## GENERATE PLOTS

for ii in range(1,NoTimeSeriesWithBeards+1):
    if ii==3:
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
                            plot_or_save='save',
                            annotate=eval('annotation'+str(ii)),
                            annotatePointXY=eval('annotatePointXY'+str(ii)),
                            annotateTextXY=eval('annotateTextXY'+str(ii))
                            )
    else:
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
                                    plot_or_save='save')
                                    #,
                                    #xAxisLims=['2020-7-26 00:00','2020-7-27 00:00'])

for ii in range(1,NoTimeSeriesSubplots+1):
    generateTimeSeriesSubplots(df_SS,
                                TimeIndex="TIMESTAMP",
                                timeseries_plots=eval('timeseries_plots_subplot'+str(ii)),
                                nRows=nRows,
                                nCols=nCols,
                                xAxisName='',
                                yAxisName=eval('yAx_subplot'+str(ii)),
                                fname='test_timeseriesSubplots'+str(ii)+'.png',
                                plot_or_save='save')
                                #,
                                #xAxisLims=['2020-7-26 00:00','2020-7-27 00:00'])

for ii in range(1,NoTimeSeriesDisplaced+1):
    generateTimeSeriesDisplaced(inputData=df_SS,
                                TimeIndex="TIMESTAMP",
                                timeseries_plots=eval('timeseries_plots_displaced'+str(ii)),
                                dispFactor=eval('dispFactor'+str(ii)),
                                dispRef=eval('dispRef'+str(ii)),
                                title=eval('title_disp'+str(ii)),
                                xAxisName='',
                                yAxisName=eval('yAx_disp'+str(ii)),
                                fname='test_timeseriesDisplaced'+str(ii)+'.png',
                                plot_or_save='save')
                                #,
                                #xAxisLims=['2020-7-26 00:00','2020-7-27 00:00'])

for ii in range(1,NoTimeSeriesDisplacedMinMaxAvg+1):
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
                                            plot_or_save='save')
                                            #,
                                            #xAxisLims=['2020-7-26 00:00','2020-7-27 00:00']
                                            #)
# ii=3
# generateTimeSeriesDisplacedMinMaxAvg(inputData=df_SS,
                                        # TimeIndex="TIMESTAMP",
                                        # timeseries_plots_min=eval('timeseries_plots_displaced_min'+str(ii)),
                                        # timeseries_plots_max=eval('timeseries_plots_displaced_max'+str(ii)),
                                        # timeseries_plots_avg=eval('timeseries_plots_displaced_avg'+str(ii)),
                                        # beards=True,
                                        # dispFactor=eval('dispFactorMMA'+str(ii)),
                                        # dispRef=eval('dispRefMMA'+str(ii)),
                                        # title=eval('title_dispMMA'+str(ii)),
                                        # xAxisName='',
                                        # yAxisName=eval('yAx_dispMMA'+str(ii)),
                                        # fname='test_timeseriesDisplacedMinMaxAvg'+str(ii)+'.png',
                                        # plot_or_save='save',
                                        # #axisLims=['2020-7-26','2020-7-27',0,100000],
                                        # xAxisLims=['2020-8-6 12:00','2020-8-6 15:00']
                                        # #yAxisLims=[80,220]
                                        # )



for ii in range(1,NoTimeSeriesPlots+1):
    generateTimeSeriesPlot(df_SS,"TIMESTAMP",eval('timeseries_plot'+str(ii)),'a temporary title','test_timeseries'+str(ii)+'.png','save')
    generateTimeSeriesPlotZoomed(df_SS,"TIMESTAMP",eval('timeseries_plot'+str(ii)),'a temporary title','test_timeseries_zoom'+str(ii)+'.png','save')

for ii in range(1,NoXYPlots+1):
    generateXYPlot(df_SRES,eval('XY_plot'+str(ii)),'linear',eval('XY_plot'+str(ii)+'_title'),'test_XY'+str(ii)+'.png','save')

for ii in range(1,NoInvNormPlots+1):
    generateInvNormPlot(df_SRES,"TIMESTAMP",eval('InvNorm_toPlot'+str(ii)),InvNormBinStart,InvNormBinInc,InvNormBinEnd,InvNormMin,InvNormMax,title_InvNorm,'test_InvNorm'+str(ii)+'.png','save')

## DEFINE CLASSES
from functions.ClassPDF import ClassPDF

## COMPILE PDF
pdf = ClassPDF(logo_path=logo_path,title=title,author=author)
pdf.set_title(title) # change metadata title
pdf.set_author(author) # change metadata author

#import config file
exec(open(templateFile).read())

pdf.output(output_name, 'F')