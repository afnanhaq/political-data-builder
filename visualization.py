from arcgis.gis import GIS
from arcgis.geocoding import geocode
from IPython.display import display
import json

#call this on main

def visualization(df):
    '''
    Puts every coordinate in the data frame into a GIS. Returns a link to the GIS map
    '''
    df = df.loc[:, ['Residence_Addresses_Latitude', 'Residence_Addresses_Longitude']].dropna()
    df['Residence_Addresses_Latitude'] = pd.to_numeric(df['Residence_Addresses_Latitude'])
    df['Residence_Addresses_Longitude'] = pd.to_numeric(df['Residence_Addresses_Longitude'])
    coord = (df[['Residence_Addresses_Longitude', 'Residence_Addresses_Latitude']])
    coord.columns = ['x', 'y']
    fc = gis.content.import_data(coord)
    fc_dict = dict(fc.properties)
    json_voters = json.dumps({"featureCollection": {"layers": [fc_dict]}})
    item_properties = {'title': 'Voters df',
                       'description': 'Example demonstrating conversion of pandas ' + \
                                      'dataframe object to a GIS item',
                       'text': json_voters,
                       'type': 'Feature Collection',
                       'acess': 'public'
                       }
    item = gis.content.add(item_properties)
    item.share(True)

    link_to_map = 'https://nyuds.maps.arcgis.com/home/webmap/viewer.html?useExisting=1&layers=' + str(item.id)
    return link_to_map