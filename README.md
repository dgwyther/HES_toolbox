# HES Toolbox
This repository contains assorted tools for HES work.
D.Gwyther 2019-2020

## Contents
- [Install](#install)
- [Toolbox structure](#toolbox-structure)
- [Use case: Generating a report with FPDF](#report-generation)
  - [Data preparation](#report-data-prep)
  - [User config](#report-config)
  - [Template](#report-template)
  - [Report Driver](#report-driver)
- [Use case: Generating a report for a new site](#new-report-generation)
- [Use case: Generating a report with Dash](#dash-report)

## Requirements
Written and tested with `python3`. Dash works with `python2.7`. Requirements given in `requirements.txt`.

## Install
0. Suggest using an anaconda environment.
1. Activate the python 3.7 environment and change the desired directory
1. `git clone git@github.com:dgwyther/HES_toolbox.git` will clone this package to the current directory within a new folder called `HES_toolbox`. Alternatively, if you wish to control the folder name it is cloned into: `git clone git@github.com:dgwyther/HES_toolbox.git HES_toolbox_CCB_reports` will clone into `HES_toolbox_CCB_reports`.
2. Install requirements with `$ pip install -r requirements.txt`. Or, run the toolbox (with `python3 reportDriver_*.py`) and install the packages asked for in the error code.
3. To create a report, call python on the driver scripts like: `python3 reportDriver_*.py`.

## Toolbox structure
Comments below show the purpose of each folder or file:
```
HES_toolbox/
├── assets							# styles, logos or repeatedly used files
│   ├── header.css
│   ├── logo.png
│   └── print_setup.css
├── development           # files currently not being used or in dev.
│   ├── reportSimpleDASH.py					# Script to generate report with plotly-dash
│   └── reportSimplePDF.py					# Script to generate reports with fpdf
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
├── reportDriver_*.py						# Driver script for generating reports with fpdf
├── reportDataPrep_*.py					# data cleaning & prep that is called by `reportDriver_*.py`
├── reportConfig_*.py					# plot config called by `reportDriver_*.py`
├── reportTemplate_*.py					# report template file called by `reportDriver_*.py`
└── requirements.txt					# package requirements
```

## Report Generation
The process for generating a report is outlined below. Also, in the next subsections, each constituent file is detailed.
1. Prepare the input data through removal of erroneous data, adding of NaN's to any data gaps, etc using the file `reportDataPrep_*.py`.

2. Set the user configuration options, such as the title, date, data path and plotting choices in `reportConfig_*.py`.

3. Set the layout for the report in `reportTemplate_*.py`. For example, add new sections, plots, captions.

4. Run `python3 reportDriver._*py`to load the project data, user definitions and compile the output PDF.

#### Report Data prep

#### Report Config
This file is used to set the logo, metadata and output options, as well the all important plotting options.

Logo, metadata and output options:
```
title = 'Example title that is about the same length '
author = 'Example author and date'
logo_path = 'assets/logo.png'
output_name = 'test.pdf'
```

This file also sets the data path and the aliasing options. Data settings including input filenames and column names are used to `loadData`:
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

Then, choices for plotting are set, such as:
- options for the summary table
- options for any time series plots (with and without beards)
- options for any X-Y plots
- options for any displaced plots
- options for any inverse normal plots
- options for a largest event table.

#### Report Template

This file sets the layout for the final report. A simple layout would look like this:
```
pdf = ClassPDF(logo_path=logo_path,title=title,author=author)
pdf.print_sectionHeader(1, 'The only section')
pdf.print_text('some notes;)
pdf.print_timeSeriesPlot('test_fig1.png',190,'A caption')
pdf.print_text('some more notes')
pdf.output(output_name, 'F')
```

#### Report Driver

The driver file is the driver for the report generation process. It first loads (i.e. it runs) the config file. It then loads the data, applies the aliases and applies the data prep file. It then generates the figures, which are defined as on/off in the config file. Lastly, it creates the PDF class object and loads the template file, before making the actual output PDF.

The only editable section of the driver file is below the loading of functions/modules, where 3 lines define the config, template and data prep files:

```
# DEFINE TEMPLATE AND CONFIG FILE:
configFile = 'reportConfig_CCB_NB.py'
templateFile = 'reportTemplate_CCB_NB.py'
dataPrepFile = 'reportDataPrep_CCB_NB.py'
```

## New Report Generation
If you require a new report, there is a standard process for creating the new report. The process will depend on whether the report is for a completely new site, or if it is a new type of report for an existing site (e.g. diagnostic report, troubleshooting report, internal report, TMR report, etc).

- If the new report is for a new sensor site, then all files will need to be copy and modified for this new site. The new config file should contain the prescription for which plots you require. The new template file should outline the order and captions of the new report. If you don't require a different report outline, then there could be a generic template that is used for different reports (e.g. the diagnostics template for CCB_NB and CCB_SB is virtually identical). Lastly, a data prep file will need to be written for each site. As time progresses, you may find you need to edit the data prep file occasionally to deal with data errors and outages. Lastly, the driver file will need to be edited (at the top) to specify the config, template and data prep files.
- If the new report is a different report for an existing site, then the existing reportDataPrep_*.py file can be used. For example, a diagnostics report for an existing site would use the existing data prep file for that site. Likewise, if a report needs to be produced for a different end-user (e.g. internal reporting vs. for the instrument manufacturer), then the same data prep file would be used. In both of these cases, a new/modified template file and config file would be needed. As the driver calls the config, template and data prep files, the driver file would need to be modified to point to the new files.

## Dash Report
- `reportSimpleDASH.py`: Run this file with `python3 reportSimpleDASH.py` to produce a simple dashboard report. View in browser at `http://127.0.0.1:8050`. It can be printed to PDF using the browser Print option.




### Credits:
David E. Gwyther
