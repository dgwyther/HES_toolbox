#module functions
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#local functions
from functions.fun_loadData import loadData
from functions.fun_applyAliasTable import applyAliasTable
from functions.fun_addWaveformIndex import addWaveformIndex
from functions.fun_generateWaveformPlots import generateWaveformPlot
from functions.fun_removeOutsideDates import removeOutsideDates

# filename settings
SWfm_filename = '../SampleData/HE602_3680_RV50_CCB_SB_SensorWfm.dat'
TimeIndex="TIMESTAMP"

# alias settings
loadAlias='none'
aliasTablePath = '../SampleData/tmp.TMR701_RV50_CCB_NB_aliasTable.csv'

# event settings
Interval = 0.05 #seconds
dateRangeStart=['2020-AUG-26 00:01']
dateRangeEnd=  ['2020-AUG-27 00:00']

# plot settings
plotVariables=['microS1T20Rel(1)',
                'microS1T20Rel(2)',
                'microS1T20Rel(3)',
                'microS1T20Rel(4)',
                'microS1T20Rel(5)',
                'microS1T20Rel(6)',
                'microS1T20Rel(7)',
                'microS1T20Rel(8)']
nRows=10
nCols=2
fname='test_waveformsubplots'
plot_or_save='save'

########################## NO EDITS BELOW #############

# Load data
if 'SWfm_filename' in locals():
    print('loading data from '+SWfm_filename)
    df_SWfm,colNamesSWfm = loadData(SWfm_filename,TimeIndex)



# Alias data
if loadAlias=='csv':
    aliasTable_FromCSV=readAliasCSV(aliasTablePath)
    applyAliasTable(df_SWfm,aliasTable_FromCSV)

# Remove data outside of dateInterval
print(df_SWfm)
df_SWfm = removeOutsideDates(df_SWfm,TimeIndex,dateRangeStart,dateRangeEnd)
print('keeping events only between',dateRangeStart,' to ',dateRangeEnd)
print(df_SWfm)
# Find events
df_SWfm = addWaveformIndex(df_SWfm,TimeIndex,Interval)

generateWaveformPlot(df_SWfm, TimeIndex, plotVariables, nRows, nCols, fname, plot_or_save,'shareXaxis')

# # Plot events
# nRows=10
# nCols=2
# fig, axs = plt.subplots(nRows, nCols, figsize=(10, 15), dpi=100, sharex=True)
# for jj in range(0,math.ceil(df_SWfm['waveformIndex'].iloc[-1]/(nRows*nCols))):
    # fig, axs = plt.subplots(nRows, nCols, figsize=(10, 15), dpi=100, sharex=True)
    # axIndex=1;
    # for nn in range(nRows*nCols*jj+1,nRows*nCols*(jj+1)+1):
        # if nn > df_SWfm['waveformIndex'].iloc[-1]: #don't do anything if we hit the last waveformIndex
            # continue
        # ax = axs.ravel()[axIndex-1]
        # toPlotX = df_SWfm[TimeIndex].loc[df_SWfm['waveformIndex']==nn]-df_SWfm[TimeIndex].loc[df_SWfm['waveformIndex']==nn].iloc[0]
        # for vv,vname in enumerate(plotVariables):
            # toPlotY = df_SWfm[vname].loc[df_SWfm['waveformIndex']==nn]
            # _ = ax.plot(toPlotX.dt.total_seconds(), toPlotY, label=vname)
        # ax.grid(b=True, which='major', color='#666666', linestyle='-')
        # ax.minorticks_on()
        # ax.grid(b=True, which='minor', color='#999999', linestyle='-',alpha=0.2)
        # ax.spines['top'].set_visible(False)
        # ax.spines['right'].set_visible(False)
        # _=ax.text(0.5,0.86,df_SWfm[TimeIndex].loc[df_SWfm['waveformIndex']==nn].iloc[0], horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        # axIndex=axIndex+1;
    # leg = ax.legend(bbox_to_anchor=(-1.1, -.75, -2, .102), loc=3, ncol=4, frameon=False)
    # leg.set_in_layout(False)
    # plt.grid(True)
    # plt.tight_layout(rect=[0,0.031,1,1])
    # print('saving figure number '+str(jj+1))
    # plt.savefig('test_waveformsubplots'+str(jj+1)+'.png')
    # plt.close()





# plt.figure(figsize=(10, 15),facecolor='white', dpi=200)
# nRows=10
# nCols=2
# # plot numbering starts at 1, not 0
# plot_number = 1
# for waveformIndex, selection in list(df_SWfm.groupby("waveformIndex"))[0:nRows*nCols]:
    # print(waveformIndex)
    # ax = plt.subplot(nRows, nCols, plot_number);
    # _ = selection.plot(x=TimeIndex, y=plotVariables, ax=ax, legend=False);
    # _ = ax.set_xlabel('')
    # plt.grid(True)
    # plt.tight_layout()
    # # Go to the next plot for the next loop
    # plot_number = plot_number + 1
# #

# plt.tight_layout()
# #plt.show()
# plt.savefig('test_waveformsubplots.png')




# nRows=10
# nCols=2
# fig, axes = plt.subplots(nRows, nCols, sharex=True, sharey=True, figsize=(10,15))
# axes_list = [item for sublist in axes for item in sublist]

# for waveformIndex, selection in list(df_SWfm.groupby("waveformIndex"))[0:nRows*nCols]:
    # ax = axes_list.pop(0)
    # selection.plot(x=TimeIndex, y=plotVariables, ax=ax, legend=False)
# #    ax.set_title(countryname)
# #    ax.tick_params(
# #        which='both',
# #        bottom='off',
# #        left='off',
# #        right='off',
# #        top='off'
# #    )
# #    ax.spines['left'].set_visible(False)
# #    ax.spines['top'].set_visible(False)
# #    ax.spines['right'].set_visible(False)

# # Now use the matplotlib .remove() method to
# # delete anything we didn't use
# for ax in axes_list:
    # ax.remove()








# if plot_or_save=='plot':
    # plt.show()
# elif plot_or_save=='save':
    # plt.savefig(fname)
