# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os 
from datetime import datetime
today = datetime.now()
wdir = os.chdir(r"C:\Users\anton\OneDrive\Desktop\Working folder")
##insert datetime month format as string instead of August
if not os.path.exists('August'):
    os.makedirs('August')
    
os.chdir("August")
os.mkdir(today.strftime("%B %d"))
os.chdir(today.strftime("%B %d"))
## create a folder with name of the day and date

###import Excel files

###clean up Excel files