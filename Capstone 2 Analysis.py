#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os


# In[8]:


#Finding the working directory
print(os.getcwd())
#Printing the names of files in the current working directory
print(os.listdir(os.getcwd()))
#Changing the working directory to the file that contains the capstone data (SpringBoard Cap2 Data)
os.chdir('C:\\Users\\Admin\\Downloads\\SpringBoard Cap2 Data')
#Creating the dataframe out of the csv file Sales Transaction v.4a
df=pd.read_csv('Sales Transaction v.4a.csv')
#Looking at the dataframe
print(df)


# In[9]:


#Examining the data
print(df.head())
print(df.info())


# In[208]:


#Filtering df to the product names that meet criteria 1
criteria_1 = df.groupby('ProductName').filter(lambda x: x['Quantity'].mean() >= 7 and x['Price'].mean() >= 20)
#Creating variable that shows the product names of that filter
meet_cri1 = criteria_1['ProductName'].unique()
#Printing those names
print(meetcri1)
#Grouping the above data to then get the averages from
c1t_avg= criteria_1.groupby('ProductName')[['Quantity', 'Price']].mean()
print(c1t_avg)
#creating new table to make boxplots from
boxd= criteria_1[['ProductName','Quantity', 'Price']]
#Creating two different plots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7,7))
#Creating the first boxplot to show the quanityt of each product
sns.boxplot(data=boxd, x='ProductName', y='Quantity', color='Red', ax=axes[0])
#Naming the quantity plot
axes[0].set_title('Quantity')
#Rotation the produt name labels
axes[0].tick_params(axis='x', rotation=90)
#Box plotting the price data
sns.boxplot(data=boxd, x='ProductName', y='Price', color='Orange', ax=axes[1])
#Rotating the Product name labels
axes[1].tick_params(axis='x', rotation=90)
#Naming the price plot
axes[1].set_title('Price')
plt.show()


# In[229]:


sns.boxplot(data=boxd, x='ProductName', y='Quantity', color='Red')
plt.xticks(rotation=90)


# In[221]:


#Finding the varance in the form of inter quanrtile range of quantity since it's not visible in the boxplot
q3 = criteria_1.groupby('ProductName')['Quantity'].quantile(0.75)
q1 = criteria_1.groupby('ProductName')['Quantity'].quantile(0.25)
iqr = q3 - q1
print(iqr)


# In[223]:


#Creating the group of product names that meet crietria 1 and 2 by having an 80th percentile of avg quantities above 10
criteria_2= criteria_1.groupby('ProductName')['Quantity'].quantile(0.8).reset_index()
#Returning the names of products that meet criteria 2
meet_cri2= criteria_2.loc[criteria_2['Quantity']>=10, 'ProductName']
print(meet_cri2)
print(criteria_2)
#Sizing chart
plt.figure(figsize=(9,9))
#Creating a colored bar chart
sns.barplot(data=criteria_2, x= 'ProductName', y= 'Quantity', hue= 'Quantity', color= 'Blue')
plt.xticks(rotation=90)
plt.title('Top 20th Percentile of products quantities per order')


# In[225]:


#Making another graph for the 90th percentile to see if there are any products that sell more than 10 units 10% of the time
cri22=criteria_1.groupby('ProductName')['Quantity'].quantile(0.9).reset_index()
sns.barplot(data=cri22, x= 'ProductName', y= 'Quantity', hue= 'Quantity', color= 'Red')
plt.xticks(rotation=90)


# In[148]:


#Creating a column of the dates as datetime data
criteria_1['dt_date']= pd.to_datetime(criteria_1['Date'],format='%m/%d/%Y')
#Creating another column for the month that the order was sold in
criteria_1['month']=criteria_1['dt_date'].dt.month
#Creating a multiple line chart of the quantity sould across months in order to test products for criteria 3: 
#"Sells with minimal fluctuation year-round"
plt.figure(figsize=(10, 6))
#creating new data frame that excludes canceled or reutrned orders
c1=criteria_1[criteria_1['Quantity']>0]
g=sns.lineplot(data=c1, x='dt_date', y='Quantity', hue='ProductName', estimator=None)
g.set_xticklabels(['January', 'March', 'May', 'July', 'September', 'November'])
g.set_xlabel('Month')
g.set_ylabel('Quantity')
#Creating second visual for counting the number of months a product was sold in
m_count=criteria_1.groupby('ProductName')['month'].nunique()
print(m_count)


# In[230]:


#Creating a chart that shows the number of months that each criteria 1 product sold in
#Starting by creating a table that shows the number of countries that each crit 1 product sold in
countries= criteria_1.groupby('ProductName')['Country'].nunique()
#Reseting the index
countries =countries.reset_index()
print(countries)
#Creating a bar plot to visualize
plt.figure(figsize=(7,7))
plt.xticks(rotation=90)
f=sns.barplot(data=countries, x='ProductName', y= 'Country')

