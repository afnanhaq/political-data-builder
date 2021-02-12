from tkinter import * 
from tkinter import ttk 
# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
from tkinter.filedialog import asksaveasfile 


#Save File as CSV or TAB or ShapeFile 
#TODO Finish this and test

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