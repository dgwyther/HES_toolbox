import pandas as pd
import numpy as np


def removeVariableBetweenDates(inputData,TimeIndex,Variable,removeStart,removeEnd):
    for ii,var in enumerate(Variable):
        for r in range(0,len(removeStart)):
            mask = (inputData[TimeIndex]>=removeStart[r]) & (inputData[TimeIndex]<=removeEnd[r])
            inputData[var].where(~mask, other=np.NaN, inplace=True)
