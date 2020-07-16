import datetime

import pandas as pd
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
import numpy as np
from scipy import stats

def generateInvNormPlot(inputData,TimeIndex,InvNorm_toPlot,InvNormBinStart,InvNormBinInc,InvNormBinEnd,InvNormMin,InvNormMax,title,fname,plot_or_save):
#   Calculate constants
    Events_per_day = len(inputData)/pd.to_numeric(datetime.timedelta.total_seconds(inputData[TimeIndex].max()-inputData[TimeIndex].min()) / (3600*24))
    ET_ARI1day = -stats.norm.ppf(1/Events_per_day)
    ET_95in1day = -stats.norm.ppf(1/(20*Events_per_day+1))
    ET_95in1year = -stats.norm.ppf(1/(20*365*Events_per_day+1))
    ET_95in100year = -stats.norm.ppf(1/(20*100*365*Events_per_day+1))


    fig, ax = plt.subplots(figsize=(10, 5), dpi=100)

    for var in InvNorm_toPlot:
    #    bin the data
        IN_binned,IN_edges = np.histogram(inputData[var],np.arange(InvNormBinStart,InvNormBinEnd+InvNormBinInc,InvNormBinInc))
        binEdgesToPlot = IN_edges[1:] # shift bin edge to the upper edge for plotting
        IN_cdf = pd.DataFrame({"cdf": IN_binned.cumsum()})
        IN_cdf["edges"] = binEdgesToPlot #add new column
        IN_cdf.mask((IN_cdf == IN_cdf.shift(1)) | (IN_cdf == 0), inplace=True) #remove duplicate bins
        idx = np.isfinite(IN_cdf["cdf"].to_numpy()) # make mask for NaN values
    #   make the inverse of the normal prob CDF
        with np.errstate(invalid='ignore'):
            IN_cdf["InvSNCDF"] = pd.DataFrame(stats.norm.ppf(IN_cdf["cdf"]/(inputData[var].count()+1))) # and mask by idx to remove NaNs
    #   make a fit line through data
        xLims =np.array([0,ET_95in100year])
        IN_cdf_fitLims = IN_cdf[(IN_cdf["InvSNCDF"] >= InvNormMin) & (IN_cdf["InvSNCDF"] <= InvNormMax)]
        mask_nan_fitLims = np.isfinite(IN_cdf_fitLims["cdf"].to_numpy())
        fit = poly.polyfit(IN_cdf_fitLims["InvSNCDF"].to_numpy()[mask_nan_fitLims], IN_cdf_fitLims["edges"].to_numpy()[mask_nan_fitLims], 1)
    #   do plotting of points and fit line
        colour=next(ax._get_lines.prop_cycler)['color']
        ax.plot(binEdgesToPlot,IN_cdf["InvSNCDF"], label=[var],markersize=1,marker='.',linestyle = 'None',color=colour)
        ax.plot(poly.polyval(xLims,fit),xLims,color=colour)

    ax.set_xlabel(r'strain ($\mu \epsilon$)')  # Add an x-label to the axes.
    ax.set_ylabel('Inverse normal CDF probability (No. of sigma)')  # Add a y-label to axes
    ax.set_title(title)  # Add a title to the axes.
    plt.grid(True)
    ax.autoscale(enable=True, axis='both', tight=True)
    ax.legend(loc=(1.05, 0.5), edgecolor='None', markerscale=1.8)
    plt.tight_layout()
    if plot_or_save=='plot':
        plt.show()
    elif plot_or_save=='save':
        plt.savefig(fname)

