
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from zipfile import ZipFile 
import sys


import os
#import janitor

#Files to include 
from remove import remove_null, drop_private
from cleaning import *
from jittering import *
from classification import *
from visualization import *
from save_file import *

#Global Variables
#keys: State_typeOfFile        Item: DataFrame
place_dic = {}


def zip_extractor(place):
    # if there's an error, try \ instead of /
    file_name = "//storage.rcs.nyu.edu/L2_Political/03-01-2020-delivery/files-by-state/"+ place + ".zip"
    #file_name = "\\storage.rcs.nyu.edu\L2_Political\03-01-2020-delivery\files-by-state" + place + ".zip"
    # opening the zip file in READ mode 
    zip = ZipFile(file_name,'r') 

    demographics_file = zip.open(place + "-DEMOGRAPHIC.tab")
    vote_history_file = zip.open(place + "-VOTEHISTORY.tab")
    zip.close()
    demographics = pd.read_csv(demographics_file, 
                                sep='\t', dtype=str, encoding='unicode_escape',
                               nrows=10)
    vote_history = pd.read_csv(vote_history_file, 
                                sep='\t', dtype=str, encoding='unicode_escape',
                                nrows=10)

    return demographics, vote_history


#Iterates through all of the files by state and unzips 
def create_df(): 
    for file in os.listdir('//storage.rcs.nyu.edu/L2_Political/03-01-2020-delivery/files-by-state/'):
    #for file in os.listdir('\\storage.rcs.nyu.edu\L2_Political\03-01-2020-delivery\files-by-state'):
        rename = file[file.find("--")+2:file.find("-2")-1]

        place = file[:file.find(".zip")]
        demographics, vote_history = zip_extractor(place)

        place_dic["%s_demographic" %rename] = demographics
        place_dic["%s_voting_history" %rename] = vote_history

def get_state_keys(): 
    return place_dic.keys()


def get_sample(df, sample_size):
    return df.sample(frac=sample_size)


def merge(state_demographic, state_vote_history):
    merged_file = pd.merge(state_vote_history, state_demographic,
                       how='left', left_on='LALVOTERID', right_on='LALVOTERID')
    
    return merged_file


def main(): 
    #create global place_dic 
    global place_dic
    #EXTRACTING ZIPS 
        #creating DataFrames
    create_df()
    state_file_keys = get_state_keys()
    print("--- State File Keys ---")
    print(state_file_keys)
    print("----------------------")

    #Removing Nulls and Private Information 
    place_dic = remove_null(place_dic)

    #TODO drop only for demographic
    #place_dic = drop_private(place_dic)

    #TODO National or StateWise 
    #If National: 
    #else: TODO replace filename 
    df = place_dic["AK_demographic"]

    #TODO if demographic then jitter  -> National as well 

    #Sampling 
    #sample_state _____ TODO 
    df = get_sample(df, .10)

    #TODO if merge 
    #merged_df = merge(state_demographic, state_vote_history)
            #TODO if merge with demographic then jitter 


    #CLEANING 
    #creating numeric columns
    df = prelim_numeric_converter(df) 
    
    #Link for ArcGIS Data Visualization 
    link = visualization(df)
    print(link)
    if sys.platform=='win32':
        os.startfile(link)
    elif sys.platform=='darwin':
        subprocess.Popen(['open', link])
    else:
        try:
            subprocess.Popen(['xdg-open', link])
        except OSError:
            print('Please open a browser on: '+ link)


    #TODO only for demographic 
    # converting election results to numeric (resource heavy)
    #df = election_numeric_converter()



    """
    Requires better processing 
    Requirements: 
        - Sampled
        - Heavy Processer 
        - Lot of Ram
    Potential: 
        - Prediction of Voting Patterns 
        - Political Campaigning 
        - Predictions of income level, status, zip code, etc

    Description
        -  TODO 
    """
    #Imputation using Machine Learning
    #call_classification(df)

    #PCA 
    #TODO if time 

    #Saving Resulting DataFrame to CSV
    #TODO pass in the df to save in save_file.py
    start()
    #stripped_sample.to_csv(r'virginia-onepercent-sample.csv', index=False, encoding='utf-8')
    

main() 