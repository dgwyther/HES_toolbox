import pandas as pd
import numpy as np

from fun_loadData import loadData
from fun_applyAliasTable import applyAliasTable

def searchForErroneousData(inputDataName,TimeIndex,**kwargs):
    inputData,colNames = loadData(inputDataName,TimeIndex)
    
    if ('aliasTable' in kwargs):
        aliasTable=kwargs['aliasTable']
        applyAliasTable(inputData,aliasTable)
        
    if ('method' in kwargs):
        if kwargs['method']=='threshold':
            threshold = kwargs['thresholdValue']
            for var in list(inputData.columns.values)[2:]:
                mask = inputData[var]>=threshold
                print(' ')
                for ii in range(0,len(mask)):
                    if mask[ii]:
                        print(inputData[TimeIndex][ii], var, inputData[var][ii])
