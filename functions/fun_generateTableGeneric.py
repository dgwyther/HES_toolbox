import datetime

import numpy as np
import pandas as pd

##############################################################
# generateTableGeneric(self, nRows, nCols, inputData)
# This function generates a FPDF table with the given number
# of rows (nRows) and columns (nCols) with the data given
# in the dataframe (inputData). Note that the size of inputData
# must match (nRows,nCols).
def generateTableGeneric(pdfObject,nRows,nCols,inputData):

#   Set title
    pdfObject.set_font('arial', 'B', 12)
    pdfObject.cell(60)
    pdfObject.cell(75, 10, table_title, 0, 2, 'C')
    pdfObject.cell(90, 10, " ", 0, 2, 'C')
    pdfObject.cell(-40)
    pdfObject.set_font('arial', 'BU', 12)
#   make column header 
    for i in range(0, nCols):
        if i==0:
            self.cell(40, 10,inputData.columns[i], 0, 0, 'C')
        elif i==nCols-1:
            self.cell(40, 10,inputData.columns[i], 0, 2, 'C')
        else:
            self.cell(40, 10,inputData.columns[i], 0, 0, 'C')

    pdfObject.cell(-90)
    pdfObject.set_font('arial', '', 12)
#   fill data in for rest of table
    for i in range(1, nRows): # and exclude first (title) row
        for j in range(0, nCols):
            if j==nCols-1:
                pdfObject.cell(40, 10, '%s' % (inputData.iloc[i,j]), 0, 2, 'C')
            else:
                pdfObject.cell(40, 10, '%s' % (inputData.iloc[i,j]), 0, 0, 'C')
#   finish table with some white space below
    pdfObject.cell(-90)
    pdfObject.cell(90, 10, " ", 0, 2, 'C')
    pdfObject.cell(-30)
