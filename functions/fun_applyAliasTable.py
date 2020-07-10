def applyAliasTable(inputData,aliasTableName):
    inputData.rename(columns=aliasTableName, inplace=True) # apply rename function over df 