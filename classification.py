# -*- coding: utf-8 -*-
"""
The class classification implements sophisticated code that enables 
imputation using machine learning, and dimension reduction using 
Principal Component Analysis. 

-- ADVISORY -----
As the dataset the user would be working with is immense,
the functions in this class for imputation (knn_imputation(df)) 
require a lot of memory in RAM and processing
power. Therefore, it is reccomended to only run this function with test data
or with a capable computer 

-- Potential ----
Using knn_imputation(df), users could predict factors like income, 
location, age, etc. of individuals based on patterns and trends 
observed in the dataset.

Using pca_plot(df), users could understand the variance distrabution of 
the data giving an insight into how many dimesions to reduce by without 
compromizing the statistical strength of the data.
"""

#Imputation using Machine Learning

# drop_binary(df) is a function that drops columns with binary data. 
# this is useful when implementing KNN and PCA.
# df sampled dataset, pd.DataFrame
# returns: df, modifed dataset without binary columns

def drop_binary(df):    
    binary = []
    # Getting the indices for columns that are binary
    for i in range(df.shape[1]):
        if (df.iloc[ : , i].isnull().values.any()):
            if (len(df.iloc[ : , i].value_counts()) == 1):
                binary.append(i)
    # Dropping columns indicated in 'binary'
    df.drop(df.columns[binary], axis = 1, inplace = True)
    return df

# knn_imputation(df) uses supervised machine learning to 
# impute missing numeric data. The implemented classification techique 
# the K-Nearest Neighbor
# df sampled dataset, pd.DataFrame
# returns: df, modifed dataset with imputed values

def knn_imputation(df):
    # drops all columns that are not numeric 
    df = df.select_dtypes(exclude=['object']).copy()
    # drops binary columns
    df = drop_binary(df)
    df.head()
    # model for implementing KNN
    imputer = KNNImputer(n_neighbors = int(df.shape[0]**(1/2)))
    df = imputer.fit_transform(df)
    return df


# pca_plot(df) plots the Cumulative Explained Variance of the numeric 
# columns in the data set. This provides the user with insight on how
# many numeric columns in the dataset explain the total variannce of the 
# dataset. This is useful when users intend on using dimension reduction 
# methods like PCA and would like to know how many dimensions to reduce to.
# df: sampled dataset, pd.DataFrame
# displays: a graph depicting the Cumulative explained variance
    
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



# call_classification(data) calls on the functions in this class
# data: sampled dataset, pd.DataFrame
# displays: a graph depicting the Cumulative explained variance
# returns: dataframe with imputed data
def call_classification(data): 
    sampled_data = prelim_numeric_converter(data)

    imputed_data = knn_imputation(sampled_data)

    #Plot Numeric Variables Explain Variance of Entire DataSet
    pca_plot(sampled_data)
    
    return(imputed_data)


