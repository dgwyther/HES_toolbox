import argparse

import pandas as pd
import numpy as np

from functions.fun_loadData import loadData
from functions.fun_applyAliasTable import applyAliasTable

parser = argparse.ArgumentParser(description='Check for erroneous data')

parser.add_argument('--inputDataName', metavar='inputDataName', help='path/filename to the input date')
parser.add_argument('--TimeIndex', help='name for the time index, e.g. "TIMESTAMP"')
parser.add_argument('--aliasTable', help='path/filename to the alias Table')
parser.add_argument('--method', help='what method for error detection do you want? options: threshold')
parser.add_argument('--thresholdValue', type=int, help='what threshold value do you want?')


args = parser.parse_args()


inputData,colNames = loadData(args.inputDataName,args.TimeIndex)

if args.aliasTable:
    applyAliasTable(inputData,args.aliasTable)

iii = 0
if args.method=='threshold':
    threshold = args.thresholdValue
    print(' ')
    for var in list(inputData.columns.values)[2:]:
        mask = inputData[var]>=threshold
        for ii in range(0,len(mask)):
            if mask[ii]:
                print(inputData[args.TimeIndex][ii], var, inputData[var][ii])
                iii=iii+1
        if any(mask): #add line break if any found
            print(' ')
    print('total erroneous points found: '+str(iii))
    print('computed with '+args.method+' method with threshold of '+str(threshold))