## TRIMMING DATA
# remove first alignments of strain group 1
trimVariable=['S_SB_HJ3_C2D_Min','S_SB_HJ3_C2D_Max','S_SB_HJ3_C2D_Avg',
              'S_SB_HJ3_S2D_Min','S_SB_HJ3_S2D_Max','S_SB_HJ3_S2D_Avg',
              'S_SB_HJ3_C3H_Min','S_SB_HJ3_C3H_Max','S_SB_HJ3_C3H_Avg',
              'S_SB_HJ3_C3D_Min','S_SB_HJ3_C3D_Max','S_SB_HJ3_C3D_Avg',
              'S_SB_HJ3_C3V_Min','S_SB_HJ3_C3V_Max','S_SB_HJ3_C3V_Avg',
              'S_SB_HJ3_S3H_Min','S_SB_HJ3_S3H_Max','S_SB_HJ3_S3H_Avg',
              'S_SB_HJ3_S3D_Min','S_SB_HJ3_S3D_Max','S_SB_HJ3_S3D_Avg',
              'S_SB_HJ3_S3V_Min','S_SB_HJ3_S3V_Max','S_SB_HJ3_S3V_Avg']
trimStart=  ['2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40']
trimEnd=    ['2020-AUG-25 11:50',
             '2020-AUG-25 11:50',
             '2020-AUG-25 11:50',
             '2020-AUG-25 11:50',
             '2020-AUG-25 11:50',
             '2020-AUG-25 11:50',
             '2020-AUG-25 11:50',
             '2020-AUG-25 11:50']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
# remove first alignments of strain group 2
trimVariable=['S_SB_HJ3_C1H_Min','S_SB_HJ3_C1H_Max','S_SB_HJ3_C1H_Avg',
              'S_SB_HJ3_C1D_Min','S_SB_HJ3_C1D_Max','S_SB_HJ3_C1D_Avg',
              'S_SB_HJ3_C1V_Min','S_SB_HJ3_C1V_Max','S_SB_HJ3_C1V_Avg',
              'S_SB_HJ3_C2B_Min','S_SB_HJ3_C2B_Max','S_SB_HJ3_C2B_Avg',
              'S_SB_HJ3_S2B_Min','S_SB_HJ3_S2B_Max','S_SB_HJ3_S2B_Avg',
              'S_SB_HJ3_S1H_Min','S_SB_HJ3_S1H_Max','S_SB_HJ3_S1H_Avg',
              'S_SB_HJ3_S1D_Min','S_SB_HJ3_S1D_Max','S_SB_HJ3_S1D_Avg',
              'S_SB_HJ3_S1V_Min','S_SB_HJ3_S1V_Max','S_SB_HJ3_S1V_Avg']
trimStart=  ['2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40',
             '2020-AUG-25 11:40']
trimEnd=    ['2020-AUG-25 15:50',
             '2020-AUG-25 15:50',
             '2020-AUG-25 15:50',
             '2020-AUG-25 15:50',
             '2020-AUG-25 15:50',
             '2020-AUG-25 15:50',
             '2020-AUG-25 15:50',
             '2020-AUG-25 15:50']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)
# remove dropouts in load data on sep 15th
trimVariable=['L_SB_HJ3_B123_Min','L_SB_HJ3_B123_Max','L_SB_HJ3_B123_Avg',
              'L_SB_HJ3_B2_Min','L_SB_HJ3_B2_Max','L_SB_HJ3_B2_Avg',
              'L_SB_HJ3_B3_Min','L_SB_HJ3_B3_Max','L_SB_HJ3_B3_Avg',
              'DF_SB_HJ3_B1_Min','DF_SB_HJ3_B1_Max','DF_SB_HJ3_B1_Avg',
              'DF_SB_HJ3_B2_Min','DF_SB_HJ3_B2_Max','DF_SB_HJ3_B2_Avg',
              'DF_SB_HJ3_B3_Min','DF_SB_HJ3_B3_Max','DF_SB_HJ3_B3_Avg']
trimStart=  ['2020-SEP-15 16:00']
trimEnd=    ['2020-SEP-15 16:15']
df_SS = removeVariableBetweenDates(df_SS,"TIMESTAMP",trimVariable,trimStart,trimEnd)

## RE-ALIGNING DATA

# Re-align/join any datasets which have had shifts mid-data
# variablesToRealign=['S_SB_HJ3_C2B_Avg','S_SB_HJ3_C2B_Min','S_SB_HJ3_C2B_Max',
#                     'S_SB_HJ3_S2B_Avg','S_SB_HJ3_S2B_Min','S_SB_HJ3_S2B_Max',
#                     'S_SB_HJ3_S3H_Avg','S_SB_HJ3_S3H_Min','S_SB_HJ3_S3H_Max',
#                     'S_SB_HJ3_C3H_Avg','S_SB_HJ3_C3H_Min','S_SB_HJ3_C3H_Max']
# shiftTimes=['2020-AUG-07 11:50','2020-AUG-07 11:50','2020-AUG-07 11:50',
#             '2020-AUG-07 01:30','2020-AUG-07 01:30','2020-AUG-07 01:30',
#             '2020-AUG-06 14:35','2020-AUG-06 14:35','2020-AUG-06 14:35',
#             '2020-AUG-06 14:35','2020-AUG-06 14:35','2020-AUG-06 14:35']
# shiftValues=[48.38, 48.38, 48.38,
#              17.3, 17.3, 17.3,
#              -50.8,-50.8,-50.8,
#              -28.5,-28.5,-28.5 ]
# joinOffsetData(df_SS,"TIMESTAMP",variablesToRealign,shiftTimes,shiftValues)
