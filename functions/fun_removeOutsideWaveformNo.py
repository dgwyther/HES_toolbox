import pandas as pd

def removeOutsideWaveformNo(inputData,removeStart,removeEnd):
	for r in range(0,len(removeStart)):
		mask = (inputData['waveformIndex']>=removeStart[r]) & (inputData['waveformIndex']<=removeEnd[r])
		inputData.drop(inputData.index[~mask], inplace=True)
		return inputData
