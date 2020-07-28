### Template file
# This file provides the layout and order template for the document.
## 

pdf.print_sectionHeader(1, 'Summary information')
#pdf.generateTableOverview(df_SRES,"TIMESTAMP",table_title,col_titles,sensorStatisticsFields,sensorStatisticsNames)
pdf.print_text(section1_notes)

pdf.print_sectionHeader(2, 'Beard plots')
for ii in range(1,NoTimeSeriesWithBeards+1):
    pdf.print_timeSeriesPlot('test_timeseriesBeards'+str(ii)+'.png',190,eval('caption_Beards'+str(ii)))

pdf.print_sectionHeader(3, 'Subplots')
for ii in range(1,NoTimeSeriesSubplots+1):
    pdf.print_timeSeriesPlot('test_timeseriesSubplots'+str(ii)+'.png',190,'A caption')

pdf.print_sectionHeader(4, 'Displaced timeseries')
for ii in range(1,NoTimeSeriesDisplaced+1):
    pdf.print_timeSeriesPlot('test_timeseriesDisplaced'+str(ii)+'.png',190,'A caption')

pdf.print_sectionHeader(5, 'Displaced timeseries with beards')
for ii in range(1,NoTimeSeriesDisplacedMinMaxAvg+1):
    pdf.print_timeSeriesPlot('test_timeseriesDisplacedMinMaxAvg'+str(ii)+'.png',190,'A caption')

for ii in range(1,NoTimeSeriesPlots+1):
    pdf.print_timeSeriesPlot('test_timeseries'+str(ii)+'.png',190,'A caption')
    pdf.print_timeSeriesPlotZoomed('test_timeseries_zoom'+str(ii)+'.png',190,'Another caption')
