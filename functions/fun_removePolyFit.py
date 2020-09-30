import datetime
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt



def removePolyFit(inputData, TimeIndex, fieldName, newFieldName, **keyword_parameters):
	print('removing a polynomial fit through variable '+fieldName)
	maskFieldNans = np.isfinite(inputData[fieldName]) # mask of where NaN locations
	t = mdates.date2num(inputData[TimeIndex][maskFieldNans])
	z2 = np.polyfit(t, inputData[fieldName][maskFieldNans], 2) 	# do the fit
	p2 = np.poly1d(z2) 											# make a 1d polynomial object
	fit = p2(mdates.date2num(inputData[TimeIndex]))				# fit the object back to the original dates
	output = inputData[fieldName]-fit + fit[0]					# remove polynomial and shift back up with first value
	inputData[newFieldName]=output
	if ('includeMinMax' in keyword_parameters and keyword_parameters['includeMinMax'] == 'yes'):
		print('also removing same fit from '+fieldName[:-4]+'_Min'+' and '+fieldName[:-4]+'_Max')
		outputMin = inputData[fieldName[:-4]+'_Min'] - fit + fit[0]
		outputMax = inputData[fieldName[:-4]+'_Max'] - fit + fit[0]
		inputData[newFieldName[:-4]+'_Min']=outputMin
		inputData[newFieldName[:-4]+'_Max']=outputMax
	if ('plot' in keyword_parameters and keyword_parameters['plot'] == 'yes'):
		fig, ax = plt.subplots()
		ax.plot(inputData["TIMESTAMP"], output, '+', color='r')
		ax.plot(inputData["TIMESTAMP"], fit, '-g')
		ax.plot(inputData["TIMESTAMP"], inputData[fieldName], '+', color='b')
		plt.show()
		print(inputData[fieldName], inputData[newFieldName], inputData[newFieldName[:-4]+'_Min'], inputData[newFieldName[:-4]+'_Max'])
	print('returning new data fields in '+newFieldName,end='')
	if ('includeMinMax' in keyword_parameters and keyword_parameters['includeMinMax'] == 'yes'): print(', '+newFieldName[:-4]+'_Min'+' and in '+newFieldName[:-4]+'_Max')
	print('')
	return inputData
