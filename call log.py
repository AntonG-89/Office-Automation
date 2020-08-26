
## This is a first try at the function, which sorts rows in the Call Log, picks the ones that have been completed and need follow up, and moves them to a Follow Up worksheet
import pandas as pd
import openpyxl
call_path = r"C:\Users\anton\OneDrive\Desktop\Working folder\Working files\Call Log.xlsx"


## Opening a Call Log
call_log = pd.read_excel(call_path)

## using pd.ExcelWriter append function to add the "Yes" rows to the "Follow Ups" worksheet. 
## This sheet tracks when the records are imported and provides reminders when follow ups are due.
wb = openpyxl.load_workbook(call_path)
writer = pd.ExcelWriter(call_path, engine = "openpyxl", mode= "a")
## This is a weird function. writer.sheets and writer.book have to be created for the append function to work properly.
## explicit statement of .copy() for yes_rows dataframe. Default .view() leads to a SettingWithCopyWarning. 
def move_fus():
    yes_rows = call_log.loc[call_log["Reached?"] == "Yes"].copy()
    yes_cols(yes_rows)
    writer.sheets = dict((ws.title, ws) for ws in wb.worksheets)
    writer.book = wb    
    yes_rows.to_excel(writer, sheet_name ="Sheet1", startrow = wb["Sheet1"].max_row, startcol = 0,  header = False, index =False)

    writer.save()
    writer.close()
  
##This is a function to be used to transform Yes_rows df
def yes_cols(x):
    
    x["Record Date"] = pd.to_datetime("today").strftime("%x")


