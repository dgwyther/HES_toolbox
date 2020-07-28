### Template file
# This file provides the template for outputting a report with reportDriver.py
# Settings are defined here and this whole file is loaded as a module when the 
# driver file is run.
# If multiple plots are desired, keep the setting name the same, but increment
# by 1 (e.g. timeseries_plot1, timeseries_plot2)
###

# global defns
title = 'CCB Northbound draft report'
author = 'Author: DEG'
logo_path = 'assets/logo.png'
output_name = 'test.pdf'

# file locations
SS_filename = '../SampleData/HE604_RV50_CCB_NB_SensorStats.dat'
#SRES_filename = '../dash/GAF/Data/HE605_RV50_GAF_SensorRelEventStats.dat'

# Alias table definition
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
## LOAD FROM SPREADSHEET

# 1. Summary table title, sensor fields and names
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


section1_notes = 'You might want to include some introductory notes.'

# 2. Time series plot - include field names for each plot
NoTimeSeriesPlots = 0
timeseries_plot1 = ["SensorRel_Max(1)",
                    "SensorRel_Max(2)",
                    "SensorRel_Max(3)",
                    "SensorRel_Max(4)",
                    "SensorRel_Max(5)"]
#
NoTimeSeriesWithBeards=5
timeseries_plots_min1=[ 'L_NB_HJ3_B1_Min',
                        'L_NB_HJ3_B2_Min',
                        'L_NB_HJ3_B3_Min',
                        'L_NB_HJ3_B123_Min']
timeseries_plots_max1=[ 'L_NB_HJ3_B1_Max',
                        'L_NB_HJ3_B2_Max',
                        'L_NB_HJ3_B3_Max',
                        'L_NB_HJ3_B123_Max']
timeseries_plots_avg1=[ 'L_NB_HJ3_B1_Avg',
                        'L_NB_HJ3_B2_Avg',
                        'L_NB_HJ3_B3_Avg',
                        'L_NB_HJ3_B123_Avg']
title_Beards1='Loading Mass'
yAx_Beards1='Loading mass (t)'
caption_Beards1='first caption of beard plot'
timeseries_plots_min2=['DF_NB_HJ3_B1_Min',
                        'DF_NB_HJ3_B2_Min',
                        'DF_NB_HJ3_B3_Min']
timeseries_plots_max2=['DF_NB_HJ3_B1_Max',
                        'DF_NB_HJ3_B2_Max',
                        'DF_NB_HJ3_B3_Max']
timeseries_plots_avg2=['DF_NB_HJ3_B1_Avg',
                        'DF_NB_HJ3_B2_Avg',
                        'DF_NB_HJ3_B3_Avg']
title_Beards2='Distribution factor'
yAx_Beards2='D-factor (unitless)'
caption_Beards2='2nd caption of beard plot'
timeseries_plots_min3=['Therm1_Min(1)',
                       'Therm1_Min(2)',
                       'Therm1_Min(3)',
                       'Therm1_Min(4)',
                       'Therm1_Min(5)',
                       'Therm1_Min(6)',
                       'Therm1_Min(7)',
                       'Therm1_Min(8)']
timeseries_plots_max3=['Therm1_Max(1)',
                       'Therm1_Max(2)',
                       'Therm1_Max(3)',
                       'Therm1_Max(4)',
                       'Therm1_Max(5)',
                       'Therm1_Max(6)',
                       'Therm1_Max(7)',
                       'Therm1_Max(8)']                       
timeseries_plots_avg3=['Therm1_Avg(1)',
                       'Therm1_Avg(2)',
                       'Therm1_Avg(3)',
                       'Therm1_Avg(4)',
                       'Therm1_Avg(5)',
                       'Therm1_Avg(6)',
                       'Therm1_Avg(7)',
                       'Therm1_Avg(8)']                       
title_Beards3='Thermistor 1'
yAx_Beards3='Temperature (C)'
caption_Beards3='3rd caption of beard plot'
timeseries_plots_min4=['Therm2_Min(1)',
                       'Therm2_Min(2)',
                       'Therm2_Min(3)',
                       'Therm2_Min(4)',
                       'Therm2_Min(5)',
                       'Therm2_Min(6)',
                       'Therm2_Min(7)',
                       'Therm2_Min(8)']
timeseries_plots_max4=['Therm2_Max(1)',
                       'Therm2_Max(2)',
                       'Therm2_Max(3)',
                       'Therm2_Max(4)',
                       'Therm2_Max(5)',
                       'Therm2_Max(6)',
                       'Therm2_Max(7)',
                       'Therm2_Max(8)']                       
timeseries_plots_avg4=['Therm2_Avg(1)',
                       'Therm2_Avg(2)',
                       'Therm2_Avg(3)',
                       'Therm2_Avg(4)',
                       'Therm2_Avg(5)',
                       'Therm2_Avg(6)',
                       'Therm2_Avg(7)',
                       'Therm2_Avg(8)']                       
title_Beards4='Thermistor 2'
yAx_Beards4='Temperature (C)'
caption_Beards4='4th caption of beard plot'
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
title_Beards5='Thermistor 3'
yAx_Beards5='Temperature (C)'
caption_Beards5='5th caption of beard plot'
#
NoTimeSeriesSubplots=0
timeseries_plots_subplot1=['Therm1_Avg(1)',
                            'Therm1_Avg(2)',
                            'Therm1_Avg(3)']
nRows=1
nCols=3
yAx_subplot1='Temperature (C)'

NoTimeSeriesDisplaced=3
timeseries_plots_displaced1=['Disp_Avg(1)',
                            'Disp_Avg(2)',
                            'Disp_Avg(3)',
                            'Disp_Avg(4)',
                            'Disp_Avg(5)',
                            'Disp_Avg(6)']
dispFactor1=20
dispRef1='initial'
title_disp1='Displacement with offset of '+str(dispFactor1)
yAx_disp1='Displacement (mm)'
timeseries_plots_displaced2=['microS1T20_Avg(1)',
                            'microS1T20_Avg(2)',
                            'microS1T20_Avg(3)',
                            'microS1T20_Avg(4)',
                            'microS1T20_Avg(5)',
                            'microS1T20_Avg(6)',
                            'microS1T20_Avg(7)',
                            'microS1T20_Avg(8)']
dispFactor2=20
dispRef2='initial'
title_disp2='Microstrain at S1 at T=20C with offset of '+str(dispFactor2)
yAx_disp2=r'Microstrain ($\mu \epsilon$)'
timeseries_plots_displaced3=['microS2T20_Avg(1)',
                            'microS2T20_Avg(2)',
                            'microS2T20_Avg(3)',
                            'microS2T20_Avg(4)',
                            'microS2T20_Avg(5)',
                            'microS2T20_Avg(6)',
                            'microS2T20_Avg(7)',
                            'microS2T20_Avg(8)']
dispFactor3=20
dispRef3='initial'
title_disp3='Microstrain at S2 at T=20C with offset of '+str(dispFactor3)
yAx_disp3=r'Microstrain ($\mu \epsilon$)'

NoTimeSeriesDisplacedMinMaxAvg=3
timeseries_plots_displaced_min1=['Disp_Min(1)',
                            'Disp_Min(2)',
                            'Disp_Min(3)',
                            'Disp_Min(4)',
                            'Disp_Min(5)',
                            'Disp_Min(6)']
timeseries_plots_displaced_max1=['Disp_Max(1)',
                            'Disp_Max(2)',
                            'Disp_Max(3)',
                            'Disp_Max(4)',
                            'Disp_Max(5)',
                            'Disp_Max(6)']
timeseries_plots_displaced_avg1=['Disp_Avg(1)',
                            'Disp_Avg(2)',
                            'Disp_Avg(3)',
                            'Disp_Avg(4)',
                            'Disp_Avg(5)',
                            'Disp_Avg(6)']
dispFactorMMA1=20
dispRefMMA1='initial'
title_dispMMA1='Displacements'
yAx_dispMMA1='Displacement (mm)'
timeseries_plots_displaced_min2=['microS1T20_Min(1)',
                            'microS1T20_Min(2)',
                            'microS1T20_Min(3)',
                            'microS1T20_Min(4)',
                            'microS1T20_Min(5)',
                            'microS1T20_Min(6)',
                            'microS1T20_Min(7)',
                            'microS1T20_Min(8)']
timeseries_plots_displaced_max2=['microS1T20_Max(1)',
                            'microS1T20_Max(2)',
                            'microS1T20_Max(3)',
                            'microS1T20_Max(4)',
                            'microS1T20_Max(5)',
                            'microS1T20_Max(6)',
                            'microS1T20_Max(7)',
                            'microS1T20_Max(8)']
timeseries_plots_displaced_avg2=['microS1T20_Avg(1)',
                            'microS1T20_Avg(2)',
                            'microS1T20_Avg(3)',
                            'microS1T20_Avg(4)',
                            'microS1T20_Avg(5)',
                            'microS1T20_Avg(6)',
                            'microS1T20_Avg(7)',
                            'microS1T20_Avg(8)']
dispFactorMMA2=20
dispRefMMA2='initial'
title_dispMMA2='Microstrain S1 at T=20'
yAx_dispMMA2=r'Microstrain ($\mu \epsilon$)'
timeseries_plots_displaced_min3=['microS2T20_Min(1)',
                            'microS2T20_Min(2)',
                            'microS2T20_Min(3)',
                            'microS2T20_Min(4)',
                            'microS2T20_Min(5)',
                            'microS2T20_Min(6)',
                            'microS2T20_Min(7)',
                            'microS2T20_Min(8)']
timeseries_plots_displaced_max3=['microS2T20_Max(1)',
                            'microS2T20_Max(2)',
                            'microS2T20_Max(3)',
                            'microS2T20_Max(4)',
                            'microS2T20_Max(5)',
                            'microS2T20_Max(6)',
                            'microS2T20_Max(7)',
                            'microS2T20_Max(8)']
timeseries_plots_displaced_avg3=['microS2T20_Avg(1)',
                            'microS2T20_Avg(2)',
                            'microS2T20_Avg(3)',
                            'microS2T20_Avg(4)',
                            'microS2T20_Avg(5)',
                            'microS2T20_Avg(6)',
                            'microS2T20_Avg(7)',
                            'microS2T20_Avg(8)']
dispFactorMMA3=20
dispRefMMA3='initial'
title_dispMMA3='Microstrain S2 at T=20'
yAx_dispMMA3=r'Microstrain ($\mu \epsilon$)'
# 3. Definitions and notes for x-y section
NoXYPlots = 0
XY_plot1_title = 'R vs L HJ Crack'
XY_plot1 = ['S_P2_CH_R_HJCrack_Pkp',
            'S_P2_CH_L_HJCrack_Pkp']

XY_plot2_title = 'G1 vs G3 of Span 2'
XY_plot2 = ['S_S2_G1_Pkp',
            'S_S2_G3_Pkp']


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

