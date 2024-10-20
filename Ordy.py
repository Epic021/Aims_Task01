
def Ordy_encoding(df) : 


# get categorial columns
    cat_cols = []
    for col in df.columns :
        if (df[col].nunique() < 5 and df[col].dtype == "object" ): 
            cat_cols.append(col)

# get list of unique values in each categorial column    
    for i in range(len(cat_cols)) :
        col = cat_cols[i]
        lst = list(df[col].unique())
    
    # create integer list for encoding
        new_lst = [i for i in range(len(lst))]
    
    # Ordinal encoding             
        for i in range(len(lst)) :
            df[col] = df[col].replace(lst[i] ,new_lst[i])
    print(df)