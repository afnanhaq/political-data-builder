from tkinter import * 
from tkinter import ttk 
# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
from tkinter.filedialog import asksaveasfile 


#Save File as CSV or TAB or ShapeFile 


root = Tk() 
root.geometry('200x150') 
root.title("File Explorer")

def save(): 
    files = [('CSV Files', '*.csv'), 
             ('Shape Files', '.shp'), 
             ('TAB Files', '*.tab')] 
    file = asksaveasfile(mode='w', filetypes = files, defaultextension = ".csv") 

btn = ttk.Button(root, text = 'Save', command = lambda : save()) 
btn.pack(side = TOP, pady = 20) 


def main(): 
    

main()


# Returns aggregated demographic information for each party
# Argument: a sampled, numeric, demographic or merged dataframe 
def demographic_agg(df):
    try:
        df['counter'] = 1
        data = pd.crosstab(index=df['Parties_Description'], columns=[df['EthnicGroups_EthnicGroup1Desc'],df['Voters_Gender']], values=df['counter'], aggfunc='sum')
        return data
    except:
        print("Sorry, not Enough Information for a Demographic Breakdown")


# Returns aggregated information on historical voting performance for each party
# Argument: a sampled, numeric, merged dataframe
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