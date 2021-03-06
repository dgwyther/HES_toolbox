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


#global defns
title = 'Example title that is about the same length '
author = 'Example author and date'
logo_path = 'assets/logo.png'
output_name = 'test.pdf'

# data defns
SS_filename = '../dash/GAF/Data/HE605_RV50_GAF_SensorStats.dat'
colNamesSS = ["TIMESTAMP","RECORD","BattV_Min","BattV_Avg","PTemp_C_Avg","SensorRel_Min(1)","SensorRel_Min(2)","SensorRel_Min(3)","SensorRel_Min(4)","SensorRel_Min(5)","SensorRel_Max(1)","SensorRel_Max(2)","SensorRel_Max(3)","SensorRel_Max(4)","SensorRel_Max(5)"]
SRES_filename = '../dash/GAF/Data/HE605_RV50_GAF_SensorRelEventStats.dat'
colNamesSRES = ["TIMESTAMP","RECORD","SensorRelEventMin(1)","SensorRelEventMin(2)","SensorRelEventMin(3)","SensorRelEventMin(4)","SensorRelEventMin(5)","SensorRelEventMax(1)","SensorRelEventMax(2)","SensorRelEventMax(3)","SensorRelEventMax(4)","SensorRelEventMax(5)","SensorRelEventPkp(1)","SensorRelEventPkp(2)","SensorRelEventPkp(3)","SensorRelEventPkp(4)","SensorRelEventPkp(5)","SensorWfmTrigSensor","SensorOffset(1)","SensorOffset(2)","SensorOffset(3)","SensorOffset(4)","SensorOffset(5)"]

df_SS = loadData(SS_filename,"TIMESTAMP",colNamesSS)
df_SRES = loadData(SRES_filename,"TIMESTAMP",colNamesSRES)
# Trim data

# Alias data
aliasTable_SRES = {
    "TIMESTAMP":"TIMESTAMP",
    "RECORD":"record",
    "SensorRelEventMin(1)":"S_P2_CH_L_HJCrack_Min",
    "SensorRelEventMin(2)":"S_P2_CH_R_HJCrack_Min",
    "SensorRelEventMin(3)":"S_S2_G1_Min",
    "SensorRelEventMin(4)":"S_S2_G2_Min",
    "SensorRelEventMin(5)":"S_S2_G3_Min",
    "SensorRelEventMax(1)":"S_P2_CH_L_HJCrack_Max",
    "SensorRelEventMax(2)":"S_P2_CH_R_HJCrack_Max",
    "SensorRelEventMax(3)":"S_S2_G1_Max",
    "SensorRelEventMax(4)":"S_S2_G2_Max",
    "SensorRelEventMax(5)":"S_S2_G3_Max",
    "SensorRelEventPkp(1)":"S_P2_CH_L_HJCrack_Pkp",
    "SensorRelEventPkp(2)":"S_P2_CH_R_HJCrack_Pkp",
    "SensorRelEventPkp(3)":"S_S2_G1_Pkp",
    "SensorRelEventPkp(4)":"S_S2_G2_Pkp",
    "SensorRelEventPkp(5)":"S_S2_G3_Pkp",
    "SensorWfmTrigSensor":"Sensor Waveform Trigger",
    "SensorOffset(1)":"S_P2_CH_L_HJCrack_Offset",
    "SensorOffset(2)":"S_P2_CH_R_HJCrack_Offset",
    "SensorOffset(3)":"S_S2_G1_Offset",
    "SensorOffset(4)":"S_S2_G2_Offset",
    "SensorOffset(5)":"S_S2_G3_Offset"
}

applyAliasTable(df_SRES,aliasTable_SRES)

# 1. Definitions and notes for summary table section
table_title = '' # title for the table
col_titles = ['','all time','last week'] # column titles
sensorStatisticsFields=['S_P2_CH_L_HJCrack_Max',
                        'S_P2_CH_R_HJCrack_Max',
                        'S_S2_G1_Max',
                        'S_S2_G2_Max',
                        'S_S2_G3_Max'] # what fields to do you want stats for?
sensorStatisticsNames=['S_P2_CH_L_HJCrack Max',
                       'S_P2_CH_R_HJCrack Max',
                       'S_S2_G1 Max',
                       'S_S2_G2 Max',
                       'S_S2_G3 Max'] # name to give in table?


stats_notes = 'This bit can include any special notes that you want to make about the statistics in this report. e.g. Note erroneous data arising due to blah blah. This will be automatically added as a special note to the end of the statistics summary section.'

# 2. Definitions and notes for time series section
# which plots to make?
timeseries_plots = ["SensorRel_Max(1)",
                    "SensorRel_Max(2)",
                    "SensorRel_Max(3)",
                    "SensorRel_Max(4)",
                    "SensorRel_Max(5)"]
                    
# 3. Definitions and notes for x-y section
XY_plot1_title = 'R vs L HJ Crack'
XY_plot1 = ['S_P2_CH_R_HJCrack_Pkp',
            'S_P2_CH_L_HJCrack_Pkp']
XY_plot2_title = 'G1 vs G3 of Span 2'
XY_plot2 = ['S_S2_G1_Pkp',
            'S_S2_G3_Pkp']


# 4. Definitions and notes for inv normal plot section
InvNorm_toPlot = ["S_P2_CH_R_HJCrack_Pkp",
                    "S_P2_CH_L_HJCrack_Pkp",
                    "S_S2_G1_Pkp",
                    "S_S2_G2_Pkp",
                    "S_S2_G3_Pkp"]

InvNormBinStart=0
InvNormBinEnd=200
InvNormBinInc=2
InvNormMin = 1
InvNormMax = 2.75

title_InvNorm = 'title of inverse normal plot'

# 5. Definitions and notes for Largest Events table
table_title2 = '' # title for the table
col_titles2 = ['','all time','last week'] # column titles
sensorStatisticsFields2=['S_P2_CH_L_HJCrack_Pkp',
                        'S_P2_CH_R_HJCrack_Pkp',
                        'S_S2_G1_Pkp',
                        'S_S2_G2_Pkp',
                        'S_S2_G3_Pkp'] # what fields to do you want stats for?
sensorStatisticsNames2=['P2_L_HJCrack Pkp',
                        'P2_R_HJCrack Pkp',
                        'S2_G1 Pkp',
                        'S2_G2 Pkp',
                        'S2_G3 Pkp'] # name to give in table?

stats_notes2 = 'This bit can include any special notes that you want to make about the statistics in this report. e.g. Note erroneous data arising due to blah blah. This will be automatically added as a special note to the end of the statistics summary section.'



## GENERATE PLOTS

generateTimeSeriesPlot(df_SS,"TIMESTAMP",timeseries_plots,'a temporary title','test_fig1.png','save')

generateTimeSeriesPlotZoomed(df_SS,"TIMESTAMP",timeseries_plots,'a temporary title','test_fig2.png','save')

generateXYPlot(df_SRES,XY_plot1,'linear',XY_plot1_title,'testXY1.png','save')

generateXYPlot(df_SRES,XY_plot2,'linear',XY_plot2_title,'testXY2.png','save')

generateInvNormPlot(df_SRES,"TIMESTAMP",InvNorm_toPlot,InvNormBinStart,InvNormBinInc,InvNormBinEnd,InvNormMin,InvNormMax,title_InvNorm,'testInvNorm.png','save')

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
pdf.print_timeSeriesPlot('test_fig1.png',190,'A caption')
pdf.print_timeSeriesPlotZoomed('test_fig2.png',190,'Another caption')
#
pdf.print_sectionHeader(3, 'X-Y data')
pdf.print_addPlot('testXY1.png',120,'Another caption')
pdf.print_addPlot('testXY2.png',120,'Another caption again')
#
pdf.print_sectionHeader(4, 'Inverse normal plots')
pdf.print_addPlot('testInvNorm.png',190,'Inverse Normal: Another caption again again')
#
pdf.print_sectionHeader(5, 'Largest events')
pdf.generateTableLargestEvents(df_SRES,10,6,11,"TIMESTAMP",table_title2,col_titles2,sensorStatisticsFields2,sensorStatisticsNames2)
pdf.print_text(stats_notes2)

pdf.output(output_name, 'F')