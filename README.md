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

### Credits:
David E. Gwyther
