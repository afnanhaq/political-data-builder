# -*- coding: utf-8 -*-
"""
The function save_file is called when a user wants to download a 
file from the website. It uses a GUI that allows users to intuitively 
choose the location and file type of the sampled data. Additionally,
it creates dataframes consisting of aggregated data from the dataframes
passed as arguements.
"""

import pandas as pd
from tkinter import * 
from tkinter import ttk 
# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
from tkinter.filedialog import asksaveasfile 


#Save File as CSV or TAB or ShapeFile 
#TODO Finish this and test does not take in a df to save 
def start(df):
    root = Tk() 
    root.geometry('200x150') 
    root.title("File Explorer")
    save(df)

def save(df): 
    file_to_save = df.to_csv(sep=",")
    files = [('CSV Files', '*.csv'), 
             ('Shape Files', '.shp'), 
             ('TAB Files', '*.tab')] 
    file = asksaveasfile(mode='w', filetypes = files, defaultextension = ".csv") 
    #file_to_save.to_csv(file)

    btn = ttk.Button(root, text = 'Save', command = lambda : save()) 
    btn.pack(side = TOP, pady = 20) 

 

# merged_agg(df) reads voter information and returns aggregated 
# information on historical voting performance for each party
# df: merged dataset, should be a pandas DataFrame
# returns data, pd.DataFrame

def merged_agg(df):
    try:
        criteria = [df['VotingPerformanceEvenYearGeneral'].between(0, 25), 
                df['VotingPerformanceEvenYearGeneral'].between(26, 50), 
                df['VotingPerformanceEvenYearGeneral'].between(51, 75), 
                df['VotingPerformanceEvenYearGeneral'].between(76, 101)]
        values = ['Poor', 'Below_Average', 'Above_average', 'Excellent']

        df['general_voting_performance'] = np.select(criteria, values, "Unknown")        
        data = pd.crosstab(index=df['Parties_Description'], columns=df['general_voting_performance'], values=df['counter'], aggfunc='sum')
        return data
    except:
        print("Sorry, not Enough Information for a Voting History Breakdown")



# demographic_agg(df) reads voter information and returns aggregated 
# demographic information for each party
# df: demographic/merged dataset, should be a pandas DataFrame
# returns data, pd.DataFrame
        
def demographic_agg(df):
    try:
        df['counter'] = 1
        data = pd.crosstab(index=df['Parties_Description'], columns=[df['EthnicGroups_EthnicGroup1Desc'],df['Voters_Gender']], values=df['counter'], aggfunc='sum')
        return data
    except:
        print("Sorry, not Enough Information for a Demographic Breakdown")

#TODO Delete this main below, only used for testing purposes
def main():
    data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
    # Create the pandas DataFrame 
    df = pd.DataFrame(data, columns = ['Name', 'Age'])
    start(df)

main()