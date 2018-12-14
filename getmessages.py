# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:34:24 2018

@author: zmoran
"""

import requests
import datetime
import pandas as pd
import json

FREEGEOPIP_URL = 'http://api.ipstack.com'
key = 'cd111cd2de8b56abbf2d1be357f8543c'



def time(stamp):
    if stamp > 1451736000 and stamp < 1476878400:
        stamp -= 36000
    return datetime.datetime.fromtimestamp(
        int(stamp)
    ).strftime('%Y-%m-%d %H:%M:%S')

#print(time(1538553409))
    
columns = ['Time','Type','Author','Content','Group','otherPerson','Latitude','Longitude','City','State','Country']

import os
rootdir = r"C:\Users\zmoran\Documents\Silver\Dashboard and Data\Who Am I\USEFUL\messages"

paths = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        test = os.path.join(subdir, file)
        if test[-12:] == 'message.json':
            paths.append(test)
            
csv_array = []

test = []
    
for p in paths:
    tmp = []        
    mes = json.load(open(p))
    if len(mes['participants'])>2:
        group = "Group Chat"
    else:
        group = "NULL"
    for m in mes['messages']:
        tmp = []  
        try:
            tmp.append(time(m['timestamp_ms']/1000))
        except:
            tmp.append("NULL")
        tmp.append("Message")
        try:
            tmp.append(m['sender_name'])
        except:
            tmp.append("NULL")
        try:
            tmp.append(m['content'])
        except:
            tmp.append("NULL")
        tmp.append(group)
        tmp.append("NULL")
        tmp.append("NULL")
        tmp.append("NULL")
        tmp.append("NULL")
        tmp.append("NULL")
        tmp.append("NULL")
        csv_array.append(tmp)
        
df = pd.DataFrame(csv_array)
df.columns = columns
df.to_csv('messages.csv', sep='\t')




tmp = []
for p in paths:       
    mes = json.load(open(p))
    for m in mes['messages']: 
        try:
            tmp.append(m['content'])
        except:
            tmp.append("NULL")
















