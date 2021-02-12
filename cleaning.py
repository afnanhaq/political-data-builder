

# Function converts the obvious numeric columns into int/float
def prelim_numeric_converter(df):
    df.loc[:, df.columns.str.startswith('VotingPerformance')] = df.loc[:, df.columns.str.startswith('VotingPerformance')].replace(["%"], "", regex=True)
    df.loc[:, df.columns.str.startswith('Commercial')] = df.loc[:, df.columns.str.startswith('Commercial')].replace(["$"], "", regex=True)
    cols = df.columns
    for c in cols:
        try:
            df[c] = pd.to_numeric(df[c])
        except:
            pass
    return df



# converting election results to numeric (resource heavy)
def election_numeric_converter(df):
    col_len = df.shape[1]-1
    df.loc[:, df.columns.str.startswith('Election')] = df.loc[:, df.columns.str.startswith('Election')].replace(["%"], "", regex=True)
    for i in range(df.loc[:, df.columns.str.startswith('Election')].shape[1]):
        try:
            df.iloc[:, col_len-i] = pd.to_numeric(df.iloc[:, col_len-i])
        except:
            pass
    return df