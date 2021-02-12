

#Imputation using Machine Learning


def drop_binary(df):    
    binary = []
    # Getting the indices for columns that are binary
    for i in range(df.shape[1]):
        if (df.iloc[ : , i].isnull().values.any()):
            if (len(df.iloc[ : , i].value_counts()) == 1):
                binary.append(i)
    df.drop(df.columns[binary], axis = 1, inplace = True)
    return df


# run after dropping personal data and threshold
def knn_imputation(df):
    df = df.select_dtypes(exclude=['object']).copy()
    df = drop_binary(df)
    df.head()
    imputer = KNNImputer(n_neighbors = int((df.shape[0]**(1/2))/2))
    df = imputer.fit_transform(df)
    return df


# Plotting the cumulative explained variance to determine the required covariates
def pca_plot(df):
    df = df.select_dtypes(exclude=['object']).copy()
    df = drop_binary(df)
    df.fillna(0, inplace=True)
    pca = PCA().fit(df)
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('number of components')
    plt.ylabel('cumulative explained variance')
    plt.xlim([0, 25])
    plt.grid()
    plt.grid(which='minor', alpha=0.2)
    plt.grid(which='major', alpha=0.7)
    plt.minorticks_on()
    plt.title("Cumulative explained variance vs. Number of Covariates")
    plt.show()



# Must pass in sampled data 
def call_classification(data): 
    sampled_data = prelim_numeric_converter(data)

    imputed_data = knn_imputation(sampled_data)

    #Plot Numeric Variables Explain Variance of Entire DataSet
    pca_plot(sampled_data)


