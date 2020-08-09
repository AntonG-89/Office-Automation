import os 
from datetime import datetime
import shutil


##First function of the day: Create daily folder, populate with worksheets, open the directory for work
def day_start()
    today = datetime.now()
    wdir = os.chdir(r"C:\Users\anton\OneDrive\Desktop\Working folder")
    ## Creating a new month folder/ accessing current month folder
    month = today.strftime("%B")
    if not os.path.exists(month):
        os.makedirs(month)

    ## create a folder with name of the day and date / find a better solution here  
    os.chdir(month)
    os.makedirs(today.strftime("%B %d"), exist_ok = True)
    os.chdir(today.strftime("%B %d"))

    ####import Excel files
    ## below, consider "~Working files" method analog, if it exists, to avoid hardcoding the path to Working Folder\Working files
    source = r"C:\Users\anton\OneDrive\Desktop\Working folder\Working files" ## this folder is hidden, but components are not
    destination = os.getcwd()
    xl_files = os.listdir(source)
    for file in xl_files:
        try:
            new_xl =  shutil.copy(f"{source}/{file}", destination)
            splt = os.path.splitext(new_xl)
            os.rename(new_xl, splt[0] + " " + today.strftime("%B %d") + splt[1])
        except FileExistsError:
            print("File already exists")

    os.startfile(destination)        

    ## Clean Up files
