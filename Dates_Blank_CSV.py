# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:20:25 2021

@author: Jacob Oppelt
"""
import re
import pandas as pd

dates_data = []*7502
x_position_data = ['0']*7502
y_position_data = ['0']*7502
name_data = ['0']*7502
activity_data = ['0']*7502
dates_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')
x_position_pattern = re.compile(r'([N]\d{2}|[S]\d{2})')
y_position_pattern = re.compile(r'([E]\d{2}|[S]\d{2})')
name_pattern = re.compile(r'(NOAA\s\d{4,5}|NOAA\d{4,5})')

dates_file=open("dates.txt")
dates_file_txt=dates_file.read().replace("\n","")
dates_file.close()

dates_matches = dates_pattern.findall(dates_file_txt)

for match in dates_matches:
    dates_data.append(match)

positions

df = pd.DataFrame([dates_data, x_position_data, y_position_data, name_data, activity_data]).T
df.index.name = 'Message Number'
df.columns=['Date', 'E-W Position', 'N-S Position', 'NOAA Name', 'Activity']


df.to_csv("d-blank.csv")
