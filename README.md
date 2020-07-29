# HES_toolbox
This repository contains assorted tools for HES work.

## Requirements
Written and tested with `python3`. Dash works with `python2.7`. Requirements given in `requirements.txt`.

## Install
0. Suggest using an anaconda environment.
1. `git clone` to local environment
2. Install requirements with `$ pip install -r requirements.txt`
3. Voila!

## Toolbox structure
Comments below show the purpose of each folder or file:
```
HES_toolbox/
├── assets							# styles, logos or repeatedly used files
│   ├── header.css
│   ├── logo.png
│   └── print_setup.css
├── functions						# stand-alone functions called by other functions
│   ├── ClassPDF.py						# class file for reporting with FPDF
│   ├── fun_applyAliasTable.py
│   ├── fun_generateInvNormPlot.py
│   ├── fun_generateTableGeneric.py
│   ├── fun_generateTableOverview.py
│   ├── fun_generateTimeSeriesPlots.py
│   ├── fun_generateXYPlot.py
│   ├── fun_loadData.py
│   ├── fun_removeDates.py
│   └── __init__.py
├── README.md							# Readme file
├── reportDriver.py						# Driver script for generating reports with fpdf
├── reportSimpleDASH.py					# Script to generate report with plotly-dash
├── reportSimplePDF.py					# Script to generate reports with fpdf
├── reportTemplate.py					# user template file called by `reportDriver.py`
└── requirements.txt					# package requirements
```

## Main files
- `reportSimpleDASH.py`: Run this file with `python3 reportSimpleDASH.py` to produce a simple dashboard report. View in browser at `http://127.0.0.1:8050`. It can be printed to PDF using the browser Print option.
- `reportSimplePDF.py`: compile a pdf directly with `python3 reportSimplePDF.py`. To change compilation options (including which layout, variables to include in plots, which plots to include, title, author, captions, etc), edit the file `reportSimplePDF.py`.
- `reportDriver.py`: compile a pdf with the same FPDF package as `reportSimplePDF.py`. With `reportDriver.py` all user input is split into a separate template file (e.g. `reportTemplate.py`) which is loaded by the `reportDriver.py` to compile the PDF. Run with `python3 reportDriver.py`.

### reportSimplePDF.py
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

### reportDriver.py
This is an alternative method for compiling a PDF using the FPDF library, similar to using `reportSimplePDF.py`. However, this method separates out the driver (that compiles the PDF) from the template file (which contains all user input and definitions).

#### 1. Set the user config file:
See for example `reportConfig_CCB_NB.py`. 

1. First set the global definitions (e.g. title, author, output_name); the file locations and the names of the columns in the `.dat` file; and, what to alias those names as.
2. Summary table: Set the title, column names, fields and names to show in the table. Optionally, include some notes about this table.
3. Time series plots: Set how many plots you want, then include a definition `timeseries_plotX = ["first_variable","etc"]` where `X` is increments for each plot.
4. XP plots. Same as for Timeseries plots.
5. Inverse Normal plots. Same as for Timeseries plots. In addition, set the bin increments and fitting limits.
6. Largest events table: Set the title, column titles and fields.

#### 2. Set the user template file
See for example `reportTemplate_CCB_NB.py`. 

1. Set the template for the report. For example, add new sections with section headers, plots for each section

#### 2. Run `reportDriver.py`
Now run `python3 reportDriver.py` to load the user definitions and compile the output PDF.


### Credits:
David E. Gwyther
