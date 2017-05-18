# [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle!

import pandas as pd
import numpy as np


# In[30]:

pwd


# ** Read Salaries.csv as a dataframe called sal.**

# In[55]:

sal = pd.read_csv('/Users/antongorev/GitHub/ML_Python/mySalaries.csv', na_values = ['Not Provided'])


# ** Check the head of the DataFrame. **

# In[56]:

sal.dtypes


# In[58]:

sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[68]:

sal.info()


# **What is the average BasePay ?**

# In[70]:

sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[73]:

sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[76]:

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[85]:

sal.iloc[24]['TotalPayBenefits'] # First approach


# In[86]:

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']  # Second approach


# ** What is the name of highest paid person (including benefits)?**

# In[87]:

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'] #???????????????


# In[92]:

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()] #??????????


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[90]:

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[96]:

sal.groupby('Year')['BasePay'].mean()


# ** How many unique job titles are there? **

# In[97]:

sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[107]:

sal['JobTitle'].value_counts().head().sort_values(ascending=False)


# In[125]:

sal[sal['Year'] == 2013]['JobTitle'].value_counts().head().sort_values(ascending=False)


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[138]:

JT2013_1 = sal[sal['Year'] == 2013]['JobTitle'].value_counts()
JT2013_1[JT2013_1 == 1].count() #???????????????????????


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[139]:




# In[21]:

# Idk how to get this result, three of my approaches give the same result, but not 477


# In[154]:

# First approach   ??????????????????
jt = sal['JobTitle']
len([ el for el in jt.values if ('Chief' in el) ])


# In[167]:

# Second approach   ??????????????????
df = sal['JobTitle'].value_counts()
chief_df = [el for el in df.keys() if ('Chief' in el)]
sum(df[chief_df])


# In[174]:

# Third approach ????????????????
def my_func(title):
    if 'Chief' in title:
        title = 'UGALUGA'
    return title


df = sal['JobTitle'].apply(my_func)
df[df == 'UGALUGA'].count()


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[22]:

# Create two series from required columns of'sal' dataframe  
title_len = pd.Series(sal['JobTitle'].apply(len), name = 'title_len')
TotalPayBenefits = pd.Series(sal['TotalPayBenefits'])


# In[23]:

# Concatenate both series into the dataframe, then compute pairwise correlation 
pd.concat([title_len, TotalPayBenefits], axis=1).corr()


# # Great Job!
