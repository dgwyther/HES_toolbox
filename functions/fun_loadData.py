import pandas as pd

def loadData(filename,timeIndex):
    # colNames_out = pd.read_csv(filename,nrows=1,skiprows=1,na_values='NAN').columns.to_list()
    # df_out = pd.read_csv(filename, skiprows=3, na_values='NAN')
    # df_out.columns=colNames_out
    # df_out=df_out.astype({'TIMESTAMP': 'datetime64'})
    # return df_out, colNames_out
    df_out = pd.read_csv(filename,header=1, skiprows=[2,3], na_values='NAN')
    df_out=df_out.astype({'TIMESTAMP': 'datetime64'})
    colNames_out = list(df_out.columns)
    return df_out, colNames_out
