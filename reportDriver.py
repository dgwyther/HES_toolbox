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
from functions.fun_generateXYPlot import generateXYPlot
from functions.fun_generateInvNormPlot import generateInvNormPlot

#import template file
from reportTemplate import *

# Load data
df_SS = loadData(SS_filename,"TIMESTAMP",colNamesSS)
df_SRES = loadData(SRES_filename,"TIMESTAMP",colNamesSRES)

# Trim data

# Alias data
applyAliasTable(df_SRES,aliasTable_SRES)



## GENERATE PLOTS

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
pdf.print_sectionHeader(1, 'Summary statistics')
pdf.generateTableOverview(df_SRES,"TIMESTAMP",table_title,col_titles,sensorStatisticsFields,sensorStatisticsNames)
pdf.print_text(stats_notes)
#
pdf.print_sectionHeader(2, 'Timeseries data')
for ii in range(1,NoTimeSeriesPlots+1):
    pdf.print_timeSeriesPlot('test_timeseries'+str(ii)+'.png',190,'A caption')
    pdf.print_timeSeriesPlotZoomed('test_timeseries_zoom'+str(ii)+'.png',190,'Another caption')

pdf.print_sectionHeader(3, 'X-Y data')
for ii in range(1,NoXYPlots+1):
    pdf.print_addPlot('test_XY'+str(ii)+'.png',120,'Another caption')

pdf.print_sectionHeader(4, 'Inverse normal plots')
for ii in range(1,NoInvNormPlots+1):
    pdf.print_addPlot('test_InvNorm'+str(ii)+'.png',190,'Inverse Normal: Another caption again again')
#
pdf.print_sectionHeader(5, 'Largest events')
pdf.generateTableLargestEvents(df_SRES,10,6,11,"TIMESTAMP",table_title2,col_titles2,sensorStatisticsFields2,sensorStatisticsNames2)
pdf.print_text(stats_notes2)

pdf.output(output_name, 'F')