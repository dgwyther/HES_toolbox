import dash
import dash_core_components as dcc
import dash_html_components as html
import os
import time
import datetime
import numpy as np

from scipy import stats
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objects as go
import plotly

#own functions
from functions.fun_removeDates import removeDates
from functions.fun_loadData import loadData
from functions.fun_applyAliasTable import applyAliasTable
import functions.fun_generateTimeSeriesPlots 

# Load defaults, externals and datasets
coloursDef = plotly.colors.DEFAULT_PLOTLY_COLORS

# Load external stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Load external datasets
SS_filename = '../dash/GAF/Data/HE605_RV50_GAF_SensorStats.dat'
colNamesSS = ["TIMESTAMP","RECORD","BattV_Min","BattV_Avg","PTemp_C_Avg","SensorRel_Min(1)","SensorRel_Min(2)","SensorRel_Min(3)","SensorRel_Min(4)","SensorRel_Min(5)","SensorRel_Max(1)","SensorRel_Max(2)","SensorRel_Max(3)","SensorRel_Max(4)","SensorRel_Max(5)"]
SRES_filename = '../dash/GAF/Data/HE605_RV50_GAF_SensorRelEventStats.dat'
colNamesSRES = ["TIMESTAMP","RECORD","SensorRelEventMin(1)","SensorRelEventMin(2)","SensorRelEventMin(3)","SensorRelEventMin(4)","SensorRelEventMin(5)","SensorRelEventMax(1)","SensorRelEventMax(2)","SensorRelEventMax(3)","SensorRelEventMax(4)","SensorRelEventMax(5)","SensorRelEventPkp(1)","SensorRelEventPkp(2)","SensorRelEventPkp(3)","SensorRelEventPkp(4)","SensorRelEventPkp(5)","SensorWfmTrigSensor","SensorOffset(1)","SensorOffset(2)","SensorOffset(3)","SensorOffset(4)","SensorOffset(5)"]

df_SS = loadData(SS_filename,"TIMESTAMP",colNamesSS)
df_SRES = loadData(SRES_filename,"TIMESTAMP",colNamesSRES)

# Remove bad data by setting snipping lengths (by time)
snipStart = ['2019-08-30 00:27:33',
			'2019-08-30 00:42:28.560',
			'2020-04-06 04:53:58.000']
snipEnd = ['2019-08-30 00:35:36.760',
			'2019-08-30 00:52:15.740',
			'2020-04-06 05:00:42.080']

removeDates(df_SRES,"TIMESTAMP",snipStart,snipEnd)
removeDates(df_SS,"TIMESTAMP",snipStart,snipEnd)

# Use alias table to change names
aliasTable_SRES = {
    "TIMESTAMP":"time",
    "RECORD":"record",
    "SensorRelEventMin(1)":"S_P2_CH_L_HJCrack_Min",
    "SensorRelEventMin(2)":"S_P2_CH_R_HJCrack_Min",
    "SensorRelEventMin(3)":"S_S2_G1_Min",
    "SensorRelEventMin(4)":"S_S2_G2_Min",
    "SensorRelEventMin(5)":"S_S2_G3_Min",
    "SensorRelEventMax(1)":"S_P2_CH_L_HJCrack_Max",
    "SensorRelEventMax(2)":"S_P2_CH_R_HJCrack_Max",
    "SensorRelEventMax(3)":"S_S2_G1_Max",
    "SensorRelEventMax(4)":"S_S2_G2_Max",
    "SensorRelEventMax(5)":"S_S2_G3_Max",
    "SensorRelEventPkp(1)":"S_P2_CH_L_HJCrack_Pkp",
    "SensorRelEventPkp(2)":"S_P2_CH_R_HJCrack_Pkp",
    "SensorRelEventPkp(3)":"S_S2_G1_Pkp",
    "SensorRelEventPkp(4)":"S_S2_G2_Pkp",
    "SensorRelEventPkp(5)":"S_S2_G3_Pkp",
    "SensorWfmTrigSensor":"Sensor Waveform Trigger",
    "SensorOffset(1)":"S_P2_CH_L_HJCrack_Offset",
    "SensorOffset(2)":"S_P2_CH_R_HJCrack_Offset",
    "SensorOffset(3)":"S_S2_G1_Offset",
    "SensorOffset(4)":"S_S2_G2_Offset",
    "SensorOffset(5)":"S_S2_G3_Offset"
}

applyAliasTable(df_SRES,aliasTable_SRES)

# define dropdown and plotting options
opts=[{'label': k, 'value': k} for k in list(df_SS.columns.values)[1:]]
opts_SRES=[{'label': k, 'value': k} for k in list(df_SRES.columns.values)[1:]]
opts_SRES_InvNorm=['SensorRelEventMax(1)','SensorRelEventMax(2)','SensorRelEventMax(3)','SensorRelEventMax(4)','SensorRelEventMax(5)']
default_SenRelMax=['SensorRel_Max(1)','SensorRel_Max(2)','SensorRel_Max(3)','SensorRel_Max(4)','SensorRel_Max(5)'];
default_SenRelPkp=['SensorRel_Pkp(1)','SensorRel_Max(2)','SensorRel_Max(3)','SensorRel_Max(4)','SensorRel_Max(5)'];

# Settings for plots
InvNormBinStart=0
InvNormBinEnd=200
InvNormBinInc=2
InvNormMin = 1
InvNormMax = 2.75

# generate tables
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# Last Week stats
start_date = pd.to_datetime(df_SRES['TIMESTAMP'].max())-datetime.timedelta(days=7)
end_date = pd.to_datetime(df_SRES['TIMESTAMP'].max())
mask = (df_SRES['TIMESTAMP'] > start_date) & (df_SRES['TIMESTAMP'] <= end_date)
df_SRES_stats_LastWeekFull = df_SRES.loc[mask]

SRES_stats_overview = {
                'Date start': [df_SRES['TIMESTAMP'].min().strftime("%d-%m-%y %H:%M"),df_SRES_stats_LastWeekFull['TIMESTAMP'].min().strftime("%d-%m-%y %H:%M")],
                'Date end': [df_SRES['TIMESTAMP'].max().strftime("%d-%m-%y %H:%M"),df_SRES_stats_LastWeekFull['TIMESTAMP'].max().strftime("%d-%m-%y %H:%M")],
                '# of Rel Events': [df_SRES.shape[0],df_SRES_stats_LastWeekFull.shape[0]],
                'Events/day': [round(df_SRES.shape[0]/pd.to_numeric(datetime.timedelta.total_seconds(df_SRES["TIMESTAMP"].max()-df_SRES["TIMESTAMP"].min()) / (3600*24)),1),round(df_SRES_stats_LastWeekFull.shape[0]/pd.to_numeric(datetime.timedelta.total_seconds(df_SRES_stats_LastWeekFull["TIMESTAMP"].max()-df_SRES_stats_LastWeekFull["TIMESTAMP"].min()) / (3600*24)),1)],
                'Sensor(1) Max': [round(df_SRES['SensorRelEventMax(1)'].max(),1),round(df_SRES_stats_LastWeekFull['SensorRelEventMax(1)'].max(),1)],
                'Sensor(2) Max': [round(df_SRES['SensorRelEventMax(2)'].max(),1),round(df_SRES_stats_LastWeekFull['SensorRelEventMax(2)'].max(),1)],
                'Sensor(3) Max': [round(df_SRES['SensorRelEventMax(3)'].max(),1),round(df_SRES_stats_LastWeekFull['SensorRelEventMax(3)'].max(),1)],
                'Sensor(4) Max': [round(df_SRES['SensorRelEventMax(4)'].max(),1),round(df_SRES_stats_LastWeekFull['SensorRelEventMax(4)'].max(),1)],
                'Sensor(5) Max': [round(df_SRES['SensorRelEventMax(5)'].max(),1),round(df_SRES_stats_LastWeekFull['SensorRelEventMax(5)'].max(),1)]
                }

df_SRES_stats_overview = pd.DataFrame(SRES_stats_overview).T.reset_index()
df_SRES_stats_overview.columns={'','All Time','Last Two Weeks'}
df_SRES_stats_overview.index={'Date start','Date end','# of Rel Events','Events/day','Sensor(1) Max','Sensor(2) Max','Sensor(3) Max','Sensor(4) Max','Sensor(5) Max'}

                                        
# all time top 20
SRES_stats_Top20= df_SRES.nlargest(40,['SensorRelEventPkp(1)','SensorRelEventPkp(2)','SensorRelEventPkp(3)','SensorRelEventPkp(4)','SensorRelEventPkp(5)'])

SRES_stats_Top20.drop(columns=["RECORD","SensorRelEventMin(1)","SensorRelEventMin(2)","SensorRelEventMin(3)","SensorRelEventMin(4)","SensorRelEventMin(5)","SensorRelEventMax(1)","SensorRelEventMax(2)","SensorRelEventMax(3)","SensorRelEventMax(4)","SensorRelEventMax(5)","SensorWfmTrigSensor","SensorOffset(1)","SensorOffset(2)","SensorOffset(3)","SensorOffset(4)","SensorOffset(5)"],inplace=True)


SRES_stats_Top20_form = {
                        'TIMESTAMP': SRES_stats_Top20["TIMESTAMP"].dt.strftime("%d-%m-%y %H:%M"),
                        'SensorRelEventPkp(1)': round(SRES_stats_Top20["SensorRelEventPkp(1)"],1),
                        'SensorRelEventPkp(2)': round(SRES_stats_Top20["SensorRelEventPkp(2)"],1),
                        'SensorRelEventPkp(3)': round(SRES_stats_Top20["SensorRelEventPkp(3)"],1),
                        'SensorRelEventPkp(4)': round(SRES_stats_Top20["SensorRelEventPkp(4)"],1),
                        'SensorRelEventPkp(5)': round(SRES_stats_Top20["SensorRelEventPkp(5)"],1)
                        }

df_SRES_stats_Top20=pd.DataFrame(SRES_stats_Top20_form,columns=["TIMESTAMP","SensorRelEventPkp(1)","SensorRelEventPkp(2)","SensorRelEventPkp(3)","SensorRelEventPkp(4)","SensorRelEventPkp(5)"])

#highlight
def highlight_inInterval(s, threshold_s,threshold_e, column):
    mask = (s[column] > threshold_s) & (s[column] <= threshold_e)
    return ['background-color: yellow' if mask.any() else '' for v in mask]

df_SRES_stats_Top20.style.apply(highlight_inInterval, threshold_s='2019-09-28',threshold_e='2019-09-29', column='TIMESTAMP', axis=1)


## generate figures
trace_initialPlot = go.Scatter(x=df_SS['TIMESTAMP'], y=df_SS['SensorRel_Min(1)'],name='SensorRel_Min(1)')
#fig_finalPlot = go.Scatter(x=df_SS['TIMESTAMP'], y=df_SS['SensorRel_Max(1)'],name='SensorRel_Max(1)')
layout_initialPlot = go.Layout(
#                        title = 'Max bending strains since commencement of monitoring',
                        hovermode = 'closest',
                        xaxis={'title': 'time/date'},
                        yaxis={'title': "&#956;&#949;"},
                        margin={'l': 40, 'b': 40, 't': 30, 'r': 10},
                        legend_orientation="v",
                        font=dict(
                        size=18))
layout_initialPlotZoom = go.Layout(
#                        title = 'Max bending strains in the past two weeks',
                        hovermode = 'closest',
                        xaxis=dict({'title': 'time/date'}, range=[pd.to_datetime(df_SS['TIMESTAMP'].max())-datetime.timedelta(days=14), pd.to_datetime(df_SS['TIMESTAMP'].max())]),
                        yaxis=dict(title="&#956;&#949;"),
                        margin={'l': 40, 'b': 40, 't': 30, 'r': 10},
                        legend_orientation="v",
                        font=dict(
                        size=18))
# make sensor rel event stat plots
## First SRES plot
trace_SRES_Sensor1=go.Scatter(x=df_SRES['TIMESTAMP'],
                                y=df_SRES['SensorRelEventMin(1)'],
                                name='SensorRelEvent_Min(1)')

layout_SRES_Sensor1 = go.Layout(
#                        title = 'Sensor(1) Rel Event Min/Max',
                        hovermode = 'closest',
                        xaxis={'title': 'time/date'},
                        yaxis={'title': "&#956;&#949;"},
                        margin={'l': 40, 'b': 40, 't': 30, 'r': 10}
)
fig_SRES1=go.Figure(data=[trace_SRES_Sensor1], layout=layout_SRES_Sensor1)
fig_SRES1.add_trace(go.Scatter(x=df_SRES['TIMESTAMP'],
                                y=df_SRES['SensorRelEventMax(1)'],
                                name='SensorRelEvent_Max(1)')
)
fig_SRES1.update_layout(legend_orientation="h")

## Second SRES plot
trace_SRES_Sensor2=go.Scatter(x=df_SRES['TIMESTAMP'],
                                y=df_SRES['SensorRelEventMax(1)'],
                                name='SensorRelEvent_Max(1)')

layout_SRES_Sensor2 = go.Layout(title = 'Sensor Rel Event Maxes',
                        hovermode = 'closest',
                        xaxis={'title': 'time/date'},
                        yaxis={'title': "&#956;&#949;"},
                        margin={'l': 40, 'b': 40, 't': 30, 'r': 10}
)
fig_SRES2=go.Figure(data=[trace_SRES_Sensor2], layout=layout_SRES_Sensor2)
fig_SRES2.add_trace(go.Scatter(x=df_SRES['TIMESTAMP'],
                                y=df_SRES['SensorRelEventMax(2)'],
                                name='SensorRelEvent_Max(2)')
)                 
fig_SRES2.add_trace(go.Scatter(x=df_SRES['TIMESTAMP'],
                                y=df_SRES['SensorRelEventMax(3)'],
                                name='SensorRelEvent_Max(3)')
)
fig_SRES2.add_trace(go.Scatter(x=df_SRES['TIMESTAMP'],
                                y=df_SRES['SensorRelEventMax(4)'],
                                name='SensorRelEvent_Max(4)')
)
fig_SRES2.add_trace(go.Scatter(x=df_SRES['TIMESTAMP'],
                                y=df_SRES['SensorRelEventMax(5)'],
                                name='SensorRelEvent_Max(5)')
) 
fig_SRES2.update_layout(legend_orientation="h")

## Third SRES plot - histogram of max values for sensor(1)
fig_SRES_hist1 = go.Figure()
fig_SRES_hist1.add_trace(go.Histogram(x=df_SRES['SensorRelEventMax(1)'],
                                        name='SensorRelEventMax(1)',
                                        nbinsx=30))
fig_SRES_hist1.add_trace(go.Histogram(x=df_SRES['SensorRelEventMax(2)'],
                                        name='SensorRelEventMax(2)',
                                        nbinsx=30))
fig_SRES_hist1.add_trace(go.Histogram(x=df_SRES['SensorRelEventMax(3)'],
                                        name='SensorRelEventMax(3)',
                                        nbinsx=30))
fig_SRES_hist1.add_trace(go.Histogram(x=df_SRES['SensorRelEventMax(4)'],
                                        name='SensorRelEventMax(4)',
                                        nbinsx=30))
fig_SRES_hist1.add_trace(go.Histogram(x=df_SRES['SensorRelEventMax(5)'],
                                        name='SensorRelEventMax(5)',
                                        nbinsx=30))                                        
fig_SRES_hist1.update_layout(
#    title_text='Histogram of max events at Sensors 1-5', # title of plot
    xaxis_title_text="&#956;&#949;", # xaxis label
    yaxis_title_text='Count', # yaxis label
    yaxis_type="log",
    barmode='group',
    legend_orientation="v",
    margin={'l': 40, 'b': 40, 't': 30, 'r': 10},
    font=dict(size=18)
    )
fig_SRES_hist1.update_traces(opacity=0.75)

## Inverse normal plot

Events_per_day = df_SRES["SensorRelEventMax(1)"].count()/pd.to_numeric(datetime.timedelta.total_seconds(df_SRES["TIMESTAMP"].max()-df_SRES["TIMESTAMP"].min()) / (3600*24))
ET_ARI1day = -stats.norm.ppf(1/Events_per_day)
ET_95in1day = -stats.norm.ppf(1/(20*Events_per_day+1))
ET_95in1year = -stats.norm.ppf(1/(20*365*Events_per_day+1))
ET_95in100year = -stats.norm.ppf(1/(20*100*365*Events_per_day+1))

data_InvNorm1 = []
loop_ind = -1
for var in opts_SRES_InvNorm:
    loop_ind=loop_ind+1
    IN_inputData = df_SRES[var]
    IN_binned,IN_edges = np.histogram(IN_inputData,np.arange(InvNormBinStart,InvNormBinEnd+InvNormBinInc,InvNormBinInc))
    bin_edges_plot = IN_edges[1:] # shift bin edge to the upper edge for plotting
    IN_cdf = pd.DataFrame({"cdf": IN_binned.cumsum()})
    IN_cdf["edges"] = bin_edges_plot #add new column
    IN_cdf.mask((IN_cdf == IN_cdf.shift(1)) | (IN_cdf == 0), inplace=True)
    idx = np.isfinite(IN_cdf["cdf"].to_numpy()) # make mask for NaN values
    with np.errstate(invalid='ignore'):
        IN_cdf["InvSNCDF"] = pd.DataFrame(stats.norm.ppf(IN_cdf["cdf"]/(IN_inputData.count()+1))) # and mask by idx to remove NaNs
    x_lims =np.array([0,ET_95in100year])
    IN_cdf_fitLims = IN_cdf[(IN_cdf["InvSNCDF"] >= InvNormMin) & (IN_cdf["InvSNCDF"] <= InvNormMax)]
    mask_nan_fitLims = np.isfinite(IN_cdf_fitLims["cdf"].to_numpy())
    fit = np.polyfit(IN_cdf_fitLims["InvSNCDF"].to_numpy()[mask_nan_fitLims], IN_cdf_fitLims["edges"].to_numpy()[mask_nan_fitLims], 1) #np.polyfit(IN_cdf["InvSNCDF"].to_numpy()[idx], bin_edges_plot[idx], 1)
    pts_InvNorm1 = go.Scatter(y=IN_cdf["InvSNCDF"],
                    x=bin_edges_plot, 
                    mode = 'markers',
                    marker=dict(color=coloursDef[loop_ind]),
                    showlegend=True,
                    name=var
                    )
    line_InvNorm1 = go.Scatter(y=x_lims,
                    x=fit[1]+fit[0]*x_lims, 
                    mode = 'lines',
                    line=dict(width=1, color=coloursDef[loop_ind], dash='dash'),
                    showlegend=True,
                    name=var+'_fit'
                    )
    data_InvNorm1.append(pts_InvNorm1)
    data_InvNorm1.append(line_InvNorm1)

layout_InvNorm1 = go.Layout(title = 'InvSNCDF vs binned strain',
                        hovermode = 'closest',
                        xaxis={'title': 'strain (&#956;&#949;)','range':[0,200]},
                        yaxis={'title': "Inverse normal CDF probabilities vs. binned strain"},
                        margin={'l': 240, 'b': 40, 't': 30, 'r': 210}
)
data_InvNorm1.append(go.Scatter(x=[0,250], 
                        y=[ET_ARI1day, ET_ARI1day],
                        mode="lines",                            
                        name="ARI = 1 day",
                        line=dict(width=2, color='dodgerblue'),
                        marker=dict(size=2)
))
data_InvNorm1.append(go.Scatter(x=[0,250], 
                        y=[ET_95in1day, ET_95in1day],
                        mode="lines",                            
                        name="95% in 1 day",
                        line=dict(width=2, color='goldenrod'),
                        marker=dict(size=2)
))
data_InvNorm1.append(go.Scatter(x=[0,250], 
                        y=[ET_95in1year, ET_95in1year],
                        mode="lines",                            
                        name="95% in 1 year",
                        line=dict(width=2, color='firebrick'),
                        marker=dict(size=2)
))
data_InvNorm1.append(go.Scatter(x=[0,250], 
                        y=[ET_95in100year, ET_95in100year],
                        mode="lines",                            
                        name="95% in 100 years",
                        line=dict(width=2, color='forestgreen'),
                        marker=dict(size=2)
))
fig_InvNorm1 = go.Figure(data=data_InvNorm1, layout=layout_InvNorm1)

## start dash

app.layout = html.Div(children=[
            html.H3(children='Gateway Arterial Flyover - Bridge monitoring update',style={'textAlign': 'center'}),
            html.Br(),

        #    html.H2(children=SRES_filename),
        #    html.H4(['Page loaded at ',datetime.datetime.now().strftime('%Y-%m-%d'),'  ',datetime.datetime.now().strftime('%H:%M:%S')]),
            html.H6(children=['Monitoring statistics for data captured on Span 2 and Pier 2 of the Gateway Arterial Flyover, the week ending ',time.strftime("%Y-%m-%d",time.localtime(os.path.getmtime(SS_filename)))],style={'textAlign': 'center'}),
            html.Hr(),
            
            
            html.H4('Monitoring summary'),
            html.H6(['The following statistics show summaries of data captured over the period ',df_SRES["TIMESTAMP"].min().strftime("%d %B %Y"),' to ',df_SRES["TIMESTAMP"].max().strftime("%d %B %Y"),'.']),
            html.Br(),
            generate_table(df_SRES_stats_overview),
            html.Br(),
            html.H6(['The following histogram shows aggregated data maximums captured at each sensor for the period ',df_SRES["TIMESTAMP"].min().strftime("%d %B %Y"),' to ',df_SRES["TIMESTAMP"].max().strftime("%d %B %Y"),'.']),           
            dcc.Graph(
            id='plot_SRES_hist1',
            figure=fig_SRES_hist1
            ),
            html.Br(),
            html.Br(),
   
            html.H4('Maximum mid-span bending strains'),
            html.H6(['The maximum bending strains measured mid-span for the whole monitoring period and last two weeks (pink highlight).']),
            
            dcc.Graph(
            id='plot1',
            ),
            dcc.Dropdown(
            id='multiVariableDropdown',
            options=opts,
            value=default_SenRelMax,
            multi=True,
            style = {'display':'inline-block'}
            ),       
            dcc.Graph(
            id='plot2'
            ), 
            dcc.Dropdown(
            id='multiVariableDropdown2',
            options=opts,
            value=default_SenRelMax,
            multi=True
            ),
            html.Br(),
            
            html.H4('Largest events'),    
            html.H6('Statistics for the top 20 maximum girder bending strains are shown below.'),
            html.Br(),
            generate_table(df_SRES_stats_Top20),
            html.Br(),

            html.H4('Comparison to a standard normal distribution'),    
            html.H6('Binned data for each sensor is compared to the standard normal distribution'),     
            dcc.Graph(
            id='plot_InvNorm1',
            figure=fig_InvNorm1
            )         
        ]

)



# Add callback functions
## For long-timescale time series plot
@app.callback(Output('plot1', 'figure'),
             [Input('multiVariableDropdown', 'value')])
def update_graph(selectedVariable):
    traces = []
    for var in selectedVariable:
        traces.append(go.Scatter(x=df_SS['TIMESTAMP'], 
                            y=df_SS[var],
                            mode="lines",
                            name=var,
                            marker=dict(size=2)
            ))
        fig1 = go.Figure(data=traces, layout=layout_initialPlot)
# Add shape regions
        fig1.update_layout(
            shapes=[
                # 1st highlight during Feb 4 - Feb 6
                dict(
                    type="rect",
                    # x-reference is assigned to the x-values
                    xref="x",
                    # y-reference is assigned to the plot paper [0,1]
                    yref="paper",
                    x0=pd.to_datetime(df_SS['TIMESTAMP'].max())-datetime.timedelta(days=14),
                    y0=0,
                    x1=pd.to_datetime(df_SS['TIMESTAMP'].max()),
                    y1=1,
                    fillcolor="LightSalmon",
                    opacity=0.5,
                    layer="below",
                    line_width=0,
                )

            ]
        )
    return fig1
    
## For short-timescale time series plot
@app.callback(Output('plot2', 'figure'),
             [Input('multiVariableDropdown2', 'value')])
def update_figure(selectedVariable2):
    traces = []
    for var in selectedVariable2:
        traces.append(go.Scatter(x=df_SS['TIMESTAMP'], 
                            y=df_SS[var],
                            mode="lines",
                            name=var,
                            marker=dict(size=2)
            ))
        fig2 = go.Figure(data=traces, layout=layout_initialPlotZoom)
    return fig2


if __name__ == '__main__':
    app.run_server(debug=True)

