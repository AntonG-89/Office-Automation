
import os 
from datetime import datetime
import shutil

today = datetime.now()
wdir = os.chdir(r"C:\Users\anton\OneDrive\Desktop\Working folder")
## Creating a new month folder/ accessing current month folder
##insert datetime month format as string instead of August
if not os.path.exists('August'):
    os.makedirs('August')
    
## create a folder with name of the day and date / find a better solution here  
os.chdir("August")
os.mkdir(today.strftime("%B %d"))
os.chdir(today.strftime("%B %d"))

####import Excel files
## below, consider "~Working files" method analog, if it exists, to avoid hardcoding the path to Working Folder\Working files
source = r"C:\Users\anton\OneDrive\Desktop\Working folder\Working files" ## this folder is hidden, but components are not
destination = os.getcwd()
xl_files = os.listdir(source)
for file in xl_files:
    new_xl =  shutil.copy(f"{source}/{file}", destination)
    splt = os.path.splitext(new_xl)
    os.rename(new_xl, splt[0] + " " + today.strftime("%B %d") + splt[1])
    
## Clean Up files
