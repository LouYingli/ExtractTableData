# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:26:52 2020

@author: YingliLou
"""
import pandas as pd
######
#get output(site EUI)
data=[]
try:
    dfs = pd.read_html('./eplustbl.htm')
    df1 = dfs[0]
    df2 = dfs[2]
    site_energy1 = float(df1.loc[1][1])
    area = float(df2.loc[1][1])
    data.append(str(0.088055066*1000*site_energy1/area)) #get site EUI (KBtu/ft2)
    print df1.loc[1][1]
except:
    print('data error')
        
try:
    dfs = pd.read_html('./eplustbl.htm')
    df2 = dfs[2]
    df3 = dfs[79]
    site_energy2 = float(df3.loc[4][2])
    area = float(df2.loc[1][1])
    data.append(str(0.088055066*1000*site_energy2/area)) #get site EUI (KBtu/ft2)
    print df3.loc[4][2]
except:
    print('data error')
    
print data