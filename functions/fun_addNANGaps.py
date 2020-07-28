import pandas as pd

def addNANGaps(inputData,TimeIndex,sampleInterval):
    inputData = inputData.set_index(TimeIndex).asfreq(sampleInterval).reset_index()
    return inputData
