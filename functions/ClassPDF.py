import datetime
import numpy as np
import pandas as pd
from fpdf import FPDF
# Note that as I separated this class into a separate module file, there had to be some jury-rigging to get this to work nicely with the in-built module fpdf.py. 
# - For example, I had to add the __init__ constructor, which will pull through the local variables logo_path etc into this class definition. 
# I also had to add the super() to take the fpdf.py class definitions into THIS file. AND,
# I had to change the effective_page_width to be twice as big for SOME reason. (Something in fpdf.py is not talking to this).
class ClassPDF(FPDF):
    def __init__(self, **kwargs):
        super().__init__() 
        keys = [*kwargs]
        self.logo_path = 0 if 'logo_path' not in keys else kwargs['logo_path']
        self.title = 0 if 'title' not in keys else kwargs['title']
        self.author = 0 if 'author' not in keys else kwargs['author']
# define constructor        
    def header(self):
        # Logo
        self.image(self.logo_path, 170, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        self.w = self.get_string_width(self.title) + 6
        self.set_x((210 - self.w) / 2)
        # Colors of frame, background and text
#        self.set_draw_color(0, 80, 180)
#        self.set_fill_color(230, 230, 0)
#        self.set_text_color(220, 50, 50)
#        # Thickness of frame (1 mm)
#        self.set_line_width(1)
        # Title
        self.cell(self.w, 9, self.title, 0, 0, 'C')
        # Line break
        self.ln(10)
        # Author and date
        self.cell(self.w, 9, self.author, 0, 0, 'R')        
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
        effective_page_width=self.w-2*self.l_margin
        self.cell(effective_page_width*2, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
# define the section title
    def section_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        effective_page_width=self.w-2*self.l_margin
        self.cell(effective_page_width*2, 6, 'Section %d : %s' % (num, label), 0, 1, 'L', 1)
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
        self.multi_cell(effective_page_width*2, 5, txt)
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
        self.ln(2)
# this adds a time series plot (Zoomed)        
    def print_timeSeriesPlotZoomed(self,fname,width,caption):
        effective_page_width=self.w-2*self.l_margin
        self.image(fname, x = None, y = None, w = width)
        self.cell(effective_page_width,0.0, caption,0,0,'L')
        self.ln(2)
# this adds a plot        
    def print_addPlot(self,fname,width,caption):
        effective_page_width=self.w-2*self.l_margin
        self.image(fname, x = None, y = None, w = width)
        self.cell(effective_page_width,0.0, caption,0,0,'L')
        self.ln(2)
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
        self.set_font('arial', 'B', 9)
    #   make column header 
        for i in range(0, nCols):
            if i==0:
                self.cell(32, 5,df_SRES_stats_Top20.columns[i], 'B', 0, 'C')
            elif i!=nCols-1:
                self.cell(32, 5,df_SRES_stats_Top20.columns[i], 'B', 0, 'C')
            elif i==nCols-1:
                self.cell(32, 5,df_SRES_stats_Top20.columns[i], 'B', 1, 'C')

#        self.cell(-90)
        self.set_font('arial', '', 9)
    #   fill data in for rest of table
        for i in range(0, nRows-1):
            for j in range(0, nCols):
                if j==0:
                    self.cell(32, 10, '%s' % (df_SRES_stats_Top20.iloc[i,j]), 0, 0, 'C')
                elif j!=nCols-1:
                    self.cell(32, 10, '%s' % (df_SRES_stats_Top20.iloc[i,j]), 0, 0, 'C')
                elif j==nCols-1:
                    self.cell(32, 10, '%s' % (df_SRES_stats_Top20.iloc[i,j]), 0, 1, 'C')
    #   finish table with some white space below
        self.cell(-90)
        self.cell(90, 10, " ", 0, 2, 'C')
        self.cell(-30)
