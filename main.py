import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from zipfile import ZipFile 
import sys


import os
import janitor


#Files to include 
from remove import remove_null, drop_private
from cleaning import *
from jittering import *
from classification import *
from visualization import *
#from save_file import *

#Global Variables
#keys: State_typeOfFile        Item: DataFrame
place_dic = {}

states_dict = {
    "Alaska" : "VM2--AK--2020-03-18",
    "Alabama" : "VM2--AL--2020-02-24",
    "Arkansas" : "VM2--AR--2020-02-24",
    "Arizona": "VM2--AZ--2020-02-19", 
    "California": "VM2--CA--2020-03-25", 
    "Colorado": "VM2--CO--2020-02-26",
    "Connecticut": "VM2--CT--2020-03-26",
    "DC": "VM2--DC--2020-03-02",
    "Delaware": "VM2--DE--2020-03-30",
    "Florida": "VM2--FL--2020-07-30",
    "Georgia": "VM2--GA--2020-03-02",
    "Hawaii": "VM2--HI--2020-03-02",
    "Iowa": "VM2--IA--2020-03-03",
    "Idaho": "VM2--ID--2020-03-27",
    "Illinois": "VM2--IL--2020-03-03",
    "Indiana": "VM2--IN--2020-02-27",
    "Kansas": "VM2--KS--2020-03-18",
    "Kentucky": "VM2--KY--2020-02-26",
    "Louisiana": "VM2--LA--2020-02-27",
    "Massachusetts": "VM2--MA--2020-02-19",
    "Maryland": "VM2--MD--2020-02-28",
    "Maine": "VM2--ME--2020-02-24",
    "Michigan": "VM2--MI--2020-03-02",
    "Minnesota": "VM2--MN--2020-02-25",
    "Missouri": "VM2--MO--2020-03-05",
    "Mississippi": "VM2--MS--2020-03-20",
    "Montana": "VM2--MT--2020-03-14",
    "North Carolina": "VM2--NC--2020-02-29",
    "North Dakota": "VM2--ND--2020-02-28",
    "Nebraska": "VM2--NE--2020-03-18",
    "North Hampshire": "VM2--NH--2020-03-03",
    "New Jersey": "VM2--NJ--2020-02-26",
    "New Mexico": "VM2--NM--2020-02-24",
    "Nevada": "VM2--NV--2020-02-22",
    "New York": "VM2--NY--2020-03-05",
    "Ohio": "VM2--OH--2020-02-28",
    "Oklahoma": "VM2--OK--2020-02-25",
    "Oregon": "VM2--OR--2020-02-25",
    "Philadelphia": "VM2--PA--2020-03-20",
    "Rhode Island": "VM2--RI--2020-02-28",
    "South Carolina": "VM2--SC--2020-02-21",
    "South Dakota": "VM2--SD--2020-02-25",
    "Tennessee": "VM2--TN--2020-03-31",
    "Texas": "VM2--TX--2020-03-02",
    "Utah": "VM2--UT--2020-04-07",
    "Virginia": "VM2--VA--2020-03-01",
    "Vermont": "VM2--VT--2020-02-27",
    "Washington": "VM2--WA--2020-04-20",
    "Wisconsin": "VM2--WI--2020-03-21",
    "West Virginia": "VM2--WV--2020-03-29",
    "Wyoming": "VM2--WY--2020-03-02"
}

def zip_extractor(place):
    """
    Unzips the files and 
    Input: [str] : The folder location to unzip
    Return: [dataframe] : The demographics and vote_history pandas dataframes to store in the place_dic
    """
    file_name = "//storage.rcs.nyu.edu/L2_Political/03-01-2020-delivery/files-by-state/"+ place + ".zip"
    #depending on OS 
    #file_name = "\\storage.rcs.nyu.edu\L2_Political\03-01-2020-delivery\files-by-state" + place + ".zip"
    # opening the zip file in READ mode 
    zip = ZipFile(file_name,'r') 

    demographics_file = zip.open(place + "-DEMOGRAPHIC.tab")
    vote_history_file = zip.open(place + "-VOTEHISTORY.tab")
    zip.close()
    print("---------- Extracting Data File -----------")
    demographics = pd.read_csv(demographics_file, 
                                sep='\t', dtype=str, encoding='unicode_escape',
                               nrows=10000)
    vote_history = pd.read_csv(vote_history_file, 
                                sep='\t', dtype=str, encoding='unicode_escape',
                                nrows=10000)
    return demographics, vote_history


def build_dict():
    for file in os.listdir('//storage.rcs.nyu.edu/L2_Political/03-01-2020-delivery/files-by-state/'):
    #Depends on OS
    #for file in os.listdir('\\storage.rcs.nyu.edu\L2_Political\03-01-2020-delivery\files-by-state'):
        rename = file[file.find("--")+2:file.find("-2")-1]

        place = file[:file.find(".zip")]
        demographics, vote_history = zip_extractor(place)

        place_dic["%s_demographic" %rename] = demographics
        place_dic["%s_voting_history" %rename] = vote_history
    
    
def create_df(): 
    """
    Iterates through all of the files by state, unzips, and saves in the global 
    dictionary place_dic
    Inputs: None
    Return: None
    """
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


def jitter(df):
    """
    Takes in the dataframe and uses jittering to protect the location of the individual. 
    This promotes security of information while still keeping the data accurate for analysis.
    Input: [dataframe]: dataframe for specific analysis 
    Returns: [dataframe]: dataframe with now protected users locations
    """
    df['Residence_Addresses_Latitude'] = pd.to_numeric(df['Residence_Addresses_Latitude']) 
    df['Residence_Addresses_Longitude'] = pd.to_numeric(df['Residence_Addresses_Longitude']) 
    df.jitter(
        column_name='Residence_Addresses_Latitude',
        dest_column_name='jittered_lat',
        scale=0.2
    )
    df.jitter(
    column_name='Residence_Addresses_Longitude',
    dest_column_name='jittered_long',
    scale=0.2
    )
    df = df.drop(columns=['Residence_Addresses_Latitude', 'Residence_Addresses_Longitude'])
    return df
    

def main(sampleType, whichState, sampleTechnique, sampleSize, informationType, outputType): 
    """
    The main functionality of the process. This calls files, functions, and returns updated 
    dataframes. This also allows the user to save the dataframe as a CSV, TAB, and SHP file at the end. 
    Data visualization platform will also automatically be opened hosted at ArcGIS through 
    the ArcGIS REST API. 
    """
    #create global place_dic 
    global states_dict
    global place_dic
    

    """
    if running large national sample type which is 100+ GB
    if sampleType == "nationalSample":
        create_df()
        state_file_keys = get_state_keys()
        print("--- State File Keys ---")
        print(state_file_keys)
        print("----------------------")
        if sampleTechnique == "stratified":
            pass
        else:
            pass

    """
    if sampleType == "stateSample":
        demographic, vote_history = zip_extractor(states_dict[whichState])
        
    if informationType == "VD":
        df = merge(demographic, vote_history) 
    elif informationType == "V":
        df = demographic
    elif informationType == "D":
        df = vote_history
        
    if sampleSize == "onepercent":
        df = get_sample(df, .01)
    elif sampleSize == "fivepercent":
        df = get_sample(df, .05)
    elif sampleSize == "tenpercent":
        df = get_sample(df, .10)
    elif sampleSize == "twentyfivepercent":
        df = get_sample(df, .25)

    
    print("======= CLEANING DATA ========")
    df = prelim_numeric_converter(df)
    if informationType == "VD" or informationType == "V":
        df = jitter(df)
    df = remove_null(df)
    df = drop_private(df)
    df = election_numeric_converter(df)
    print(df.head())
    if outputType == "csv":
        output = df.to_csv("{}_{}_{}_sample.csv".format(whichState, sampleSize, informationType), index=False, encoding='utf-8')
    elif outputType == "tabfile":
        output = df.to_csv("{}_{}_{}_sample.tsv".format(whichState, sampleSize, informationType), index=False, encoding='utf-8', sep="\t")
    elif outputType == "shapefile":
        output = df.to_csv("{}_{}_{}_sample.csv".format(whichState, sampleSize, informationType), index=False, encoding='utf-8')
    print("======= DONE OUTPUTTING FILE. CHECK YOUR FOLDER ===========")

    if informationType == "VD" or informationType == "V":
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
    return True

    start(df, outputType)
    
    
    


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
