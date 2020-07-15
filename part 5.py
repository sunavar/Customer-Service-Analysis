# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:39:25 2020

@author: singh
"""

#5. Perform a statistical test for the following:
#Please note: For the below statements you need to state the Null and Alternate and then provide a statistical test to accept or reject the Null Hypothesis along with the corresponding ‘p-value’.

#Whether the average response time across complaint types is similar or not (overall)
#Are the type of complaint or service requested and location related?

import scipy.stats as stats
from math import sqrt

# Since we have to compare average of more than two variables. Therefore, we use ANOVA for Part 1 - #Whether the average response time across complaint types is similar or not (overall)

# Null hypothesis H0 : All Complain Types average response time mean is similar
# Alternate hypothesis H1 : All Complain Types average response time mean is Not similar

print(df['Complaint Type'].value_counts())

top_complaints_type = df['Complaint Type'].value_counts()[:5]
print(top_complaints_type)

top_complaints_type_names = top_complaints_type.index
print(top_complaints_type_names)

sample = df.loc[df['Complaint Type'].isin(top_complaints_type_names), ['Complaint Type', 'Request_Closing_In_Hour']]
print(sample.head())

print(sample.shape)

print(sample.isnull().sum())

sample.dropna(inplace=True)
print(sample.isnull().sum())

set1 = sample[sample['Complaint Type'] == top_complaints_type_names[1]].Request_Closing_In_Hour
print(set1.head())

set2 = sample[sample['Complaint Type'] == top_complaints_type_names[2]].Request_Closing_In_Hour
print(set2.head())

set3 = sample[sample['Complaint Type'] == top_complaints_type_names[3]].Request_Closing_In_Hour
print(set3.head())

set4 = sample[sample['Complaint Type'] == top_complaints_type_names[4]].Request_Closing_In_Hour
print(set4.head())

set5 = sample[sample['Complaint Type'] == top_complaints_type_names[0]].Request_Closing_In_Hour
print(set5.head())

stats.f_oneway(set1, set2, set3, set4, set5)

# Since, pvalue<0.05 we reject null hypothesis.
# Therefore, All Complain Types average response time mean is Not similar

# Try ChiSquare Test for part2  -  Are the type of complaint or service requested and location related?

# Null Hypothesis H0 : Complain Type and Location is not related
# Alternate Hypothesis H1 : Complain Type and Location is related

from scipy.stats import chi2_contingency
top_location = df['City'].value_counts()[:5]
print(top_location)

top_location_names = top_location.index
print(top_location_names)

sample2 = df.loc[(df['Complaint Type'].isin(top_complaints_type_names)) & (df['City'].isin(top_location_names)), ['Complaint Type', 'City']]
print(sample2.head())

C_table=pd.crosstab(sample2['Complaint Type'], sample2['City'])
print(C_table)

ch2, p, dof, tb1 = chi2_contingency(C_table)

print(ch2,p,dof)

# Since, p<0.05 we reject null hypothesis.
# Therefore, Complain Type and Location is related