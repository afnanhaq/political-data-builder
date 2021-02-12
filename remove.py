
def remove_null(df):
    threshold = int(df.shape[1] * 0.75)
    df.dropna(thresh=threshold)
    return df

#Remove null with threshold of 75% 
def remove_null_all(place_dic): 
    for key in place_dic.keys(): 
                        #finds 75% of columns 
        threshold = int(place_dic[key].shape[1] * 0.75)
        place_dic[key].dropna(thresh=threshold)

    return place_dic

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
                    ,'Mailing_Addresses_ZipPlus4']
    
    # getting the indices for columns containing private information
    df.drop(private_cols, axis = 1, inplace = True)
    return df

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
                    ,'Mailing_Addresses_ZipPlus4']
    
    # getting the indices for columns containing private information
    for df in place_dic.values(): 
        df.drop(private_cols, axis = 1, inplace = True)
    return place_dic
