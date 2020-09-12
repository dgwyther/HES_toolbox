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
# NaN the displacement data, as these sensors are currently disconnected (from Aug-13)
trimVariable=['D_NB_HJ3_1HU_Min','D_NB_HJ3_1HU_Max','D_NB_HJ3_1HU_Avg',
              'D_NB_HJ3_1HL_Min','D_NB_HJ3_1HL_Max','D_NB_HJ3_1HL_Avg',
              'D_NB_HJ3_2HU_Min','D_NB_HJ3_2HL_Min','D_NB_HJ3_3HU_Min',
              'D_NB_HJ3_3HL_Min','D_NB_HJ3_2HU_Max','D_NB_HJ3_2HL_Max',
              'D_NB_HJ3_3HU_Max','D_NB_HJ3_3HL_Max','D_NB_HJ3_2HU_Avg',
              'D_NB_HJ3_2HL_Avg','D_NB_HJ3_3HU_Avg','D_NB_HJ3_3HL_Avg']
trimStart=  ['2020-AUG-13 09:50']
trimEnd=    ['2020-OCT-01 00:00']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['T_NB_HJ3_C1H_Min','T_NB_HJ3_C1H_Max','T_NB_HJ3_C1H_Avg',
              'T_NB_HJ3_S1H_Min','T_NB_HJ3_S1H_Max','T_NB_HJ3_S1H_Avg',
              'T_NB_HJ3_C2B_Min','T_NB_HJ3_C2B_Max','T_NB_HJ3_C2B_Avg']
trimStart=  ['2020-AUG-6 13:50']
trimEnd=    ['2020-AUG-6 14:20']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

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

# trimVariable=['S_NB_HJ3_S1H_Min','S_NB_HJ3_S1H_Avg','S_NB_HJ3_S1H_Max']
# trimStart=  ['2020-AUG-06 14:00']
# trimEnd=    ['2020-AUG-06 14:10']
# removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

# trimVariable=['S_NB_HJ3_S2D_Min','S_NB_HJ3_S2D_Avg','S_NB_HJ3_S2D_Max']
# trimStart=  ['2020-AUG-07 01:15']
# trimEnd=    ['2020-AUG-07 01:25']
# removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

# trimVariable=['S_NB_HJ3_S1V_Min','S_NB_HJ3_S1V_Avg','S_NB_HJ3_S1V_Max']
# trimStart=  ['2020-AUG-06 14:00']
# trimEnd=    ['2020-AUG-06 14:10']
# removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

# trimVariable=['S_NB_HJ3_S3H_Min','S_NB_HJ3_S3H_Avg','S_NB_HJ3_S3H_Max']
# trimStart=  ['2020-AUG-06 14:15']
# trimEnd=    ['2020-AUG-06 14:25']
# removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)



trimVariable=['S_NB_HJ3_C3H_Min','S_NB_HJ3_C3H_Avg','S_NB_HJ3_C3H_Max']
trimStart=  ['2020-AUG-9 23:00',
             '2020-AUG-11 04:30',
             '2020-AUG-14 01:30',
             '2020-AUG-14 07:30',
             '2020-AUG-16 19:30',
             '2020-AUG-17 20:10',
             '2020-AUG-17 22:00',
             '2020-AUG-19 01:50',
             '2020-AUG-20 22:30',
             '2020-AUG-21 00:20',
             '2020-AUG-21 08:20',
             '2020-AUG-22 00:00',
             '2020-AUG-22 00:35']

trimEnd=    ['2020-AUG-10 01:00',
             '2020-AUG-11 05:30',
             '2020-AUG-14 02:10',
             '2020-AUG-14 08:00',
             '2020-AUG-16 20:00',
             '2020-AUG-17 20:30',
             '2020-AUG-17 22:50',
             '2020-AUG-19 02:00',
             '2020-AUG-20 23:40',
             '2020-AUG-21 04:00',
             '2020-AUG-21 08:50',
             '2020-AUG-22 00:20',
             '2020-AUG-22 00:45']

removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['S_NB_HJ3_C2D_Min','S_NB_HJ3_C2D_Avg','S_NB_HJ3_C2D_Max']
trimStart=  ['2020-AUG-21 01:10']
trimEnd=    ['2020-AUG-21 04:00']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_C2B_Min','S_NB_HJ3_C2B_Avg','S_NB_HJ3_C2B_Max']
trimStart=  ['2020-AUG-21 01:10']
trimEnd=    ['2020-AUG-21 04:00']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
# the following trims are when some vwire sensors were shifted.
trimVariable=['S_NB_HJ3_S2D_Min','S_NB_HJ3_S2D_Avg','S_NB_HJ3_S2D_Max']
trimStart=  ['2020-AUG-7 01:15']
trimEnd=    ['2020-AUG-7 01:30']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_C2D_Min','S_NB_HJ3_C2D_Avg','S_NB_HJ3_C2D_Max']
trimStart=  ['2020-AUG-7 01:10']
trimEnd=    ['2020-AUG-7 01:30']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_S3H_Min','S_NB_HJ3_S3H_Avg','S_NB_HJ3_S3H_Max']
trimStart=  ['2020-AUG-6 14:10']
trimEnd=    ['2020-AUG-6 14:35']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_C3H_Min','S_NB_HJ3_C3H_Avg','S_NB_HJ3_C3H_Max']
trimStart=  ['2020-AUG-6 14:10']
trimEnd=    ['2020-AUG-6 14:35']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_S1H_Min','S_NB_HJ3_S1H_Avg','S_NB_HJ3_S1H_Max']
trimStart=  ['2020-AUG-6 13:50']
trimEnd=    ['2020-AUG-6 14:20']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_S2B_Min','S_NB_HJ3_S2B_Avg','S_NB_HJ3_S2B_Max']
trimStart=  ['2020-AUG-6 14:00']
trimEnd=    ['2020-AUG-6 14:25']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_S1V_Min','S_NB_HJ3_S1V_Avg','S_NB_HJ3_S1V_Max']
trimStart=  ['2020-AUG-6 14:00']
trimEnd=    ['2020-AUG-6 14:10']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['T_NB_HJ3_S2B_Min','T_NB_HJ3_S2B_Max','T_NB_HJ3_S2B_Avg']
trimStart=  ['2020-AUG-24 03:15',
             '2020-AUG-24 08:30',
             '2020-AUG-24 16:05',
             '2020-AUG-25 01:05',
             '2020-AUG-27 09:15']
trimEnd=    ['2020-AUG-24 06:45',
             '2020-AUG-24 14:55',
             '2020-AUG-24 21:45',
             '2020-AUG-25 01:35',
             '2020-AUG-27 09:30']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['S_NB_HJ3_S2B_Min','S_NB_HJ3_S2B_Max','S_NB_HJ3_S2B_Avg']
trimStart=  ['2020-AUG-24 03:15',
             '2020-AUG-24 08:30',
             '2020-AUG-24 16:05',
             '2020-AUG-25 01:05',
             '2020-AUG-27 09:15']
trimEnd=    ['2020-AUG-24 06:45',
             '2020-AUG-24 14:55',
             '2020-AUG-24 21:45',
             '2020-AUG-25 01:35',
             '2020-AUG-27 09:30']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['S_NB_HJ3_C2D_Min','S_NB_HJ3_C2D_Max','S_NB_HJ3_C2D_Avg']
trimStart=  ['2020-AUG-23 19:30',
             '2020-AUG-23 22:05',
             '2020-AUG-24 20:15',
             '2020-AUG-25 02:30',
             '2020-AUG-25 03:20',
             '2020-AUG-25 09:35',
             '2020-AUG-25 11:10',
             '2020-AUG-25 15:00',
             '2020-AUG-26 08:10',
             '2020-AUG-26 10:00',
             '2020-AUG-27 01:50']
trimEnd=    ['2020-AUG-23 21:10',
             '2020-AUG-23 22:20',
             '2020-AUG-24 21:20',
             '2020-AUG-25 03:05',
             '2020-AUG-25 03:30',
             '2020-AUG-25 11:00',
             '2020-AUG-25 11:50',
             '2020-AUG-25 15:15',
             '2020-AUG-26 09:20',
             '2020-AUG-26 12:10',
             '2020-AUG-27 02:10']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['S_NB_HJ3_C3H_Min','S_NB_HJ3_C3H_Max','S_NB_HJ3_C3H_Avg']
trimStart=  ['2020-AUG-23 22:35',
             '2020-AUG-24 00:20',
             '2020-AUG-24 20:30',
             '2020-AUG-25 01:20']
trimEnd=    ['2020-AUG-23 22:45',
             '2020-AUG-24 00:30',
             '2020-AUG-24 21:25',
             '2020-AUG-25 01:30']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
# remove data that is corrupted post 'blackout'/servicing on ~Sep-03.
trimVariable=['L_NB_HJ3_B1(S15_KGA2)_Min','L_NB_HJ3_B1(S15_KGA2)_Max','L_NB_HJ3_B1(S15_KGA2)_Avg',
              'L_NB_HJ3_B2(S14_KGE1)_Min','L_NB_HJ3_B2(S14_KGE1)_Max','L_NB_HJ3_B2(S14_KGE1)_Avg',
              'L_NB_HJ3_B3(S13_KGA1)_Min','L_NB_HJ3_B3(S13_KGA1)_Max','L_NB_HJ3_B3(S13_KGA1)_Avg',
              'L_NB_HJ3_B123_Min','L_NB_HJ3_B123_Max','L_NB_HJ3_B123_Avg',
              'DF_NB_HJ3_B1(S15_KGA2)_Min','DF_NB_HJ3_B1(S15_KGA2)_Max','DF_NB_HJ3_B1(S15_KGA2)_Avg',
              'DF_NB_HJ3_B2(S14_KGE1)_Min','DF_NB_HJ3_B2(S14_KGE1)_Max','DF_NB_HJ3_B2(S14_KGE1)_Avg',
              'DF_NB_HJ3_B3(S13_KGA1)_Min','DF_NB_HJ3_B3(S13_KGA1)_Max','DF_NB_HJ3_B3(S13_KGA1)_Avg']
trimStart=  ['2020-SEP-03 20:00',
             '2020-SEP-04 11:55',
             '2020-SEP-04 16:40',
             '2020-SEP-06 11:15',
             '2020-SEP-08 20:30']
trimEnd=    ['2020-SEP-03 20:15',
             '2020-SEP-04 14:05',
             '2020-SEP-04 18:50',
             '2020-SEP-06 18:20',
             '2020-SEP-09 01:10']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['T_NB_HJ3_ToBS_Min','T_NB_HJ3_ToBS_Max','T_NB_HJ3_ToBS_Avg']
trimStart=  ['2020-SEP-03 12:45']
trimEnd=    ['2020-SEP-03 12:55']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['T_NB_HJ3_ToBS_Min','T_NB_HJ3_ToBS_Max','T_NB_HJ3_ToBS_Avg',
              'T_NB_HJ3_ToTS_Min','T_NB_HJ3_ToTS_Max','T_NB_HJ3_ToTS_Avg',
              'T_NB_HJ3_BoTS_Min','T_NB_HJ3_BoTS_Max','T_NB_HJ3_BoTS_Avg',
              'T_NB_HJ3_Asphalt_Min','T_NB_HJ3_Asphalt_Max','T_NB_HJ3_Asphalt_Avg']
trimStart=  ['2020-SEP-03 12:45',
             '2020-SEP-04 01:50',
             '2020-SEP-05 03:05',
             '2020-SEP-06 05:10',
             '2020-SEP-06 21:05',
             '2020-SEP-08 01:10',
             '2020-SEP-09 00:10']
trimEnd=    ['2020-SEP-03 12:55',
             '2020-SEP-04 10:50',
             '2020-SEP-05 10:50',
             '2020-SEP-06 09:55',
             '2020-SEP-07 10:55',
             '2020-SEP-09 11:50',
             '2020-SEP-09 11:55']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_C2B_Min','S_NB_HJ3_C2B_Max','S_NB_HJ3_C2B_Avg']
trimStart=  ['2020-SEP-07 14:40']
trimEnd=    ['2020-SEP-07 14:55']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

# Add NaN in any time gaps
if 'SS_filename' in locals():
    df_SS=addNANGaps(df_SS,"TIMESTAMP",'5Min')

# Re-align/join any datasets which have had shifts mid-data
variablesToRealign=['S_NB_HJ3_S2D_Avg','S_NB_HJ3_S2D_Min','S_NB_HJ3_S2D_Max',
                    'S_NB_HJ3_C2D_Avg','S_NB_HJ3_C2D_Min','S_NB_HJ3_C2D_Max',
                    'S_NB_HJ3_S3H_Avg','S_NB_HJ3_S3H_Min','S_NB_HJ3_S3H_Max',
                    'S_NB_HJ3_C3H_Avg','S_NB_HJ3_C3H_Min','S_NB_HJ3_C3H_Max']
shiftTimes=['2020-AUG-07 01:30','2020-AUG-07 01:30','2020-AUG-07 01:30',
            '2020-AUG-07 01:30','2020-AUG-07 01:30','2020-AUG-07 01:30',
            '2020-AUG-06 14:35','2020-AUG-06 14:35','2020-AUG-06 14:35',
            '2020-AUG-06 14:35','2020-AUG-06 14:35','2020-AUG-06 14:35']
shiftValues=[64.4, 64.4, 64.4,
             17.3, 17.3, 17.3,
             -50.8,-50.8,-50.8,
             -28.5,-28.5,-28.5 ]
joinOffsetData(df_SS,"TIMESTAMP",variablesToRealign,shiftTimes,shiftValues)

variablesToRealign=['S_NB_HJ3_S1H_Avg','S_NB_HJ3_S1H_Min','S_NB_HJ3_S1H_Max',
                    'S_NB_HJ3_S2B_Avg','S_NB_HJ3_S2B_Min','S_NB_HJ3_S2B_Max',
                    'S_NB_HJ3_S1V_Avg','S_NB_HJ3_S1V_Min','S_NB_HJ3_S1V_Max']
shiftTimes=['2020-AUG-06 14:20','2020-AUG-06 14:20','2020-AUG-06 14:20',
            '2020-AUG-06 14:25','2020-AUG-06 14:25','2020-AUG-06 14:25',
            '2020-AUG-06 14:10','2020-AUG-06 14:10','2020-AUG-06 14:10']
shiftValues=[-6.0,-6.0,-6.0,
             33.1,33.1,33.1,
             42.5,42.5,42.5]
joinOffsetData(df_SS,"TIMESTAMP",variablesToRealign,shiftTimes,shiftValues)

variablesToRealign=['S_NB_HJ3_C3H_Avg','S_NB_HJ3_C3H_Min','S_NB_HJ3_C3H_Max',]
shiftTimes=['2020-AUG-25 15:20','2020-AUG-25 15:20','2020-AUG-25 15:20']
shiftValues=[167,167,167]
joinOffsetData(df_SS,"TIMESTAMP",variablesToRealign,shiftTimes,shiftValues)
#testing of B1 on 10th and 11th Sep.
trimVariable=['L_NB_HJ3_B1(S15_KGA2)_Min','L_NB_HJ3_B1(S15_KGA2)_Max','L_NB_HJ3_B1(S15_KGA2)_Avg',
              'L_NB_HJ3_B123_Min','L_NB_HJ3_B123_Max','L_NB_HJ3_B123_Avg',
              'DF_NB_HJ3_B1(S15_KGA2)_Min','DF_NB_HJ3_B1(S15_KGA2)_Max','DF_NB_HJ3_B1(S15_KGA2)_Avg',
              'DF_NB_HJ3_B2(S14_KGE1)_Min','DF_NB_HJ3_B2(S14_KGE1)_Max','DF_NB_HJ3_B2(S14_KGE1)_Avg',
              'DF_NB_HJ3_B3(S13_KGA1)_Min','DF_NB_HJ3_B3(S13_KGA1)_Max','DF_NB_HJ3_B3(S13_KGA1)_Avg']
trimStart=  ['2020-SEP-10 14:10',
             '2020-SEP-11 08:15']
trimEnd=    ['2020-SEP-10 14:40',
             '2020-SEP-11 09:40']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['L_NB_HJ3_B1(S15_KGA2)_Min','L_NB_HJ3_B1(S15_KGA2)_Max','L_NB_HJ3_B1(S15_KGA2)_Avg',
              'L_NB_HJ3_B2(S14_KGE1)_Min','L_NB_HJ3_B2(S14_KGE1)_Max','L_NB_HJ3_B2(S14_KGE1)_Avg',
              'L_NB_HJ3_B3(S13_KGA1)_Min','L_NB_HJ3_B3(S13_KGA1)_Max','L_NB_HJ3_B3(S13_KGA1)_Avg',
              'L_NB_HJ3_B123_Min','L_NB_HJ3_B123_Max','L_NB_HJ3_B123_Avg',
              'DF_NB_HJ3_B1(S15_KGA2)_Min','DF_NB_HJ3_B1(S15_KGA2)_Max','DF_NB_HJ3_B1(S15_KGA2)_Avg',
              'DF_NB_HJ3_B2(S14_KGE1)_Min','DF_NB_HJ3_B2(S14_KGE1)_Max','DF_NB_HJ3_B2(S14_KGE1)_Avg',
              'DF_NB_HJ3_B3(S13_KGA1)_Min','DF_NB_HJ3_B3(S13_KGA1)_Max','DF_NB_HJ3_B3(S13_KGA1)_Avg']
trimStart=  ['2020-SEP-10 17:15',
             '2020-SEP-11 09:50']
trimEnd=    ['2020-SEP-10 21:50',
             '2020-SEP-11 12:00']
removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
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

#for ii in range(1,NoTimeSeriesWithBeards+1):

ii=1 # Bearing Loads
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
                            **keyword_parameters1)
ii=2 # Distribution factor
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
                            **keyword_parameters2)

ii=3 # Temperatures in Group 1
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
                            **keyword_parameters3)

ii=4 # Temperatures in group 2
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
                            **keyword_parameters4)

ii=5 # Temperatures in concrete and asphalt
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
                            **keyword_parameters5)


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

#for ii in range(1,NoTimeSeriesDisplacedMinMaxAvg+1):
ii=1
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
                                        **keyword_parametersDisp1
                                        )
ii=2
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
                                        **keyword_parametersDisp2
                                        )

ii=3
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
                                        **keyword_parametersDisp3
                                        )



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
print('laying out report')
exec(open(templateFile).read())
print('making PDF')
pdf.output(output_name, 'F')
toc = time.time()
print('done at '+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+', elapsed time '+str(round(toc-tic,1))+'s')
