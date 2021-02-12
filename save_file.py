import pandas as pd
from tkinter import * 
from tkinter import ttk 
# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
from tkinter.filedialog import asksaveasfile 


#Save File as CSV or TAB or ShapeFile 
#TODO Finish this and test
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


#TODO Delete this main below, only used for testing purposes
def main():
    data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
    # Create the pandas DataFrame 
    df = pd.DataFrame(data, columns = ['Name', 'Age'])
    start(df)

main()