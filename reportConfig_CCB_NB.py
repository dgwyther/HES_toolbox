import datetime
today = datetime.date.today()
### Template file
# This file provides the template for outputting a report with reportDriver.py
# Settings are defined here and this whole file is loaded as a module when the
# driver file is run.
# If multiple plots are desired, keep the setting name the same, but increment
# by 1 (e.g. timeseries_plot1, timeseries_plot2)
###

# global defns
title = 'Captain Cook Bridge (Northbound): Halving Joint 3 Monitoring Project'
#author = 'Report issued: '+f"{datetime.datetime.now():%d-%b-%Y}"
author = ''
logo_path = 'assets/logo.png'
output_name = str(f"{datetime.datetime.now():%Y_%m_%d}"+'.nb.draft.pdf')

# file locations
SS_filename = '../SampleData/HE604_RV50_CCB_NB_SensorStats.dat'

## Alias table definition
# Either select 'none': no aliasing
# or 'csv': to load from a path given in aliasTablePath
# or 'dict': to load from a dictionary entered below.
loadAlias='csv'
aliasTablePath='../SampleData/HE604_RV50_CCB_NB_aliasTable.csv'
# loadAlias='dict'
# aliasTable_SRES = {
    # "TIMESTAMP":"TIMESTAMP",
    # "RECORD":"record",
    # "SensorRelEventMin(1)":"S_P2_CH_L_HJCrack_Min",
    # "SensorRelEventMin(2)":"S_P2_CH_R_HJCrack_Min",
    # "SensorRelEventMin(3)":"S_S2_G1_Min",
    # "SensorRelEventMin(4)":"S_S2_G2_Min",
    # "SensorRelEventMin(5)":"S_S2_G3_Min",
    # "SensorRelEventMax(1)":"S_P2_CH_L_HJCrack_Max",
    # "SensorRelEventMax(2)":"S_P2_CH_R_HJCrack_Max",
    # "SensorRelEventMax(3)":"S_S2_G1_Max",
    # "SensorRelEventMax(4)":"S_S2_G2_Max",
    # "SensorRelEventMax(5)":"S_S2_G3_Max",
    # "SensorRelEventPkp(1)":"S_P2_CH_L_HJCrack_Pkp",
    # "SensorRelEventPkp(2)":"S_P2_CH_R_HJCrack_Pkp",
    # "SensorRelEventPkp(3)":"S_S2_G1_Pkp",
    # "SensorRelEventPkp(4)":"S_S2_G2_Pkp",
    # "SensorRelEventPkp(5)":"S_S2_G3_Pkp",
    # "SensorWfmTrigSensor":"Sensor Waveform Trigger",
    # "SensorOffset(1)":"S_P2_CH_L_HJCrack_Offset",
    # "SensorOffset(2)":"S_P2_CH_R_HJCrack_Offset",
    # "SensorOffset(3)":"S_S2_G1_Offset",
    # "SensorOffset(4)":"S_S2_G2_Offset",
    # "SensorOffset(5)":"S_S2_G3_Offset"
# }

## LOAD FROM SPREADSHEET
# 1. Summary table title, sensor fields and names
table_title1 = 'title' # title for the table

section1_notes = 'This report present data gathered at the CCB northbound halving joint 3 monitoring station.'

#############################################################
# 2. Time series plot - include field names for each plot
NoTimeSeriesPlots = 0
timeseries_plot1 = ["A116_BattV_Avg","BattV_Avg"]
keyword_parameters_ts1={'addHighlight':'None',
                     'yAxisName':'Voltage (V)',
                     'xAxisName':'time',
                     'yAxisLims':'None',
                     'xAxisLims':'None', #['2020-8-27 09:00','2020-8-27 12:30']
                     'annotate': 'None',
                     'annotatePointXY': {'time':['26-07-2020 15:40'],'height':[15]},
                     'annotateTextXY': {'time':['26-07-2020 15:40'],'height':[10]},
                     'xTickFormat':['%d-%m','weekly'],
                     'plot_or_save':'plot'
                    }
#
NoTimeSeriesWithBeards=5
timeseries_plots_min1=[ 'L_NB_HJ3_B1(S15_KGA2)_Min',
                        'L_NB_HJ3_B2(S14_KGE1)_Min',
                        'L_NB_HJ3_B3(S13_KGA1)_Min',
                        'L_NB_HJ3_B123_Min']
timeseries_plots_max1=[ 'L_NB_HJ3_B1(S15_KGA2)_Max',
                        'L_NB_HJ3_B2(S14_KGE1)_Max',
                        'L_NB_HJ3_B3(S13_KGA1)_Max',
                        'L_NB_HJ3_B123_Max']
timeseries_plots_avg1=[ 'L_NB_HJ3_B1(S15_KGA2)_Avg',
                        'L_NB_HJ3_B2(S14_KGE1)_Avg',
                        'L_NB_HJ3_B3(S13_KGA1)_Avg',
                        'L_NB_HJ3_B123_Avg']
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
timeseries_plots_min2=['DF_NB_HJ3_B1(S15_KGA2)_Min',
                        'DF_NB_HJ3_B2(S14_KGE1)_Min',
                        'DF_NB_HJ3_B3(S13_KGA1)_Min']
timeseries_plots_max2=['DF_NB_HJ3_B1(S15_KGA2)_Max',
                        'DF_NB_HJ3_B2(S14_KGE1)_Max',
                        'DF_NB_HJ3_B3(S13_KGA1)_Max']
timeseries_plots_avg2=['DF_NB_HJ3_B1(S15_KGA2)_Avg',
                        'DF_NB_HJ3_B2(S14_KGE1)_Avg',
                        'DF_NB_HJ3_B3(S13_KGA1)_Avg']
title_Beards2='Distribution factor (Minimum, Average & Maximum)'
yAx_Beards2='Distribution factor'
keyword_parameters2={'yAxisLims':'None',
                     'xAxisLims':'None', #['2020-8-27 09:00','2020-8-27 12:30']
                     'annotate': 'None',
                     'annotatePointXY': {'time':['26-07-2020 15:40'],'height':[15]},
                     'annotateTextXY': {'time':['26-07-2020 15:40'],'height':[10]},
                     'xTickFormat':['%d-%m','weekly'],
                     'plot_or_save':'save'
                    }
caption_Beards2=''
timeseries_plots_min3=['T_NB_HJ3_C2B_Min',
                       'T_NB_HJ3_S2B_Min',
                       'T_NB_HJ3_S1H_Min',
                       'T_NB_HJ3_S1D_Min',
                       'T_NB_HJ3_S1V_Min',
                       'T_NB_HJ3_C1H_Min',
                       'T_NB_HJ3_C1D_Min',
                       'T_NB_HJ3_C1V_Min']
timeseries_plots_max3=['T_NB_HJ3_C2B_Max',
                       'T_NB_HJ3_S2B_Max',
                       'T_NB_HJ3_S1H_Max',
                       'T_NB_HJ3_S1D_Max',
                       'T_NB_HJ3_S1V_Max',
                       'T_NB_HJ3_C1H_Max',
                       'T_NB_HJ3_C1D_Max',
                       'T_NB_HJ3_C1V_Max']
timeseries_plots_avg3=['T_NB_HJ3_C2B_Avg',
                       'T_NB_HJ3_S2B_Avg',
                       'T_NB_HJ3_S1H_Avg',
                       'T_NB_HJ3_S1D_Avg',
                       'T_NB_HJ3_S1V_Avg',
                       'T_NB_HJ3_C1H_Avg',
                       'T_NB_HJ3_C1D_Avg',
                       'T_NB_HJ3_C1V_Avg']
title_Beards3='Temperature (Vibrating Wire Sensor Group 1)'
yAx_Beards3='Temperature (C)'
keyword_parameters3={'yAxisLims':[5,30],
                     'xAxisLims':'None', #['2020-8-27 09:00','2020-8-27 12:30']
                     'annotate': ['sudden drop in ambient temperature'],
                     'annotatePointXY': {'time':['26-07-2020 15:40'],'height':[15]},
                     'annotateTextXY': {'time':['26-07-2020 15:40'],'height':[10]},
                     'xTickFormat':['%d-%m','weekly'],
                     'plot_or_save':'save'
                    }
caption_Beards3=''
timeseries_plots_min4=['T_NB_HJ3_C2D_Min',
                       'T_NB_HJ3_S2D_Min',
                       'T_NB_HJ3_S3H_Min',
                       'T_NB_HJ3_S3D_Min',
                       'T_NB_HJ3_S3V_Min',
                       'T_NB_HJ3_C3H_Min',
                       'T_NB_HJ3_C3D_Min',
                       'T_NB_HJ3_C3V_Min']
timeseries_plots_max4=['T_NB_HJ3_C2D_Max',
                       'T_NB_HJ3_S2D_Max',
                       'T_NB_HJ3_S3H_Max',
                       'T_NB_HJ3_S3D_Max',
                       'T_NB_HJ3_S3V_Max',
                       'T_NB_HJ3_C3H_Max',
                       'T_NB_HJ3_C3D_Max',
                       'T_NB_HJ3_C3V_Max']
timeseries_plots_avg4=['T_NB_HJ3_C2D_Avg',
                       'T_NB_HJ3_S2D_Avg',
                       'T_NB_HJ3_S3H_Avg',
                       'T_NB_HJ3_S3D_Avg',
                       'T_NB_HJ3_S3V_Avg',
                       'T_NB_HJ3_C3H_Avg',
                       'T_NB_HJ3_C3D_Avg',
                       'T_NB_HJ3_C3V_Avg']
title_Beards4='Temperatures (Vibrating Wire Sensor Group 2)'
yAx_Beards4='Temperature (C)'
keyword_parameters4={'yAxisLims':[5,30],
                     'xAxisLims': 'None',
                     'xTickFormat':['%d-%m','weekly'],
                     'plot_or_save':'save'
                     }
caption_Beards4=''
timeseries_plots_min5=['T_NB_HJ3_Asphalt_Min',
                        'T_NB_HJ3_ToTS_Min',
                        'T_NB_HJ3_BoTS_Min',
                        'T_NB_HJ3_ToBS_Min',]
timeseries_plots_max5=['T_NB_HJ3_Asphalt_Max',
                        'T_NB_HJ3_ToTS_Max',
                        'T_NB_HJ3_BoTS_Max',
                        'T_NB_HJ3_ToBS_Max',]
timeseries_plots_avg5=['T_NB_HJ3_Asphalt_Avg',
                        'T_NB_HJ3_ToTS_Avg',
                        'T_NB_HJ3_BoTS_Avg',
                        'T_NB_HJ3_ToBS_Avg',]
title_Beards5='Temperature - Concrete & Asphalt'
yAx_Beards5='Temperature (C)'
keyword_parameters5={'yAxisLims': [12.5,35],
                     'xAxisLims': 'None',
                     'xTickFormat':['%d-%m','weekly'],
                     'plot_or_save':'save'
                     }
caption_Beards5=''

#############################################################
NoTimeSeriesSubplots=0
timeseries_plots_subplot1=['Therm1_Avg(1)',
                            'Therm1_Avg(2)',
                            'Therm1_Avg(3)']
nRows=1
nCols=3
yAx_subplot1='Temperature (C)'

#############################################################
NoTimeSeriesDisplaced=0
timeseries_plots_displaced1=['D_NB_HJ3_1HU_Avg',
                            'D_NB_HJ3_1HL_Avg',
                            'D_NB_HJ3_2HU_Avg',
                            'D_NB_HJ3_2HL_Avg',
                            'D_NB_HJ3_3HU_Avg',
                            'D_NB_HJ3_3HL_Avg']
dispFactor1=20
dispRef1='initial'
title_disp1='Displacement (with offset of '+str(dispFactor1)+'mm )'
yAx_disp1='Displacement (mm)'
timeseries_plots_displaced2=[   'S_NB_HJ3_C2B_Avg',
                                'S_NB_HJ3_S2B_Avg',
                                'S_NB_HJ3_S1H_Avg',
                                'S_NB_HJ3_S1D_Avg',
                                'S_NB_HJ3_S1V_Avg',
                                'S_NB_HJ3_C1H_Avg',
                                'S_NB_HJ3_C1D_Avg',
                                'S_NB_HJ3_C1V_Avg']
dispFactor2=20
dispRef2='initial'
title_disp2='Strain (Vibrating Wire Sensor Group 1 - Min, Avg, Max, '+str(dispFactor2)+'ue offset, temperature corrected)'
yAx_disp2=r'Microstrain ($\mu \epsilon$)'
timeseries_plots_displaced3=['S_NB_HJ3_C2D_Avg',
                            'S_NB_HJ3_S2D_Avg',
                            'S_NB_HJ3_S3H_Avg',
                            'S_NB_HJ3_S3D_Avg',
                            'S_NB_HJ3_S3V_Avg',
                            'S_NB_HJ3_C3H_Avg',
                            'S_NB_HJ3_C3D_Avg',
                            'S_NB_HJ3_C3V_Avg']
dispFactor3=20
dispRef3='initial'
title_disp3='Strain (Vibrating Wire Sensor Group 2 - Min, Avg, Max, '+str(dispFactor3)+'ue offset, temperature corrected)'
yAx_disp3=r'Microstrain ($\mu \epsilon$)'

#############################################################
NoTimeSeriesDisplacedMinMaxAvg=3
timeseries_plots_displaced_min1=[   'D_NB_HJ3_1HU_Min',
                                    'D_NB_HJ3_1HL_Min',
                                    'D_NB_HJ3_2HU_Min',
                                    'D_NB_HJ3_2HL_Min',
                                    'D_NB_HJ3_3HU_Min',
                                    'D_NB_HJ3_3HL_Min']
timeseries_plots_displaced_max1=[   'D_NB_HJ3_1HU_Max',
                                    'D_NB_HJ3_1HL_Max',
                                    'D_NB_HJ3_2HU_Max',
                                    'D_NB_HJ3_2HL_Max',
                                    'D_NB_HJ3_3HU_Max',
                                    'D_NB_HJ3_3HL_Max']
timeseries_plots_displaced_avg1=[   'D_NB_HJ3_1HU_Avg',
                                    'D_NB_HJ3_1HL_Avg',
                                    'D_NB_HJ3_2HU_Avg',
                                    'D_NB_HJ3_2HL_Avg',
                                    'D_NB_HJ3_3HU_Avg',
                                    'D_NB_HJ3_3HL_Avg']
dispFactorMMA1=25
dispRefMMA1='initial'
title_dispMMA1='Displacement (with offset of '+str(dispFactorMMA1)+'mm )'
yAx_dispMMA1='Displacement (mm)'
keyword_parametersDisp1={'yAxisLims':'None',
                         'xAxisLims':'None',
                         'xTickFormat':['%d-%m','weekly'],
                         'plot_or_save':'save'
                         }
#
timeseries_plots_displaced_min2=[   'S_NB_HJ3_C2B_Min',
                                    'S_NB_HJ3_S2B_Min',
                                    'S_NB_HJ3_S1H_Min',
                                    'S_NB_HJ3_S1D_Min',
                                    'S_NB_HJ3_S1V_Min',
                                    'S_NB_HJ3_C1H_Min',
                                    'S_NB_HJ3_C1D_Min',
                                    'S_NB_HJ3_C1V_Min']
timeseries_plots_displaced_max2=[   'S_NB_HJ3_C2B_Max',
                                    'S_NB_HJ3_S2B_Max',
                                    'S_NB_HJ3_S1H_Max',
                                    'S_NB_HJ3_S1D_Max',
                                    'S_NB_HJ3_S1V_Max',
                                    'S_NB_HJ3_C1H_Max',
                                    'S_NB_HJ3_C1D_Max',
                                    'S_NB_HJ3_C1V_Max']
timeseries_plots_displaced_avg2=[   'S_NB_HJ3_C2B_Avg',
                                    'S_NB_HJ3_S2B_Avg',
                                    'S_NB_HJ3_S1H_Avg',
                                    'S_NB_HJ3_S1D_Avg',
                                    'S_NB_HJ3_S1V_Avg',
                                    'S_NB_HJ3_C1H_Avg',
                                    'S_NB_HJ3_C1D_Avg',
                                    'S_NB_HJ3_C1V_Avg']
dispFactorMMA2=25
dispRefMMA2='initial'
title_dispMMA2='Strain (Vibrating Wire Sensor Group 1 - Min, Avg, Max, '+str(dispFactorMMA2)+'ue offset, temperature corrected)'
yAx_dispMMA2=r'Microstrain ($\mu \epsilon$)'
keyword_parametersDisp2={'yAxisLims':[-50,350],
                         'xAxisLims':'None', #['2020-8-27 09:00','2020-8-27 12:30']
                         'xTickFormat':['%d-%m','weekly'],
                         'plot_or_save':'save'
                         }
#
timeseries_plots_displaced_min3=[   'S_NB_HJ3_C2D_Min',
                                    'S_NB_HJ3_S2D_Min',
                                    'S_NB_HJ3_S3H_Min',
                                    'S_NB_HJ3_S3D_Min',
                                    'S_NB_HJ3_S3V_Min',
                                    'S_NB_HJ3_C3H_Min',
                                    'S_NB_HJ3_C3D_Min',
                                    'S_NB_HJ3_C3V_Min']
timeseries_plots_displaced_max3=[   'S_NB_HJ3_C2D_Max',
                                    'S_NB_HJ3_S2D_Max',
                                    'S_NB_HJ3_S3H_Max',
                                    'S_NB_HJ3_S3D_Max',
                                    'S_NB_HJ3_S3V_Max',
                                    'S_NB_HJ3_C3H_Max',
                                    'S_NB_HJ3_C3D_Max',
                                    'S_NB_HJ3_C3V_Max']
timeseries_plots_displaced_avg3=[   'S_NB_HJ3_C2D_Avg',
                                    'S_NB_HJ3_S2D_Avg',
                                    'S_NB_HJ3_S3H_Avg',
                                    'S_NB_HJ3_S3D_Avg',
                                    'S_NB_HJ3_S3V_Avg',
                                    'S_NB_HJ3_C3H_Avg',
                                    'S_NB_HJ3_C3D_Avg',
                                    'S_NB_HJ3_C3V_Avg']
dispFactorMMA3=25
dispRefMMA3='initial'
title_dispMMA3='Strain (Vibrating Wire Sensor Group 2 - Min, Avg, Max, '+str(dispFactorMMA3)+'ue offset, temperature corrected)'
yAx_dispMMA3=r'Microstrain ($\mu \epsilon$)'
keyword_parametersDisp3={'yAxisLims':[-50,400],
                         'xAxisLims':'None', #['2020-8-27 09:00','2020-8-27 12:30']
                         'xTickFormat':['%d-%m','weekly'],
                         'plot_or_save':'save'
                         }
#############################################################
# 3. Definitions and notes for x-y section
NoXYPlots = 0
XY_plot1_title = 'R vs L HJ Crack'
XY_plot1 = ['S_P2_CH_R_HJCrack_Pkp',
            'S_P2_CH_L_HJCrack_Pkp']

XY_plot2_title = 'G1 vs G3 of Span 2'
XY_plot2 = ['S_S2_G1_Pkp',
            'S_S2_G3_Pkp']

#############################################################
# 4. Definitions and notes for inv normal plot section
NoInvNormPlots = 0
title_InvNorm = 'title of inverse normal plot'
InvNorm_toPlot1 = ["S_P2_CH_R_HJCrack_Pkp",
                    "S_P2_CH_L_HJCrack_Pkp",
                    "S_S2_G1_Pkp",
                    "S_S2_G2_Pkp",
                    "S_S2_G3_Pkp"]
InvNormBinStart=0
InvNormBinEnd=200
InvNormBinInc=2
InvNormMin = 1
InvNormMax = 2.75

#############################################################
# 5. Title, column names, fields and field names for the 'largest event' table
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
