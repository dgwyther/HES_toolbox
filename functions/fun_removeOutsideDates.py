import pandas as pd

def removeOutsideDates(inputData,TimeIndex,removeStart,removeEnd):
	for r in range(0,len(removeStart)):
		mask = (inputData[TimeIndex]>=removeStart[r]) & (inputData[TimeIndex]<=removeEnd[r])
		inputData.drop(inputData.index[~mask], inplace=True)
		return inputData
