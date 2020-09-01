import pandas as pd
import numpy as np

def addWaveformIndex(inputData,TimeIndex,Interval):
# look for time gap intervals greater than a defined interval (seconds)
    inputData['timeGapBool']=(inputData[TimeIndex].diff().dt.seconds)>Interval
# increment a column called waveformIndex by 1 whenever a True is found
    inputData['waveformIndex']=np.nan
    loop_ind=1;
    for nn in range(0,len(inputData['timeGapBool'])):
        if inputData['timeGapBool'][nn]==True:
            loop_ind=loop_ind+1
        inputData.loc[nn,'waveformIndex']=loop_ind
    inputData['waveformIndex'] = inputData['waveformIndex'].astype(int)
    print(str(len(inputData.loc[inputData[TimeIndex].diff().dt.seconds>Interval, TimeIndex]))+' events found')
    print('row number and timestamp for events are:')
    print(str(inputData.loc[inputData[TimeIndex].diff().dt.seconds>Interval, TimeIndex]))
    return inputData

