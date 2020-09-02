import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num

def generateWaveformPlot(inputData,TimeIndex,plotVariables,nRows,nCols, fname,plot_or_save,*args):
    for jj in range(0,math.ceil(inputData['waveformIndex'].iloc[-1]/(nRows*nCols))):
        if ('shareXaxis' in args):
            fig, axs = plt.subplots(nRows, nCols, figsize=(10, 15), dpi=100, sharex=True)
        else:
            fig, axs = plt.subplots(nRows, nCols, figsize=(10, 15), dpi=100, sharex=False)
        axIndex=1;
        for nn in range(nRows*nCols*jj+1,nRows*nCols*(jj+1)+1):
            if nn > inputData['waveformIndex'].iloc[-1]: #don't do anything if we hit the last waveformIndex
                continue
            ax = axs.ravel()[axIndex-1]
            toPlotX = inputData[TimeIndex].loc[inputData['waveformIndex']==nn]-inputData[TimeIndex].loc[inputData['waveformIndex']==nn].iloc[0]
            for vv,vname in enumerate(plotVariables):
                toPlotY = inputData[vname].loc[inputData['waveformIndex']==nn]
                _ = ax.plot(toPlotX.dt.total_seconds(), toPlotY, label=vname)
            ax.grid(b=True, which='major', color='#666666', linestyle='-')
            ax.minorticks_on()  
            ax.grid(b=True, which='minor', color='#999999', linestyle='-',alpha=0.2)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            _=ax.text(0.5,0.86,inputData[TimeIndex].loc[inputData['waveformIndex']==nn].iloc[0], horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
            axIndex=axIndex+1;
        leg = ax.legend(bbox_to_anchor=(-1.1, -.75, -2, .102), loc=3, ncol=4, frameon=False)
        leg.set_in_layout(False)
        plt.grid(True)
        plt.tight_layout(rect=[0,0.031,1,1])
        if plot_or_save=='plot':
            plt.show()
        elif plot_or_save=='save':
            print('saving figure number '+str(jj+1))
            plt.savefig(fname+str(jj+1)+'.png')
        plt.close()
