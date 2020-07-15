# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:37:49 2020

@author: singh
"""

# 3. Provide major insights/patterns that you can offer in a visual format (graphs or tables); at least 4 major conclusions that you can come up with after generic data mining.
# Conclusion 1: Frequency of each complain type

print(df['Complaint Type'].value_counts())

df['Complaint Type'].value_counts().plot(kind="bar", color=list('rgbkymc'), figsize=(20,10))
plt.show()

# Conclusion 2: Status of Complaints 

print(df['Status'].value_counts())

df['Status'].value_counts().plot(kind="barh", color=list('rgbkymc'), figsize=(20,10))
plt.show()

# Conclusion 3: Frequency of complaints from different cities

print(df['City'].value_counts())

df['City'].value_counts().plot(kind="bar", color=list('rgbkymc'), figsize=(20,10))
plt.show()

# Conclusion 4: 

def toHour(timeDel):
    days = timeDel.days
    hours = round(timeDel.seconds/3600, 2)
    result = (days * 24) + hours
    return result


df['Request_Closing_In_Hour'] = df['Request_Closing_Time'].apply(toHour)
print(df['Request_Closing_In_Hour'].head())

print(df['Request_Closing_In_Hour'].mean())

import math
def hourToCategory(hr):
    if (math.isnan(hr)):
        return 'Unspecified'
    elif (hr <= 1.0):
        return 'Excellent'
    elif (hr>1.0 and hr<= 2.0):
        return 'Very Good'
    elif (hr>2.0 and hr<= 4.0):
        return 'Good'
    elif (hr>4.0 and hr<=6.0):
        return 'Average'
    else:
        return 'Poor'
    
df['Request_Closing_Time_Category'] = df['Request_Closing_In_Hour'].apply(hourToCategory)
print(df['Request_Closing_Time_Category'].head())

df['Request_Closing_Time_Category'].value_counts().plot(kind='pie',autopct='%1.1f%%', startangle=90)
plt.show()

# Conclusion 5:

months = pd.Series({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'})
print(months)
print(months[12])

def getMonth(Date):
    a = str(Date)
    date = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
    return months[date.month]

df['Created_Month'] = df['Created Date'].apply(getMonth)
print(df['Created_Month'])

print(df['Created_Month'].value_counts())

df['Created_Month'].value_counts().plot(kind="barh", color=list('rgbkymc'), figsize=(15,5))
plt.show()