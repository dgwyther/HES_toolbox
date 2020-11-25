import pandas as pd

def addNANGaps(inputData,TimeIndex,sampleInterval):
#    r = pd.date_range(start=inputData[TimeIndex].min(), end=inputData[TimeIndex].max(), freq=sampleInterval)
#    print(r)
#    inputData.set_index('TIMESTAMP').reindex(r).fillna(0.0).rename_axis('TIMESTAMP').reset_index()
    inputData = inputData.set_index(TimeIndex).asfreq(sampleInterval).reset_index()
    return inputData
