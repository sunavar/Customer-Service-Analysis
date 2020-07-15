# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:37:47 2020

@author: singh
"""

# 2. Read or convert the columns ‘Created Date’ and Closed Date’ to datetime datatype and create a new column ‘Request_Closing_Time’ as the time elapsed between request creation and request closing.

import datetime as dt
import datetime, time

df['Created Date'] = pd.to_datetime(df['Created Date'])
print(df['Created Date'].dtype)

df['Closed Date'] = pd.to_datetime(df['Closed Date'])
print(df['Closed Date'].dtype)

df['Request_Closing_Time'] = df['Closed Date'] - df['Created Date']
print(df['Request_Closing_Time'].head())