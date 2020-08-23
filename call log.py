# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:09:25 2020

@author: anton
"""

import pandas as pd
import openpyxl
call_path = r"C:\Users\anton\OneDrive\Desktop\Work Trial Build\Call Log.xlsx"

call_log = pd.read_excel(call_path)
call_log


yes_rows = call_log.loc[call_log["Reached?"] == "Yes"]
yes_rows
no_rows = call_log.loc[call_log["Reached?"] == "No"]
no_rows


#yes_rows.to_excel(r"C:\Users\anton\OneDrive\Desktop\Work Trial Build\Call Log.xlsx","Follow Ups")
wb = openpyxl.load_workbook(call_path)
writer = pd.ExcelWriter(call_path, engine = "openpyxl", mode= "a")


def move_fus():
    writer.sheets = dict((ws.title, ws) for ws in wb.worksheets)
    writer.book = wb    
    yes_rows.to_excel(writer, sheet_name ="Sheet1", startrow = wb["Sheet1"].max_row, startcol = 0,  header = False, index =False)

    writer.save()
    writer.close()


