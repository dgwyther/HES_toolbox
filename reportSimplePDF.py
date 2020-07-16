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


# 1. Definitions and notes for summary table section
table_title = '' # title for the table
col_titles = ['','all time','last week'] # column titles
sensorStatisticsFields=['SensorRelEventMax(1)',
                        'SensorRelEventMax(2)',
                        'SensorRelEventMax(3)',
                        'SensorRelEventMax(4)',
                        'SensorRelEventMax(5)'] # what fields to do you want stats for?
sensorStatisticsNames=['Sensor(1) Max',
                       'Sensor(2) Max',
                       'Sensor(3) Max',
                       'Sensor(4) Max',
                       'Sensor(5) Max'] # name to give in table?


stats_notes = 'This bit can include any special notes that you want to make about the statistics in this report. e.g. Note erroneous data arising due to blah blah. This will be automatically added as a special note to the end of the statistics summary section.'

# 2. Definitions and notes for time series section
# which plots to make?
timeseries_plots = ["SensorRel_Max(1)",
                    "SensorRel_Max(2)",
                    "SensorRel_Max(3)",
                    "SensorRel_Max(4)",
                    "SensorRel_Max(5)"]
                    
# 3. Definitions and notes for x-y section
XY_plot1_title = '1 vs 2'
XY_plot1 = ['SensorRelEventPkp(1)',
            'SensorRelEventPkp(2)']
XY_plot2_title = '3 vs 4'
XY_plot2 = ['SensorRelEventPkp(3)',
            'SensorRelEventPkp(4)']



x_y_plots = [""]

# 4. Definitions and notes for inv normal plot section


invNorm_plots = ["S_P2_CH_R_HJCrack_Pkp",
                    "S_P2_CH_L_HJCrack_Pkp",
                    "S_S2_G1_Pkp",
                    "S_S2_G2_Pkp",
                    "S_S2_G3_Pkp"]

# 5. Definitions and notes for Largest Events table
table_title2 = '' # title for the table
col_titles2 = ['','all time','last week'] # column titles
sensorStatisticsFields2=['SensorRelEventPkp(1)',
                        'SensorRelEventPkp(2)',
                        'SensorRelEventPkp(3)',
                        'SensorRelEventPkp(4)',
                        'SensorRelEventPkp(5)'] # what fields to do you want stats for?
sensorStatisticsNames2=['Sensor(1) Pkp',
                       'Sensor(2) Pkp',
                       'Sensor(3) Pkp',
                       'Sensor(4) Pkp',
                       'Sensor(5) Pkp'] # name to give in table?

stats_notes2 = 'This bit can include any special notes that you want to make about the statistics in this report. e.g. Note erroneous data arising due to blah blah. This will be automatically added as a special note to the end of the statistics summary section.'



## GENERATE PLOTS

generateTimeSeriesPlot(df_SS,"TIMESTAMP",timeseries_plots,'a temporary title','test_fig1.png','save')

generateTimeSeriesPlotZoomed(df_SS,"TIMESTAMP",timeseries_plots,'a temporary title','test_fig2.png','save')

generateXYPlot(df_SRES,XY_plot1,'linear',XY_plot1_title,'testXY1.png','save')

generateXYPlot(df_SRES,XY_plot2,'linear',XY_plot2_title,'testXY2.png','save')


## DEFINE CLASSES
class PDF(FPDF):
    def header(self):
        # Logo
        self.image(logo_path, 170, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
#        self.set_draw_color(0, 80, 180)
#        self.set_fill_color(230, 230, 0)
#        self.set_text_color(220, 50, 50)
#        # Thickness of frame (1 mm)
#        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 0, 0, 'C')
        # Line break
        self.ln(10)
        # Author and date
        self.cell(w, 9, author, 0, 0, 'R')        
        # Line break
        self.ln(20)
# define footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
# define the section title
    def section_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Section %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)
# define section body text from an external txt file
    def section_bodyLoadExternal(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
# define section body text from a variable.
    def section_body(self, txt):
        self.ln(0.5)
        effective_page_width=self.w-2*self.l_margin
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(effective_page_width, 5, txt)
        # Line break
        self.ln()
#        # Mention in italics
#        self.set_font('', 'I')
#        self.cell(0, 5, '(end of excerpt)')
# this will plot a NEW section of text.
    def print_fullSection(self, num, title, text_fill):
        self.add_page()
        self.section_title(num, title)
        self.section_body(text_fill)
# this will plot a NEW section of text.
    def print_text(self, text_fill):
        self.section_body(text_fill)
# this adds a new section with section header        
    def print_sectionHeader(self, num, title):
        self.add_page()
        self.section_title(num, title)
# this adds a time series plot (non-Zoomed)
    def print_timeSeriesPlot(self,fname,width,caption):
        effective_page_width=self.w-2*self.l_margin
        self.image(fname, x = None, y = None, w = width)
        self.cell(effective_page_width,0.0, caption,0,0,'L')
        pdf.ln(2)
# this adds a time series plot (Zoomed)        
    def print_timeSeriesPlotZoomed(self,fname,width,caption):
        effective_page_width=self.w-2*self.l_margin
        self.image(fname, x = None, y = None, w = width)
        self.cell(effective_page_width,0.0, caption,0,0,'L')
        pdf.ln(2)
# this adds a plot        
    def print_addPlot(self,fname,width,caption):
        effective_page_width=self.w-2*self.l_margin
        self.image(fname, x = None, y = None, w = width)
        self.cell(effective_page_width,0.0, caption,0,0,'L')
        pdf.ln(2)
# this adds the overview table
    def generateTableOverview(self,inputDataEvents,TimeIndex,table_title,col_titles,sensorStatisticsFields,sensorStatisticsNames):
        start_date = pd.to_datetime(inputDataEvents[TimeIndex].max())-datetime.timedelta(days=7)
        end_date = pd.to_datetime(inputDataEvents[TimeIndex].max())
        mask = (inputDataEvents[TimeIndex] > start_date) & (inputDataEvents[TimeIndex] <= end_date)
        inputDataEvents_stats_LastWeekFull = inputDataEvents.loc[mask]
        # define the dictionary for creating the table
        SRES_stats_overview = {
                        'Date start': [inputDataEvents[TimeIndex].min().strftime("%d-%m-%y %H:%M"),inputDataEvents_stats_LastWeekFull[TimeIndex].min().strftime("%d-%m-%y %H:%M")],
                        'Date end': [inputDataEvents[TimeIndex].max().strftime("%d-%m-%y %H:%M"),inputDataEvents_stats_LastWeekFull[TimeIndex].max().strftime("%d-%m-%y %H:%M")],
                        '# of Rel Events': [inputDataEvents.shape[0],inputDataEvents_stats_LastWeekFull.shape[0]],
                        'Events/day': [round(inputDataEvents.shape[0]/pd.to_numeric(datetime.timedelta.total_seconds(inputDataEvents["TIMESTAMP"].max()-inputDataEvents["TIMESTAMP"].min()) / (3600*24)),1),round(inputDataEvents_stats_LastWeekFull.shape[0]/pd.to_numeric(datetime.timedelta.total_seconds(inputDataEvents_stats_LastWeekFull["TIMESTAMP"].max()-inputDataEvents_stats_LastWeekFull["TIMESTAMP"].min()) / (3600*24)),1)]
                        }
        # add changing elements
        for i in range(0,len(sensorStatisticsNames)):
            SRES_stats_overview[sensorStatisticsNames[i]]=[round(inputDataEvents[sensorStatisticsFields[i]].max(),1),round(inputDataEvents_stats_LastWeekFull[sensorStatisticsFields[i]].max(),1)]
        # turn dictionary into df
        inputDataEvents_stats_overview = pd.DataFrame(SRES_stats_overview).T
        inputDataEvents_stats_overview.columns={'0':'','1':''}
        inputDataEvents_stats_overview.rename(columns={'0':'All time','1':'Last Two Weeks'}, inplace = True)
        set_table_dims = np.shape(inputDataEvents_stats_overview)
        # now define entry into PDF
        self.set_font('arial', 'B', 12)
        self.cell(60)
        self.cell(75, 10, table_title, 0, 2, 'C')
        self.cell(90, 10, " ", 0, 2, 'C')
        self.cell(-40)
        self.set_font('arial', 'BU', 12)
        # make titles of table
        for idx, word in enumerate(col_titles):
            if idx==0:
                self.cell(50, 10, str(word), 0, 0, 'C')
            elif idx!=len(col_titles)-1:
                self.cell(40, 10, str(word), 0, 0, 'C')
            elif idx==len(col_titles)-1:
                self.cell(40, 10, str(word), 0, 2, 'C')
        # add small vertical gap
        self.cell(-90)
        self.set_font('arial', '', 12)
        # fill data in
        for i in range(0, len(inputDataEvents_stats_overview)):
            self.cell(50, 10, '%s' % (inputDataEvents_stats_overview.index[i]), 0, 0, 'C')
            self.cell(40, 10, '%s' % (inputDataEvents_stats_overview.iloc[i,0]), 0, 0, 'C')
            self.cell(40, 10, '%s' % (inputDataEvents_stats_overview.iloc[i,1]), 0, 2, 'C')
            self.cell(-90)
        # add small vertical gap
        self.cell(90, 10, " ", 0, 2, 'C')
        self.cell(-30)
    def generateTableLargestEvents(self,inputData,noLargest,nCols,nRows,TimeIndex,table_title,col_titles,sensorStatisticsFields,sensorStatisticsNames):
        #   get the largest elements
        temporary = inputData.nlargest(noLargest,sensorStatisticsFields)
        SRES_stats_Top20 = temporary[[TimeIndex]+sensorStatisticsFields]
        #   make formatted dictionary
        SRES_stats_Top20_form = {TimeIndex: SRES_stats_Top20[TimeIndex].dt.strftime("%d-%m-%y %H:%M")}
        #   add variables
        for i in range(0,len(sensorStatisticsNames)):
            SRES_stats_Top20_form[sensorStatisticsNames[i]] = round(SRES_stats_Top20[sensorStatisticsFields[i]],1)
        # convert to dataframe
        df_SRES_stats_Top20=pd.DataFrame(SRES_stats_Top20_form)
    #   Make Full Page table. Set title
        self.set_xy(10,40)
        self.set_font('arial', 'B', 12)
        self.cell(60)
        self.cell(75, 10, table_title, 0, 2, 'C')
        self.cell(90, 10, " ", 0, 1, 'C')
        self.set_font('arial', 'B', 10)
    #   make column header 
        for i in range(0, nCols):
            if i==0:
                self.cell(30, 5,df_SRES_stats_Top20.columns[i], 'B', 0, 'C')
            elif i!=nCols-1:
                self.cell(30, 5,df_SRES_stats_Top20.columns[i], 'B', 0, 'C')
            elif i==nCols-1:
                self.cell(30, 5,df_SRES_stats_Top20.columns[i], 'B', 1, 'C')

#        self.cell(-90)
        self.set_font('arial', '', 9)
    #   fill data in for rest of table
        for i in range(0, nRows-1):
            for j in range(0, nCols):
                if j==0:
                    self.cell(30, 10, '%s' % (df_SRES_stats_Top20.iloc[i,j]), 0, 0, 'C')
                elif j!=nCols-1:
                    self.cell(30, 10, '%s' % (df_SRES_stats_Top20.iloc[i,j]), 0, 0, 'C')
                elif j==nCols-1:
                    self.cell(30, 10, '%s' % (df_SRES_stats_Top20.iloc[i,j]), 0, 1, 'C')
    #   finish table with some white space below
        self.cell(-90)
        self.cell(90, 10, " ", 0, 2, 'C')
        self.cell(-30)

## COMPILE PDF





pdf = PDF()
effective_page_width=pdf.w-2*pdf.l_margin
pdf.set_title(title) # change metadata title
pdf.set_author(author) # change metadata author

pdf.print_sectionHeader(1, 'Summary statistics')
pdf.generateTableOverview(df_SRES,"TIMESTAMP",table_title,col_titles,sensorStatisticsFields,sensorStatisticsNames)
pdf.print_text(stats_notes)

pdf.print_sectionHeader(2, 'Timeseries data')
pdf.print_timeSeriesPlot('test_fig1.png',190,'A caption')
pdf.print_timeSeriesPlotZoomed('test_fig2.png',190,'Another caption')

pdf.print_sectionHeader(3, 'X-Y data')
pdf.print_addPlot('testXY1.png',120,'Another caption')
pdf.print_addPlot('testXY2.png',120,'Another caption again')


pdf.print_sectionHeader(4, 'Inverse normal plots')
# Add inverse normal plots

pdf.print_sectionHeader(5, 'Largest events')
pdf.generateTableLargestEvents(df_SRES,10,6,11,"TIMESTAMP",table_title2,col_titles2,sensorStatisticsFields2,sensorStatisticsNames2)
pdf.print_text(stats_notes2)


pdf.output(output_name, 'F')