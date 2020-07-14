import numpy as np
import pandas as pd
import datetime



def generateTableOverview(pdfObject,inputDataEvents,TimeIndex,table_title,row_titles,sensorStatisticsFields,sensorStatisticsNames):
    start_date = pd.to_datetime(inputDataEvents[TimeIndex].max())-datetime.timedelta(days=7)
    end_date = pd.to_datetime(inputDataEvents[TimeIndex].max())
    mask = (inputDataEvents[TimeIndex] > start_date) & (inputDataEvents[TimeIndex] <= end_date)
    inputDataEvents_stats_LastWeekFull = inputDataEvents.loc[mask]
    # SRES_stats_overview = {
                    # 'Date start': [inputDataEvents[TimeIndex].min().strftime("%d-%m-%y %H:%M"),inputDataEvents_stats_LastWeekFull[TimeIndex].min().strftime("%d-%m-%y %H:%M")],
                    # 'Date end': [inputDataEvents[TimeIndex].max().strftime("%d-%m-%y %H:%M"),inputDataEvents_stats_LastWeekFull[TimeIndex].max().strftime("%d-%m-%y %H:%M")],
                    # '# of Rel Events': [inputDataEvents.shape[0],inputDataEvents_stats_LastWeekFull.shape[0]],
                    # 'Events/day': [round(inputDataEvents.shape[0]/pd.to_numeric(datetime.timedelta.total_seconds(inputDataEvents[TimeIndex].max()-inputDataEvents[TimeIndex].min()) / (3600*24)),1),round(inputDataEvents_stats_LastWeekFull.shape[0]/pd.to_numeric(datetime.timedelta.total_seconds(inputDataEvents_stats_LastWeekFull[TimeIndex].max()-inputDataEvents_stats_LastWeekFull[TimeIndex].min()) / (3600*24)),1)],
                    # 'Sensor(1) Max': [round(inputDataEvents['SensorRelEventMax(1)'].max(),1),round(inputDataEvents_stats_LastWeekFull['SensorRelEventMax(1)'].max(),1)],
                    # 'Sensor(2) Max': [round(inputDataEvents['SensorRelEventMax(2)'].max(),1),round(inputDataEvents_stats_LastWeekFull['SensorRelEventMax(2)'].max(),1)],
                    # 'Sensor(3) Max': [round(inputDataEvents['SensorRelEventMax(3)'].max(),1),round(inputDataEvents_stats_LastWeekFull['SensorRelEventMax(3)'].max(),1)],
                    # 'Sensor(4) Max': [round(inputDataEvents['SensorRelEventMax(4)'].max(),1),round(inputDataEvents_stats_LastWeekFull['SensorRelEventMax(4)'].max(),1)],
                    # 'Sensor(5) Max': [round(inputDataEvents['SensorRelEventMax(5)'].max(),1),round(inputDataEvents_stats_LastWeekFull['SensorRelEventMax(5)'].max(),1)]
                    # }
#   add non-changing elements
    SRES_stats_overview = {
                    'Date start': [inputDataEvents[TimeIndex].min().strftime("%d-%m-%y %H:%M"),inputDataEvents_stats_LastWeekFull[TimeIndex].min().strftime("%d-%m-%y %H:%M")],
                    'Date end': [inputDataEvents[TimeIndex].max().strftime("%d-%m-%y %H:%M"),inputDataEvents_stats_LastWeekFull[TimeIndex].max().strftime("%d-%m-%y %H:%M")],
                    '# of Rel Events': [inputDataEvents.shape[0],inputDataEvents_stats_LastWeekFull.shape[0]],
                    'Events/day': [round(inputDataEvents.shape[0]/pd.to_numeric(datetime.timedelta.total_seconds(inputDataEvents["TIMESTAMP"].max()-inputDataEvents["TIMESTAMP"].min()) / (3600*24)),1),round(inputDataEvents_stats_LastWeekFull.shape[0]/pd.to_numeric(datetime.timedelta.total_seconds(inputDataEvents_stats_LastWeekFull["TIMESTAMP"].max()-inputDataEvents_stats_LastWeekFull["TIMESTAMP"].min()) / (3600*24)),1)]
                    }
#   add changing elements
    for i in range(0,len(sensorStatisticsNames)):
        SRES_stats_overview[sensorStatisticsNames[i]]=[round(inputDataEvents[sensorStatisticsFields[i]].max(),1),round(inputDataEvents_stats_LastWeekFull[sensorStatisticsFields[i]].max(),1)]
#   convert dict to dataframe
    inputDataEvents_stats_overview = pd.DataFrame(SRES_stats_overview).T
    inputDataEvents_stats_overview.columns={'0':'','1':''}
    inputDataEvents_stats_overview.rename(columns={'0':'All time','1':'Last Two Weeks'}, inplace = True)
    set_table_dims = np.shape(inputDataEvents_stats_overview)
#   now convert to PDF object
    pdfObject.set_font('arial', 'B', 12)
    pdfObject.cell(60)
    pdfObject.cell(75, 10, table_title, 0, 2, 'C')
    pdfObject.cell(90, 10, " ", 0, 2, 'C')
    pdfObject.cell(-40)
    pdfObject.set_font('arial', 'BU', 12)
    # make titles of table
    for idx, word in enumerate(row_titles):
        if idx==0:
            pdfObject.cell(50, 10, str(word), 0, 0, 'C')
        elif idx!=len(row_titles)-1:
            pdfObject.cell(40, 10, str(word), 0, 0, 'C')
        elif idx==len(row_titles)-1:
            pdfObject.cell(40, 10, str(word), 0, 2, 'C')

    pdfObject.cell(-90)
    pdfObject.set_font('arial', '', 12)
    # fill data in
    for i in range(0, len(inputDataEvents_stats_overview)):
        pdfObject.cell(50, 10, '%s' % (inputDataEvents_stats_overview.index[i]), 0, 0, 'C')
        pdfObject.cell(40, 10, '%s' % (inputDataEvents_stats_overview.iloc[i,0]), 0, 0, 'C')
        pdfObject.cell(40, 10, '%s' % (inputDataEvents_stats_overview.iloc[i,1]), 0, 2, 'C')
        pdfObject.cell(-90)

    pdfObject.cell(90, 10, " ", 0, 2, 'C')
    pdfObject.cell(-30)
