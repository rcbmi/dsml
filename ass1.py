#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question:1. Perform the following operations using Python on a data set : read data
# from different formats(like csv, xls),indexing and selecting data, sort data,
# describe attributes of data, checking data types of each column. (Use
# Titanic Dataset).


# In[1]:


print("hello")


# In[2]:


import pandas as pd


# In[4]:


df_csv=pd.read_csv("Titanic.csv")
print(df_csv.head(),'\n')
# df_exl=pd.read_excel("tested.xls")


# In[6]:


df=df_csv


# In[7]:


# select a single column
print("Name Column")
print(df["Name"].head())


# In[8]:


print("Name and Sex column")
print(df[["Name","Sex"]].head())


# In[10]:


# to access row by its index
df.loc[0]


# In[13]:


print(df.iloc[1:5])
# will print data for row 1 to row 4


# In[12]:


print(df.loc[0:5])
# print data for all rows qith index 0 to 5


# In[14]:


print("Passengers with age>50")
print(df[df["Age"]>50].head())


# In[16]:


# 4.Sorting the data
# sort by age in ascending order
df_sorted_age=df.sort_values(by="Age")

print(df_sorted_age[["Name","Sex","Ticket","Fare","Age"]].head())


# In[18]:


df_sorted_multi=df.sort_values(by=["Pclass","Fare"],ascending=[True,False])
print("data sorted by Pclass (asc) and Fare (desc):")
print(df_sorted_multi[["Name","Sex","Pclass","Fare","Age"]].head())


# In[19]:


# Describing attributes of data
print("Summary statistics of numerical data")
print(df.describe())



# In[23]:


print("Summmary for all columns including object type")
print(df.describe(include="all"),"\n")


# In[24]:


# print datatypes
print(df.dtypes,"\n")


# In[25]:


# for more info including datatypes
print(df.info())


# In[ ]:
print("\nSelecting the first 3 rows and specific columns (Name, Age):")
print(df.loc[:2, ['Name', 'Age']])  # Adjust columns based on your dataset structure



