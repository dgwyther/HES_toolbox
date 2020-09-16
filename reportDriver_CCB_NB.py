import time
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
from functions.fun_joinOffsetData import joinOffsetData

# DEFINE TEMPLATE AND CONFIG FILE:
configFile = 'reportConfig_CCB_NB.py'
templateFile = 'reportTemplate_CCB_NB.py'
dataPrepFile = 'reportDataPrep_CCB_NB.py'

########################### No edits below. ##############################
#import config file
tic = time.time()
print('starting compiling report at '+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print('defining configuration for report')
exec(open(configFile).read())

# Load data
if 'SS_filename' in locals():
    print('loading data from '+SS_filename)
    df_SS,colNamesSS = loadData(SS_filename,"TIMESTAMP")
if 'SRES_filename' in locals():
    print('loading data from '+SRES_filename)
    df_SRES,colNamesSRES = loadData(SRES_filename,"TIMESTAMP")

# Alias data
if loadAlias=='csv':
    aliasTable_FromCSV=readAliasCSV(aliasTablePath)
    applyAliasTable(df_SS,aliasTable_FromCSV)
elif loadAlias=='dict':
    applyAliasTable(df_SS,aliasTable)


# # Trim data
print('trimming data')
if 'dataPrepFile' in locals():
    exec(open(dataPrepFile).read())
    print('Data trimmed and re-aligned from the file '+dataPrepFile)

# Add NaN in any time gaps
if 'SS_filename' in locals():
    df_SS=addNANGaps(df_SS,"TIMESTAMP",'5Min')

## GENERATE PLOTS
print('generating plots:')
if NoTimeSeriesWithBeards!=0:
    print(str(NoTimeSeriesWithBeards)+' beard plots')
if NoTimeSeriesSubplots!=0:
    print(str(NoTimeSeriesSubplots)+' subplots')
if NoTimeSeriesDisplacedMinMaxAvg!=0:
    print(str(NoTimeSeriesDisplacedMinMaxAvg)+' displaced beard plots')
if NoTimeSeriesPlots!=0:
    print(str(NoTimeSeriesPlots)+' standard timeseries plots')
if NoXYPlots!=0:
    print(str(NoXYPlots)+' X-Y plots')
if NoInvNormPlots!=0:
    print(str(NoInvNormPlots)+' inverse normal plots')

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

for ii in range(1,NoTimeSeriesPlots+1):
    fcn_keywordparameters=eval('keyword_parameters_ts'+str(ii))
    generateTimeSeriesPlot(inputData=df_SS,
                            TimeIndex="TIMESTAMP",
                            timeseries_plots=eval('timeseries_plot'+str(ii)),
                            lines_or_markers='lines',
                            title='',
                            fname='test_timeseries'+str(ii)+'.png',
                            **fcn_keywordparameters)
    #generateTimeSeriesPlotZoomed(df_SS,"TIMESTAMP",eval('timeseries_plot'+str(ii)),'a temporary title','test_timeseries_zoom'+str(ii)+'.png','save')

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
print('laying out report')
exec(open(templateFile).read())
print('making PDF')
pdf.output(output_name, 'F')
toc = time.time()
print('done at '+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+', elapsed time '+str(round(toc-tic,1))+'s')
