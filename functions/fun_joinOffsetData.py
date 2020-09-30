import pandas as pd
import numpy as np


def joinOffsetData(inputData,TimeIndex,Variable,shiftTime,shiftValue):
    for r,var in enumerate(Variable):
        mask = (inputData[TimeIndex]>=shiftTime[r])
        inputData[var].where(~mask, other=inputData[var]+shiftValue[r],inplace=True)
    print('re-aligned and joined '+str(len(Variable))+' variables:')
    print(Variable)
    print('by the following amounts: ')
    print(shiftValue)
    print('')
