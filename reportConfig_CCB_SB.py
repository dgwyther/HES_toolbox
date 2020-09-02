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
title = 'Captain Cook Bridge: Halving Joint 3 Monitoring Project'
#author = 'Report issued: '+f"{datetime.datetime.now():%d-%b-%Y}"
author = 'Southbound'
logo_path = 'assets/logo.png'
output_name = 'test.sb.pdf'

# file locations
SS_filename = '../SampleData/TMR701_RV50_CCB_SB_SensorStats.dat'

## Alias table definition
# Either select 'none': no aliasing
# or 'csv': to load from a path given in aliasTablePath
# or 'dict': to load from a dictionary entered below.
loadAlias='none'
aliasTablePath='../SampleData/tmp.TMR701_RV50_CCB_NB_aliasTable.csv'

## LOAD FROM SPREADSHEET
# 1. Summary table title, sensor fields and names
table_title1 = 'title' # title for the table

section1_notes = 'This report present data gathered at the CCB southbound halving joint 3 monitoring station.'

# 2. Time series plot - include field names for each plot
NoTimeSeriesPlots = 0
#
NoTimeSeriesWithBeards=5
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
caption_Beards1=''
timeseries_plots_min2=[ 'DF_SB_HJ3_B1_Min',
                        'DF_SB_HJ3_B2_Min',
                        'DF_SB_HJ3_B3_Min']
timeseries_plots_max2=[ 'DF_SB_HJ3_B1_Max',
                        'DF_SB_HJ3_B2_Max',
                        'DF_SB_HJ3_B3_Max']
timeseries_plots_avg2=[ 'DF_SB_HJ3_B1_Avg',
                        'DF_SB_HJ3_B2_Avg',
                        'DF_SB_HJ3_B3_Avg']
title_Beards2='Distribution factor (Minimum, Average & Maximum)'
yAx_Beards2='Distribution factor'
caption_Beards2=''
timeseries_plots_min3=['T_SB_HJ3_C2B_Min',
                       'T_SB_HJ3_S2B_Min',
                       'T_SB_HJ3_S1H_Min',
                       'T_SB_HJ3_S1D_Min',
                       'T_SB_HJ3_S1V_Min',
                       'T_SB_HJ3_C1H_Min',
                       'T_SB_HJ3_C1D_Min',
                       'T_SB_HJ3_C1V_Min']
timeseries_plots_max3=['T_SB_HJ3_C2B_Max',
                       'T_SB_HJ3_S2B_Max',
                       'T_SB_HJ3_S1H_Max',
                       'T_SB_HJ3_S1D_Max',
                       'T_SB_HJ3_S1V_Max',
                       'T_SB_HJ3_C1H_Max',
                       'T_SB_HJ3_C1D_Max',
                       'T_SB_HJ3_C1V_Max']
timeseries_plots_avg3=['T_SB_HJ3_C2B_Avg',
                       'T_SB_HJ3_S2B_Avg',
                       'T_SB_HJ3_S1H_Avg',
                       'T_SB_HJ3_S1D_Avg',
                       'T_SB_HJ3_S1V_Avg',
                       'T_SB_HJ3_C1H_Avg',
                       'T_SB_HJ3_C1D_Avg',
                       'T_SB_HJ3_C1V_Avg']
title_Beards3='Temperature (Vibrating Wire Sensor Group 1)'
yAx_Beards3='Temperature (C)'
annotation3=['sudden drop in ambient temperature']
annotatePointXY3={  'time':['26-07-2020 15:40'],
                    'height':[15]}
annotateTextXY3={   'time':['26-07-2020 15:40'],
                    'height':[10]}
#annotatePointXY3=['26-07-2020 15:40',15]
#annotateTextXY3=['26-07-2020 15:40', 10]

caption_Beards3=''
timeseries_plots_min4=['T_SB_HJ3_C2D_Min',
                       'T_SB_HJ3_S2D_Min',
                       'T_SB_HJ3_S3H_Min',
                       'T_SB_HJ3_S3D_Min',
                       'T_SB_HJ3_S3V_Min',
                       'T_SB_HJ3_C3H_Min',
                       'T_SB_HJ3_C3D_Min',
                       'T_SB_HJ3_C3V_Min']
timeseries_plots_max4=['T_SB_HJ3_C2D_Max',
                       'T_SB_HJ3_S2D_Max',
                       'T_SB_HJ3_S3H_Max',
                       'T_SB_HJ3_S3D_Max',
                       'T_SB_HJ3_S3V_Max',
                       'T_SB_HJ3_C3H_Max',
                       'T_SB_HJ3_C3D_Max',
                       'T_SB_HJ3_C3V_Max']
timeseries_plots_avg4=['T_SB_HJ3_C2D_Avg',
                       'T_SB_HJ3_S2D_Avg',
                       'T_SB_HJ3_S3H_Avg',
                       'T_SB_HJ3_S3D_Avg',
                       'T_SB_HJ3_S3V_Avg',
                       'T_SB_HJ3_C3H_Avg',
                       'T_SB_HJ3_C3D_Avg',
                       'T_SB_HJ3_C3V_Avg']
title_Beards4='Temperatures (Vibrating Wire Sensor Group 2)'
yAx_Beards4='Temperature (C)'
caption_Beards4=''
timeseries_plots_min5=[ 'T_SB_HJ3_Asphalt_Min',
                        'T_SB_HJ3_ToTS_Min',
                        'T_SB_HJ3_BoTS_Min',
                        'T_SB_HJ3_ToBS_Min',]
timeseries_plots_max5=[ 'T_SB_HJ3_Asphalt_Max',
                        'T_SB_HJ3_ToTS_Max',
                        'T_SB_HJ3_BoTS_Max',
                        'T_SB_HJ3_ToBS_Max',]
timeseries_plots_avg5=[ 'T_SB_HJ3_Asphalt_Avg',
                        'T_SB_HJ3_ToTS_Avg',
                        'T_SB_HJ3_BoTS_Avg',
                        'T_SB_HJ3_ToBS_Avg',]
title_Beards5='Temperature - Concrete & Asphalt'
yAx_Beards5='Temperature (C)'
caption_Beards5=''

#############################################################
NoTimeSeriesSubplots=0
timeseries_plots_subplot1=[ 'Therm1_Avg(1)',
                            'Therm1_Avg(2)',
                            'Therm1_Avg(3)']
nRows=1
nCols=3
yAx_subplot1='Temperature (C)'

#############################################################
NoTimeSeriesDisplaced=0
timeseries_plots_displaced1=['D_SB_HJ3_1HU_Avg',
                             'D_SB_HJ3_1HL_Avg',
                             'D_SB_HJ3_2HU_Avg',
                             'D_SB_HJ3_2HL_Avg',
                             'D_SB_HJ3_3HU_Avg',
                             'D_SB_HJ3_3HL_Avg']
dispFactor1=20
dispRef1='initial'
title_disp1='Displacement (with offset of '+str(dispFactor1)+'mm )'
yAx_disp1='Displacement (mm)'
timeseries_plots_displaced2=[   'S_SB_HJ3_C2B_Avg',
                                'S_SB_HJ3_S2B_Avg',
                                'S_SB_HJ3_S1H_Avg',
                                'S_SB_HJ3_S1D_Avg',
                                'S_SB_HJ3_S1V_Avg',
                                'S_SB_HJ3_C1H_Avg',
                                'S_SB_HJ3_C1D_Avg',
                                'S_SB_HJ3_C1V_Avg']
dispFactor2=20
dispRef2='initial'
title_disp2='Strain (Vibrating Wire Sensor Group 1 - Min, Avg, Max, '+str(dispFactor2)+'ue offset, temperature corrected)'
yAx_disp2=r'Microstrain ($\mu \epsilon$)'
timeseries_plots_displaced3=['S_SB_HJ3_C2D_Avg',
                             'S_SB_HJ3_S2D_Avg',
                             'S_SB_HJ3_S3H_Avg',
                             'S_SB_HJ3_S3D_Avg',
                             'S_SB_HJ3_S3V_Avg',
                             'S_SB_HJ3_C3H_Avg',
                             'S_SB_HJ3_C3D_Avg',
                             'S_SB_HJ3_C3V_Avg']
dispFactor3=20
dispRef3='initial'
title_disp3='Strain (Vibrating Wire Sensor Group 2 - Min, Avg, Max, '+str(dispFactor3)+'ue offset, temperature corrected)'
yAx_disp3=r'Microstrain ($\mu \epsilon$)'

#############################################################
NoTimeSeriesDisplacedMinMaxAvg=3
timeseries_plots_displaced_min1=[   'D_SB_HJ3_1HU_Min',
                                    'D_SB_HJ3_1HL_Min',
                                    'D_SB_HJ3_2HU_Min',
                                    'D_SB_HJ3_2HL_Min',
                                    'D_SB_HJ3_3HU_Min',
                                    'D_SB_HJ3_3HL_Min']
timeseries_plots_displaced_max1=[   'D_SB_HJ3_1HU_Max',
                                    'D_SB_HJ3_1HL_Max',
                                    'D_SB_HJ3_2HU_Max',
                                    'D_SB_HJ3_2HL_Max',
                                    'D_SB_HJ3_3HU_Max',
                                    'D_SB_HJ3_3HL_Max']
timeseries_plots_displaced_avg1=[   'D_SB_HJ3_1HU_Avg',
                                    'D_SB_HJ3_1HL_Avg',
                                    'D_SB_HJ3_2HU_Avg',
                                    'D_SB_HJ3_2HL_Avg',
                                    'D_SB_HJ3_3HU_Avg',
                                    'D_SB_HJ3_3HL_Avg']
dispFactorMMA1=25
dispRefMMA1='initial'
title_dispMMA1='Displacement (with offset of '+str(dispFactor1)+'mm )'
yAx_dispMMA1='Displacement (mm)'
timeseries_plots_displaced_min2=[   'S_SB_HJ3_C2B_Min',
                                    'S_SB_HJ3_S2B_Min',
                                    'S_SB_HJ3_S1H_Min',
                                    'S_SB_HJ3_S1D_Min',
                                    'S_SB_HJ3_S1V_Min',
                                    'S_SB_HJ3_C1H_Min',
                                    'S_SB_HJ3_C1D_Min',
                                    'S_SB_HJ3_C1V_Min']
timeseries_plots_displaced_max2=[   'S_SB_HJ3_C2B_Max',
                                    'S_SB_HJ3_S2B_Max',
                                    'S_SB_HJ3_S1H_Max',
                                    'S_SB_HJ3_S1D_Max',
                                    'S_SB_HJ3_S1V_Max',
                                    'S_SB_HJ3_C1H_Max',
                                    'S_SB_HJ3_C1D_Max',
                                    'S_SB_HJ3_C1V_Max']
timeseries_plots_displaced_avg2=[   'S_SB_HJ3_C2B_Avg',
                                    'S_SB_HJ3_S2B_Avg',
                                    'S_SB_HJ3_S1H_Avg',
                                    'S_SB_HJ3_S1D_Avg',
                                    'S_SB_HJ3_S1V_Avg',
                                    'S_SB_HJ3_C1H_Avg',
                                    'S_SB_HJ3_C1D_Avg',
                                    'S_SB_HJ3_C1V_Avg']
dispFactorMMA2=25
dispRefMMA2='initial'
title_dispMMA2='Strain (Vibrating Wire Sensor Group 1 - Min, Avg, Max, '+str(dispFactor2)+'ue offset, temperature corrected)'
yAx_dispMMA2=r'Microstrain ($\mu \epsilon$)'
timeseries_plots_displaced_min3=[   'S_SB_HJ3_C2D_Min',
                                    'S_SB_HJ3_S2D_Min',
                                    'S_SB_HJ3_S3H_Min',
                                    'S_SB_HJ3_S3D_Min',
                                    'S_SB_HJ3_S3V_Min',
                                    'S_SB_HJ3_C3H_Min',
                                    'S_SB_HJ3_C3D_Min',
                                    'S_SB_HJ3_C3V_Min']
timeseries_plots_displaced_max3=[   'S_SB_HJ3_C2D_Max',
                                    'S_SB_HJ3_S2D_Max',
                                    'S_SB_HJ3_S3H_Max',
                                    'S_SB_HJ3_S3D_Max',
                                    'S_SB_HJ3_S3V_Max',
                                    'S_SB_HJ3_C3H_Max',
                                    'S_SB_HJ3_C3D_Max',
                                    'S_SB_HJ3_C3V_Max']
timeseries_plots_displaced_avg3=[   'S_SB_HJ3_C2D_Avg',
                                    'S_SB_HJ3_S2D_Avg',
                                    'S_SB_HJ3_S3H_Avg',
                                    'S_SB_HJ3_S3D_Avg',
                                    'S_SB_HJ3_S3V_Avg',
                                    'S_SB_HJ3_C3H_Avg',
                                    'S_SB_HJ3_C3D_Avg',
                                    'S_SB_HJ3_C3V_Avg']
dispFactorMMA3=25
dispRefMMA3='initial'
title_dispMMA3='Strain (Vibrating Wire Sensor Group 2 - Min, Avg, Max, '+str(dispFactor3)+'ue offset, temperature corrected)'
yAx_dispMMA3=r'Microstrain ($\mu \epsilon$)'

#############################################################
# 3. Definitions and notes for x-y section
NoXYPlots = 0

#############################################################
# 4. Definitions and notes for inv normal plot section
NoInvNormPlots = 0

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
