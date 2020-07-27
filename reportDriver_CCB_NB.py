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

#import template file
from reportTemplate_CCB_NB import *

# Load data
df_SS,colNamesSS = loadData(SS_filename,"TIMESTAMP")
#df_SRES,colNamesSRES = loadData(SRES_filename,"TIMESTAMP")

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
    generateTimeSeriesMinMaxAvg(df_SS,"TIMESTAMP",eval('timeseries_plots_min'+str(ii)),eval('timeseries_plots_max'+str(ii)),eval('timeseries_plots_avg'+str(ii)),True,'Beard plots','test_timeseriesBeards'+str(ii)+'.png','save')

for ii in range(1,NoTimeSeriesSubplots+1):
    generateTimeSeriesSubplots(df_SS,"TIMESTAMP",eval('timeseries_plots_subplot'+str(ii)),nRows,nCols,'test_timeseriesSubplots'+str(ii)+'.png','save')

for ii in range(1,NoTimeSeriesDisplaced+1):
    generateTimeSeriesDisplaced(df_SS,"TIMESTAMP",eval('timeseries_plots_displaced'+str(ii)),eval('dispFactor'+str(ii)),eval('dispRef'+str(ii)),'test_timeseriesDisplaced'+str(ii)+'.png','save')

for ii in range(1,NoTimeSeriesDisplacedMinMaxAvg+1):
    generateTimeSeriesDisplacedMinMaxAvg(df_SS,"TIMESTAMP",eval('timeseries_plots_displaced_min'+str(ii)),eval('timeseries_plots_displaced_max'+str(ii)),eval('timeseries_plots_displaced_avg'+str(ii)),True,eval('dispFactor'+str(ii)),eval('dispRef'+str(ii)),'Beard plots','test_timeseriesDisplacedMinMaxAvg'+str(ii)+'.png','save')

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
#
pdf.print_sectionHeader(1, 'Summary information')
#pdf.generateTableOverview(df_SRES,"TIMESTAMP",table_title,col_titles,sensorStatisticsFields,sensorStatisticsNames)
pdf.print_text(section1_notes)
#
pdf.print_sectionHeader(2, 'Beard plots')
for ii in range(1,NoTimeSeriesWithBeards+1):
    pdf.print_timeSeriesPlot('test_timeseriesBeards'+str(ii)+'.png',190,'A caption')

pdf.print_sectionHeader(3, 'Subplots')
for ii in range(1,NoTimeSeriesSubplots+1):
    pdf.print_timeSeriesPlot('test_timeseriesSubplots'+str(ii)+'.png',190,'A caption')

pdf.print_sectionHeader(4, 'Displaced timeseries')
for ii in range(1,NoTimeSeriesDisplaced+1):
    pdf.print_timeSeriesPlot('test_timeseriesDisplaced'+str(ii)+'.png',190,'A caption')

pdf.print_sectionHeader(5, 'Displaced timeseries with beards')
for ii in range(1,NoTimeSeriesDisplacedMinMaxAvg+1):
    pdf.print_timeSeriesPlot('test_timeseriesDisplacedMinMaxAvg'+str(ii)+'.png',190,'A caption')

for ii in range(1,NoTimeSeriesPlots+1):
    pdf.print_timeSeriesPlot('test_timeseries'+str(ii)+'.png',190,'A caption')
    pdf.print_timeSeriesPlotZoomed('test_timeseries_zoom'+str(ii)+'.png',190,'Another caption')

pdf.output(output_name, 'F')