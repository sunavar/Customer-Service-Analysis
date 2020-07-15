# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:37:51 2020

@author: singh
"""

# 4. Order the complaint types based on the average ‘Request_Closing_Time’, grouping them for different locations.

print(df['City'].isnull().sum())

df['City'].fillna('NA', inplace=True)

print(df['City'].head())

grouped_df=df.groupby(['City', 'Complaint Type'])
#print(grouped_df)

RC_mean = grouped_df.mean()['Request_Closing_In_Hour']
print(RC_mean)

print(RC_mean.isnull().sum())

grouped_df = df.groupby(['City','Complaint Type']).agg({'Request_Closing_In_Hour': 'mean'})
print(grouped_df)

print(grouped_df[grouped_df['Request_Closing_In_Hour'].isnull()])

grouped_df=grouped_df.dropna()

print(grouped_df.isnull().sum())

print(grouped_df)

grouped_df.sort_values(['City', 'Request_Closing_In_Hour'])
print(grouped_df)