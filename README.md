# HES_toolbox
This repository contains assorted tools for HES work.

## Requirements
Written and tested with `python3`. Dash works with `python2.7`. Requirements given in `requirements.txt`.

## Install
0. Suggest using an anaconda environment.
1. `git clone` to local environment
2. Install requirements with `$ pip install -r requirements.txt`
3. Voila!

## Main files
- `reportSimpleDASH.py`: Run this file with `python3 reportSimpleDASH.py` to produce a simple dashboard report. View in browser at `http://127.0.0.1:8050`. It can be printed to PDF using the browser Print option.
- `reportSimplePDF.py`: compile a pdf directly with `python3 reportSimplePDF.py`. To change compilation options (including which layout, variables to include in plots, which plots to include, title, author, captions, etc), edit the file `reportSimplePDF.py`.

### reportSimplePDF.pdf
To configure, set the following options in `reportSimplePDF.py`, which is split up into Configuration, Analysis and Compilation sections:
#### Configuration options
Logo, metadata and output options:
```
title = 'Example title that is about the same length '
author = 'Example author and date'
logo_path = 'assets/logo.png'
output_name = 'test.pdf'
```

Data settings including input filenames and column names which are used to `loadData`:
```
SRES_filename = 'Data/SensorRelEventStats.dat'
colNamesSRES = ["col1","col2","col3","etc"]
df_SRES = loadData(SRES_filename,"TIMESTAMP",colNamesSRES)
```
Note that the second argument to `loadData` is the name of the column that contains time data, e.g. `"TIMESTAMP"`.

Variables can be aliased with the `applyAliasTable` function, which takes the input file and an alias table as arguments, like `applyAliasTable(inputData,aliasTable)`. The aliasTable must be defined in the following manner:
```
aliasTable = {
  "inputvariable":"aliased name",
  "anothervariable":"the new name",
  "TIMESTAMP":"TIMESTAMP"}
```
Note that I've kept `TIMESTAMP` as `TIMESTAMP`, and order should not matter.
#### Analysis options
- set options for the summary table

- set options for any time series plots

- set options for any X-Y plots

- set options for any inverse normal plots

- set options for a largest event table.

#### Compilation options
Here, you can add or remove plots, tables, text, caption to suit. For example, a simple report would be:
```
pdf = ClassPDF(logo_path=logo_path,title=title,author=author)
pdf.print_sectionHeader(1, 'The only section')
pdf.print_text('some notes;)
pdf.print_timeSeriesPlot('test_fig1.png',190,'A caption')
pdf.print_text('some more notes')
pdf.output(output_name, 'F')
```
A more complex template is provided in the default `reportSimplePDF.py`, which includes a table of summary statistics followed by some general notes; 2 plots of timeseries data; 2 plots of X-Y data; 1 inverse normal plot; and, a largest event table followed by some notes. Each section is separated by a section title and a page break.



### Credits:
David E. Gwyther
