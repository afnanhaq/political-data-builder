# -*- coding: utf-8 -*-
"""
The class remove is used for data anonymization and dropping of columns
with over 75% NaN values. It implements privacy protection by dropping 
columns containing personally identifiable information.
"""

# remove_null(df) reads in a dataset, drops columns that have 
# over 75% of their values as NaN, and then returns the modified
# dataframe
# df: dataset for a state, pandas.DataFrame 
# returns df, without columns that are primarily filled with nulls

def remove_null(df):
    threshold = int(df.shape[1] * 0.75)
    df.dropna(thresh=threshold)
    return df

# remove_null_all(place_dic) reads in all data from the global variable 
# 'place_dic' and drops columns that have over 75% of their
#  values as NaN, and then returns the modified dictionary
# place_dic: dictionary, must be the global dictionary in 'main'
# returns place_dic, without columns that are primarily filled with nulls
    
def remove_null_all(place_dic): 
    for key in place_dic.keys(): 
                        #finds 75% of columns 
        threshold = int(place_dic[key].shape[1] * 0.75)
        place_dic[key].dropna(thresh=threshold)

    return place_dic

# drop_private(df) reads in a dataset and drops columns 
# that have identifiable data. it then returns the modified dictionary
# df: dataset for a state, pandas.DataFrame 
# returns df, without columns that have personally identifable info
    
def drop_private(df):
    # list of all columns that contain private information
    private_cols = ['VoterTelephones_Landline7Digit'
                    ,'VoterTelephones_LandlineUnformatted'
                    ,'VoterTelephones_CellPhoneFormatted'
                    ,'VoterTelephones_CellPhoneUnformatted'
                    ,'Voters_FirstName'
                    ,'Voters_MiddleName'
                    ,'Voters_LastName'
                    ,'Voters_NameSuffix'
                    ,'Residence_Addresses_AddressLine'
                    ,'Residence_Addresses_ExtraAddressLine'
                    ,'Residence_Addresses_ZipPlus4'
                    ,'Residence_Addresses_HouseNumber'
                    ,'Residence_Addresses_PrefixDirection'
                    ,'Residence_Addresses_StreetName'
                    ,'Residence_Addresses_Designator'
                    ,'Residence_Addresses_SuffixDirection'
                    ,'Residence_Addresses_ApartmentNum'
                    ,'Residence_Families_FamilyID'
                    ,'Mailing_Addresses_AddressLine'
                    ,'Mailing_Addresses_ExtraAddressLine'
                    ,'Mailing_Addresses_HouseNumber'
                    ,'Mailing_Addresses_PrefixDirection'
                    ,'Mailing_Addresses_StreetName'
                    ,'Mailing_Addresses_Designator'
                    ,'Mailing_Addresses_SuffixDirection'
                    ,'Mailing_Addresses_ApartmentNum'
                    ,'Mailing_Families_FamilyID'
                    ,'Voters_BirthDate'
                    ,'Residence_Addresses_City'
                    ,'DateConfidence_Description'
                    ,'Precinct'
                    ,'VoterTelephones_LandlineAreaCode'
                    ,'Residence_Addresses_State' 
                    ,'Residence_Addresses_LatLongAccuracy'
                    ,'Mailing_Addresses_ZipPlus4'
                    ,'Voters_StateVoterID']
    
    # dropping columns with the names listed in 'private_cols'
    df.drop(private_cols, axis = 1, inplace = True)
    return df

# drop_private_all(place_dic) reads in all data from the global variable 
# 'place_dic' and drops columns that have identifiable data.
# it then returns the modified dictionary
# place_dic: dictionary, must be the global dictionary in 'main'
# returns place_dic, without columns that have personally identifable info

def drop_private_all(place_dic):
    # list of all columns that contain private information
    private_cols = ['VoterTelephones_Landline7Digit'
                    ,'VoterTelephones_LandlineUnformatted'
                    ,'VoterTelephones_CellPhoneFormatted'
                    ,'VoterTelephones_CellPhoneUnformatted'
                    ,'Voters_FirstName'
                    ,'Voters_MiddleName'
                    ,'Voters_LastName'
                    ,'Voters_NameSuffix'
                    ,'Residence_Addresses_AddressLine'
                    ,'Residence_Addresses_ExtraAddressLine'
                    ,'Residence_Addresses_ZipPlus4'
                    ,'Residence_Addresses_HouseNumber'
                    ,'Residence_Addresses_PrefixDirection'
                    ,'Residence_Addresses_StreetName'
                    ,'Residence_Addresses_Designator'
                    ,'Residence_Addresses_SuffixDirection'
                    ,'Residence_Addresses_ApartmentNum'
                    ,'Residence_Families_FamilyID'
                    ,'Mailing_Addresses_AddressLine'
                    ,'Mailing_Addresses_ExtraAddressLine'
                    ,'Mailing_Addresses_HouseNumber'
                    ,'Mailing_Addresses_PrefixDirection'
                    ,'Mailing_Addresses_StreetName'
                    ,'Mailing_Addresses_Designator'
                    ,'Mailing_Addresses_SuffixDirection'
                    ,'Mailing_Addresses_ApartmentNum'
                    ,'Mailing_Families_FamilyID'
                    ,'Voters_BirthDate'
                    ,'Residence_Addresses_City'
                    ,'DateConfidence_Description'
                    ,'Precinct'
                    ,'VoterTelephones_LandlineAreaCode'
                    ,'Residence_Addresses_State' 
                    ,'Residence_Addresses_LatLongAccuracy'
                    ,'Mailing_Addresses_ZipPlus4'
                    ,'Voters_StateVoterID']
    
    # dropping columns with the names listed in 'private_cols'
    for df in place_dic.values(): 
        df.drop(private_cols, axis = 1, inplace = True)
    return place_dic
