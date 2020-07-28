import pandas as pd
import plotly.graph_objects as go
import plotly
import datetime
import numpy as np
from fpdf import FPDF

#own functions
from functions.fun_removeDates import removeDates
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

# Trim data

# Alias data
#aliasTable_FromCSV=readAliasCSV('tmp.GAF_aliasTable.csv')
#or use value in reportTemplate with aliasTable_SRES
#applyAliasTable(df_SRES,aliasTable_FromCSV)

#df_SS.set_index('TIMESTAMP').resample('5min').first().reset_index()
#fig,ax=plt.subplots()
#ax.plot(df_SS['TIMESTAMP'],df_SS['T_NB_HJ3_BoTS_Max'])
#plt.show()
## GENERATE PLOTS

for ii in range(1,NoTimeSeriesWithBeards+1):
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