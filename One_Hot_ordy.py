
def OH_encoding(df) :

    # get categorial columns
    cat_cols = []
    for col in df.columns :
        if (df[col].nunique() < 5 and df[col].dtype == "object" ): 
            cat_cols.append(col)

    # get list of unique values in each categorial column    
    for i in range(len(cat_cols)) :
        col = cat_cols[i]
        lst = list(df[col].unique())
        df[lst] = 0



    # One Hot Encoding 
    # iloc was showing a warning so I changed it. 
        for j in range(len(lst)) :
            for k in range(len(df[col])) :
                if lst[j] == df[cat_cols[i]].iloc[k] :
                    # df[lst[j]].iloc[k] = 1 
                    df.loc[df.index[k], lst[j]] = 1

                else :
                    # df[lst[j]].iloc[k] = 0
                    df.loc[df.index[k], lst[j]] = 0


    df.drop(columns = cat_cols , inplace = True)
    print(df)
    
