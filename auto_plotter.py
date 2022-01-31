# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:08:05 2022

@author: anton
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


#all funct
def main():
    raw_data = pd.read_csv(r'C:\Users\anton\OneDrive\Desktop\Projects\Reddit project\Sample_Data.csv')
    #read in 2nd worksheet from data 
    
    # data clean function
    data = data_clean(raw_data)
    #get plots
    d_df, d = distrb_plot(data)
    all_plot(d_df,d)

    
def distrb_plot(data): 
    for dist in data.Distributors.unique():
        dist_df = data[data.Distributors == dist]    
    return dist_df, dist
    
       
#data cleaning functions

def data_clean(data):
    #setting column names
    data.columns = data.iloc[1]
    #dropping non-data rows
    data = data.drop(data.index[[0,1]])

    #converting datatypes
    data['Chains'] = data['Chains'].astype('category')
    data['Zip Code'] = data['Zip Code'].astype('category')
    
    #current and past years
    today = dt.date.today()
    cur_year = today.strftime('%y')
    past_date = today - dt.timedelta(days=365)
    pas_year = past_date.strftime('%y') 

    #numeric columns/ insert string edit function to get current YTD columns
    num_cols = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
       'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'YTD 21',#'YTD {0}'.format(cur_year)
       'YTD 20',
       #'YTD {0}'.format(pas_year),
       'DIFF CASES', '% DIFF CASES', 'PRV R90 DID BUYS', 'CURR R90 DID BUYS',
       'DIFF DID BUYS', '% DIFF DID BUYS', 'NXT R90 DID BUYS',
       'RW - PRV R90 POD\'S', 'RW - CURR R90 POD\'S', 'RW - DIFF', 'RW - % DIFF',
       'TM - PRV R90 POD\'S', 'TM - CURR R90 POD\'S', 'TM - DIFF', 'TM - % DIFF',
       'VVP - PRV R90 POD\'S', 'VVP - CURR R90 POD\'S', 'VVP - DIFF',
       'VVP - % DIFF', 'TOTAL PREV R90 POD\'S', 'TOTAL CURR R90 POD\'S',
       'DIFF R90 POD\'S', 'MONTHS BOUGHT', 'BOUGHT ONCE', 'Avg SKU Dist',
       'Fall Off ']

    for column in num_cols:
        data[column] = pd.to_numeric(data[column], errors = 'ignore')
        
    return data



#plotter functions

#volume by month
def vol_month(df):
    df  = df[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN','JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'YTD 21']]
    df = pd.melt(df, var_name = 'Month', value_name = 'Sales')
    df = df.groupby(by='Month', sort = False).sum()
    df.Sales = df.Sales.round()
    #plt.bar(df.index,df.Sales)
    return df.index, df.Sales
    
#volume by top chains (plot top 10)
def vol_chain(df):
    df= df[['Chains','JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN','JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'YTD 21']]
    df = df.groupby(by='Chains').sum()
    df['Total'] = df.sum(axis=1)
    #sort and get top 
    #rounding values
    df.Total = df.Total.round()
    #sort and get top 
    df = df.sort_values(by=['Total'])
    df = df.tail(10)
    # drop if sum(chain) is zero
    
    #plt.bar(df.index,df.Total)
    return df.index, df.Total

#distribution - did buy's/ bar chart prev r90 curr r90 and curr-prev
def vol_didbuys(df):
    df = df[['PRV R90 DID BUYS','CURR R90 DID BUYS']]
    df = pd.melt(df, var_name = 'Did Buys', value_name = 'Sales')
    df = df.groupby(by='Did Buys').sum()
    #rounding values
    df.Sales = df.Sales.round()
    #plt.bar(df.index,df.Sales)
    return df.index, df.Sales
    
#dist r90 pod's/ volume by booze types
def vol_bytype(df):
    df = df[['RW - CURR R90 POD\'S','TM - CURR R90 POD\'S','VVP - CURR R90 POD\'S']]
    df = pd.melt(df, var_name = 'Product Type', value_name = 'Sales')
    df = df.groupby(by='Product Type').sum()
    #rounding values
    df.Sales = df.Sales.round()
    #plt.bar(df.index,df.Sales)
    return df.index, df.Sales

#dist one time buy/ did buys ytd and accts || 'TOTAL CURR R90 POD\'S' is used as TOTAL DID BUYS YTD vardf_onetime = data[['TOTAL CURR R90 POD\'S','BOUGHT ONCE']].copy()
def one_time(df):
    df = df[['TOTAL CURR R90 POD\'S','BOUGHT ONCE']]
    ## use YTD 21 
    df = pd.melt(df, var_name = 'Buy Category', value_name = 'Purchases')
    df = df.groupby(by='Buy Category').sum()
    #rounding values
    df.Purchases = df.Purchases.round()
    #plt.bar(df.index,df.Purchases)
    return df.index, df.Purchases
            
#dist nov acct fall off
def fall_off(df):
    df= df[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN','JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']]
    #finding current and previous months
    cur_date = dt.date.today()
    cur_month = cur_date.strftime('%b').upper()
    
    prev_date = cur_date.replace(day=1) - dt.timedelta(days=1)
    prev_month = prev_date.strftime('%b').upper()
    
    purch_date = prev_date - dt.timedelta(days=31)
    purch_month = purch_date.strftime('%b').upper()
    
    next_date= cur_date + dt.timedelta(days=31)
    next_month = next_date.strftime('%b').upper()
    #finding drop off accounts
    drop_offs = df[(df[prev_month] == 0) & (df[cur_month] == 0) & (df[purch_month] != 0)]
    #creating df to plot
    plt_df = pd.DataFrame(data = [len(df),len(drop_offs)], columns = ['Total'],index = ['Current Accs', 'Fall off'])
    #rounding values
    plt_df.Total = plt_df.Total.round()
    #plt.bar(plt_df.index,plt_df.Total)
    return plt_df.index, plt_df.Total, next_month

#create plot figure

def all_plot(df,dist):
    #creating canvas
    fig,ax = plt.subplots(nrows=3,ncols=2,figsize = (15,24))
    
    #defining each plot
    fig1 = ax[0,0]
    fig2 = ax[0,1]
    fig3 = ax[1,0]
    fig4 = ax[1,1]
    fig5 = ax[2,0]
    fig6 = ax[2,1]
    
    ##plotting vol_month at fig1
    #unpacking coordinates
    vol_month_x, vol_month_y = vol_month(df)
    #plotting + settings
    fig1.bar(vol_month_x,vol_month_y)
    fig1.set_xticklabels(labels = vol_month_x, rotation = 25)
    fig1.set_title('Volume by Month')
    fig1.bar_label(fig1.containers[0],label_type = 'edge')
    fig1.get_yaxis().set_visible(False)
   
    
    ##plotting vol_chain at fig2
    vol_chain_x, vol_chain_y = vol_chain(df)
    fig2.bar(vol_chain_x,vol_chain_y)
    fig2.set_xticklabels(labels = vol_chain_x, rotation = 25)
    fig2.set_title('Volume by Top Chain')
    fig2.bar_label(fig2.containers[0], label_type = 'edge')
    fig2.get_yaxis().set_visible(False)
    
    ##plotting vol_didbuys at fig3
    vol_didbuys_x, vol_didbuys_y = vol_didbuys(df)
    fig3.bar(vol_didbuys_x,vol_didbuys_y)
    fig3.set_xticklabels(labels=['Prev R90','Curr R90'])
    fig3.set_title('Distribution - Did Buy\'s')
    fig3.bar_label(fig3.containers[0], label_type = 'edge')
    fig3.get_yaxis().set_visible(False)
    #swap bars
    
    #pltting vol_bytype at fig4
    vol_bytype_x, vol_bytype_y = vol_bytype(df)
    fig4.bar(vol_bytype_x,vol_bytype_y)
    fig4.set_title('Distribution - R90 POD\'s')
    fig4.set_xticklabels(labels = ['Ranch Water','Tequila Margarita','Vodka Variety'])
    fig4.bar_label(fig4.containers[0], label_type = 'edge')
    fig4.get_yaxis().set_visible(False)
    
    #plotting one_time at fig5
    one_time_x, one_time_y = one_time(df)
    fig5.bar(one_time_x,one_time_y)
    fig5.set_title('Distribution- One Time Buy')
    fig5.set_xticklabels(labels=['Accts Bought Once','Total Did Buys YTD'])
    fig5.bar_label(fig5.containers[0], label_type = 'edge')
    fig5.get_yaxis().set_visible(False)
    #swap bars
    
    #plotting fall_off at fig6
    fall_off_x,fall_off_y, month = fall_off(df)
    fig6.bar(fall_off_x,fall_off_y)
    fig6.set_title('Distribution - {0} Account Fall Off'.format(month))
    fig6.bar_label(fig6.containers[0], label_type = 'edge')
    fig6.get_yaxis().set_visible(False)
    
    #setting figure title
    fig.suptitle(dist)
    
    #exporting fig to PDF
    plt.savefig('{0} report.pdf'.format(month))
    
