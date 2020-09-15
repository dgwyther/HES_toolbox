### Template file
# This file provides the layout and order template for the document.
##

pdf.print_sectionHeader(1, 'Summary information')
pdf.print_text(section1_notes)
DateStatsTable = pd.DataFrame( [['Start date:',df_SS["TIMESTAMP"].min().strftime("%Y-%m-%d")],
                                ['End date:',df_SS["TIMESTAMP"].max().strftime("%Y-%m-%d")],
                                ['duration (days):',round((df_SS["TIMESTAMP"].max()-df_SS["TIMESTAMP"].min()).total_seconds()/(60*60*24),1)]], columns=
                                [' ',' '])
pdf.generateTableGeneric(3,2,table_title1,DateStatsTable)
pdf.print_text(' ')

pdf.print_sectionHeader(2, 'Battery Voltages')
pdf.print_timeSeriesPlot('test_timeseries1.png',190,caption_timeseries1)

pdf.print_sectionHeaderPageBreak(3, 'Panel temperatures')
pdf.print_timeSeriesPlot('test_timeseries2.png',190,caption_timeseries2)

# pdf.print_sectionHeader(3, 'Subplots')
# for ii in range(1,NoTimeSeriesSubplots+1):
    # pdf.print_timeSeriesPlot('test_timeseriesSubplots'+str(ii)+'.png',190,'A caption')

# pdf.print_sectionHeaderPageBreak(4, 'Longitudinal Displacements')
# for ii in range(1,2):
#     pdf.print_timeSeriesPlot('test_timeseriesDisplacedMinMaxAvg'+str(ii)+'.png',190,'')
#
# pdf.print_sectionHeader(5, 'Vibrating Wire Strains')
# for ii in range(2,NoTimeSeriesDisplacedMinMaxAvg+1):
#     pdf.print_timeSeriesPlot('test_timeseriesDisplacedMinMaxAvg'+str(ii)+'.png',190,'')
#
# pdf.print_sectionHeader(6, 'Weather')
# pdf.image('tmp.chart-1.png', x=None, y=None, w=190)
# pdf.print_text('Red: Temperature. Blue: Rainfall since 9:00AM. Black triangle: Wind gust. Grey line: Wind speed.')

# for ii in range(1,NoTimeSeriesPlots+1):
    # pdf.print_timeSeriesPlot('test_timeseries'+str(ii)+'.png',190,'A caption')
    # pdf.print_timeSeriesPlotZoomed('test_timeseries_zoom'+str(ii)+'.png',190,'Another caption')
