# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:37:36 2020

@author: singh
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1.Import a 311 NYC service request.

df=pd.read_csv(r'C:\Users\singh\Documents\Data Science using Python Project 1\311_Service_Requests_from_2010_to_Present.csv')

print(df.head())

print(df.shape)

print(df.isnull().sum())

print(df[df['Closed Date'].isnull()])

print(df.dtypes)