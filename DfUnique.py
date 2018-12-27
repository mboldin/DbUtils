def DfUnique(df,v, sort=True, output='list'):
    """Make list or set of unique values for a column in dataframe 
         df -- pandas dataframe
         v -- variable column name (string) or list/tuple of names
         sort = True, sort results, as list or series
         output = list, dataframe series or set
    """  
    s = None
    if isinstance(v,str):
        if v in df.columns:
            s = df[v]
            s = set(s)
        elif v == df.index.name :
            s = getdf.index
            s = set(s)
        elif v in df.index.names :
            s =  df1a.index.get_level_values(v)
            s = set(s)
        else:
            print('Can not find %s in dataframe columns or index' % v )
    elif isinstance(v,(tuple,list)):
        s = df.loc[:,v]
        s = d.drop_duplicates().values.tolist()
    else:
        print('Can not use  %s to select from dataframe' % v )
    
    if s:
        if output == 'set':
            pass
        elif output == 'list':
            s = list(s)
            if sort:
                s.sort()
        elif output == 'dataframe':
            s = pd.DataFrame(list(s),columns = [v,])
            if sort:
                s.sort_values(v, inplace=True)
    return s
