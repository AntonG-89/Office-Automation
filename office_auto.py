# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os 
from datetime import datetime
import shutil
import winshell
os.chdir(r"C:\Users\anton\OneDrive\Desktop\Working folder")
base_root = r"C:\Users\anton\OneDrive\Desktop\Working folder"


def start_day():
     
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
    
    os.startfile(destination)
    ### List of clients for start_client function, need to itirate over list
       
def start_client():
    client_list = os.listdir(r"C:\Users\anton\OneDrive\Desktop\Working folder\Client Base Hidden")
    openf = input("Enter client's info:Lastname_number :\n")
    # Bool to find if the folder already exists
    file_exists = False
    for client in client_list:
        if client == openf:
            ##Here will be creating shortcut to client file in current directory
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
