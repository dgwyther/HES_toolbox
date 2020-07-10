def loadDat(filename,timeIndex,columnNames):
    df_out = pd.read_csv(filename, skiprows=3, na_values='NAN')
    df_out.columns=[columnNames]
    df_out=df_out.astype({'TIMESTAMP': 'datetime64'})
    return df_out