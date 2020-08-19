import os 
from datetime import datetime
import shutil
import winshell
import pandas as pd
# all hardcoded paths need to be changed to path.join solutions for scalability
os.chdir(r"C:\Users\anton\OneDrive\Desktop\Working folder")
base_root = r"C:\Users\anton\OneDrive\Desktop\Working folder"
client_root = r"C:\Users\anton\OneDrive\Desktop\Working folder\Client Base Hidden"
## First function of the day. Create workspace, add the edited Excel worksheets, ready for the day, 
## launch everything. Creating a global variable.
def start_day():
    # Need to add pin daily root to the task bar 
    global daily_root
    today = datetime.now()
    os.chdir(r"C:\Users\anton\OneDrive\Desktop\Working folder")
## Creating a new month folder/ accessing current month folder
##insert datetime month format as string instead of August
    month = today.strftime("%B")
    if not os.path.exists(month):
        os.makedirs(month)
 ## create a folder with name of the day and date   
    os.chdir(month)
    os.makedirs(today.strftime("%B %d"), exist_ok = True)
    os.chdir(today.strftime("%B %d"))
    
####import Excel files
    source = r"C:\Users\anton\OneDrive\Desktop\Working folder\Working files" ## this folder is hidden, but components are not
    destination = os.getcwd()
    xl_files = os.listdir(source)
    for file in xl_files:
        ## this error handling is a poor implementation, I want to prevent files from being copied, not renamed
        try:
            new_xl =  shutil.copy(f"{source}/{file}", destination)
            splt = os.path.splitext(new_xl)
            os.rename(new_xl, splt[0] + " " + today.strftime("%B %d") + splt[1])
        except FileExistsError:
            print ("File already exists")
 # Open current file
    os.startfile(destination)
    
## Global variable with root for today's work. Used in next_clt()
    daily_root = destination
      
## Starting a file for a client for the workday. Creating a shortcut to a main folder with all client files,
## or creating a new file. Launching the daily Excel, with Prod and UT wbs.
def start_client():
##Missing excel import functionality. Excel spreadsheets coming.
## Need to add pin to the taskbar for each client. 
    client_list = os.listdir(client_root)
    openf = input("Enter client's info:Lastname_number :\n")
    # Bool to find if the folder already exists
    file_exists = False
    for client in client_list:
        if client == openf:
            file_exists = True
            break
        else:
            continue
    # Creating a new folder if new client
    if file_exists == False:
         os.mkdir(r"C:\Users\anton\OneDrive\Desktop\Working folder\Client Base Hidden\%s" % openf)
         
    # Creating shortcut
    new_client = r"C:\Users\anton\OneDrive\Desktop\Working folder\Client Base Hidden\%s" % openf    
    winshell.CreateShortcut(
            Path = os.path.join(os.getcwd(), "%s.lnk" % openf ), 
            Target = new_client,
            Icon = (new_client,0))
   #Opening workspace. Once Excel wb added, it will be opened here as well. 
     os.chdir(new_client)
     os.startfile(new_client)   
## Since the functionality is dependant on the current working directory, this function allows movement between
## client files that have aleady been opened today.
def next_clt():
    n_client = input("Please enter the next file you would like to work on: \n")
    n_client_sc = n_client + ".lnk"
    ##List of today's clients from the daily root folder. Using global variable
    today_clients = os.listdir(daily_root) 
    e_client = False
##Checking if the shortcut to the client file was created today. This will make sure all client work is clearly visible
## in each daily folder. Plus this will allow easier navigation once pins are added.
    for i in today_clients:
       print(type(i))
       if n_client_sc != i:
           continue
       else:
          e_client = True
           
## If client file was opened today, this moves the current directory to the desired client file and launches the file          
    destination = os.path.join(client_root,n_client)
    print(destination)
    if e_client == True:
        try:
            os.chdir(destination)
        except FileNotFoundError:
            print("This client file has not been created yet")
            
    os.startfile(destination)
