## TRIMMING DATA
# NaN the displacement data, as these sensors are currently disconnected (from Aug-13)
trimVariable=['D_NB_HJ3_1HU_Min','D_NB_HJ3_1HU_Max','D_NB_HJ3_1HU_Avg',
              'D_NB_HJ3_1HL_Min','D_NB_HJ3_1HL_Max','D_NB_HJ3_1HL_Avg',
              'D_NB_HJ3_2HU_Min','D_NB_HJ3_2HL_Min','D_NB_HJ3_3HU_Min',
              'D_NB_HJ3_3HL_Min','D_NB_HJ3_2HU_Max','D_NB_HJ3_2HL_Max',
              'D_NB_HJ3_3HU_Max','D_NB_HJ3_3HL_Max','D_NB_HJ3_2HU_Avg',
              'D_NB_HJ3_2HL_Avg','D_NB_HJ3_3HU_Avg','D_NB_HJ3_3HL_Avg']
trimStart=  ['2020-AUG-13 09:50']
trimEnd=    ['2020-OCT-01 00:00']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['T_NB_HJ3_C1H_Min','T_NB_HJ3_C1H_Max','T_NB_HJ3_C1H_Avg',
              'T_NB_HJ3_S1H_Min','T_NB_HJ3_S1H_Max','T_NB_HJ3_S1H_Avg',
              'T_NB_HJ3_C2B_Min','T_NB_HJ3_C2B_Max','T_NB_HJ3_C2B_Avg']
trimStart=  ['2020-AUG-6 13:50']
trimEnd=    ['2020-AUG-6 14:20']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

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
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

# trimVariable=['S_NB_HJ3_S1H_Min','S_NB_HJ3_S1H_Avg','S_NB_HJ3_S1H_Max']
# trimStart=  ['2020-AUG-06 14:00']
# trimEnd=    ['2020-AUG-06 14:10']
# df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

# trimVariable=['S_NB_HJ3_S2D_Min','S_NB_HJ3_S2D_Avg','S_NB_HJ3_S2D_Max']
# trimStart=  ['2020-AUG-07 01:15']
# trimEnd=    ['2020-AUG-07 01:25']
# df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

# trimVariable=['S_NB_HJ3_S1V_Min','S_NB_HJ3_S1V_Avg','S_NB_HJ3_S1V_Max']
# trimStart=  ['2020-AUG-06 14:00']
# trimEnd=    ['2020-AUG-06 14:10']
# df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

# trimVariable=['S_NB_HJ3_S3H_Min','S_NB_HJ3_S3H_Avg','S_NB_HJ3_S3H_Max']
# trimStart=  ['2020-AUG-06 14:15']
# trimEnd=    ['2020-AUG-06 14:25']
# df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)



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

df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['S_NB_HJ3_C2D_Min','S_NB_HJ3_C2D_Avg','S_NB_HJ3_C2D_Max']
trimStart=  ['2020-AUG-21 01:10']
trimEnd=    ['2020-AUG-21 04:00']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_C2B_Min','S_NB_HJ3_C2B_Avg','S_NB_HJ3_C2B_Max']
trimStart=  ['2020-AUG-21 01:10']
trimEnd=    ['2020-AUG-21 04:00']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
# the following trims are when some vwire sensors were shifted.
trimVariable=['S_NB_HJ3_S2D_Min','S_NB_HJ3_S2D_Avg','S_NB_HJ3_S2D_Max']
trimStart=  ['2020-AUG-7 01:15']
trimEnd=    ['2020-AUG-7 01:30']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_C2D_Min','S_NB_HJ3_C2D_Avg','S_NB_HJ3_C2D_Max']
trimStart=  ['2020-AUG-7 01:10']
trimEnd=    ['2020-AUG-7 01:30']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_S3H_Min','S_NB_HJ3_S3H_Avg','S_NB_HJ3_S3H_Max']
trimStart=  ['2020-AUG-6 14:10']
trimEnd=    ['2020-AUG-6 14:35']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_C3H_Min','S_NB_HJ3_C3H_Avg','S_NB_HJ3_C3H_Max']
trimStart=  ['2020-AUG-6 14:10']
trimEnd=    ['2020-AUG-6 14:35']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_S1H_Min','S_NB_HJ3_S1H_Avg','S_NB_HJ3_S1H_Max']
trimStart=  ['2020-AUG-6 13:50']
trimEnd=    ['2020-AUG-6 14:20']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_S2B_Min','S_NB_HJ3_S2B_Avg','S_NB_HJ3_S2B_Max']
trimStart=  ['2020-AUG-6 14:00']
trimEnd=    ['2020-AUG-6 14:25']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_S1V_Min','S_NB_HJ3_S1V_Avg','S_NB_HJ3_S1V_Max']
trimStart=  ['2020-AUG-6 14:00']
trimEnd=    ['2020-AUG-6 14:10']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

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
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

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
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

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
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

trimVariable=['S_NB_HJ3_C3H_Min','S_NB_HJ3_C3H_Max','S_NB_HJ3_C3H_Avg']
trimStart=  ['2020-AUG-23 22:35',
             '2020-AUG-24 00:20',
             '2020-AUG-24 20:30',
             '2020-AUG-25 01:20']
trimEnd=    ['2020-AUG-23 22:45',
             '2020-AUG-24 00:30',
             '2020-AUG-24 21:25',
             '2020-AUG-25 01:30']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
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
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['T_NB_HJ3_ToBS_Min','T_NB_HJ3_ToBS_Max','T_NB_HJ3_ToBS_Avg']
trimStart=  ['2020-SEP-03 12:45']
trimEnd=    ['2020-SEP-03 12:55']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
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
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
trimVariable=['S_NB_HJ3_C2B_Min','S_NB_HJ3_C2B_Max','S_NB_HJ3_C2B_Avg']
trimStart=  ['2020-SEP-07 14:40']
trimEnd=    ['2020-SEP-07 14:55']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

## RE-ALIGNING DATA
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
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
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
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
