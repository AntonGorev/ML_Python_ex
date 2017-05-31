# [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle

import pandas as pd
import numpy as np

pwd


# ** Read Salaries.csv as a dataframe called sal.**

sal = pd.read_csv('/Users/antongorev/GitHub/ML_Python/mySalaries.csv', na_values = ['Not Provided'])

# ** Check the head of the DataFrame. **

sal.dtypes

sal.head()


# ** Use the .info() method to find out how many entries there are.**

sal.info()


# **What is the average BasePay ?**

sal['BasePay'].mean()

# ** What is the highest amount of OvertimePay in the dataset ? **

sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

# ** How much does JOSEPH DRISCOLL make (including benefits)? **

sal.iloc[24]['TotalPayBenefits'] # First approach

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']  # Second approach


# ** What is the name of highest paid person (including benefits)?**

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'] # First approach

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]  # full row


sal.loc[sal['TotalPayBenefits'].idxmax()] # Second approach (with idxmax we return index of maximum value 
                                          #  of TotPayBen axis, then we locate the row of this index)


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]

# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

sal.groupby('Year')['BasePay'].mean() # Firstly we groupe all data by 'year', then take 'BasePay' axis and find mean
                                      #  for of each group


# ** How many unique job titles are there? **

sal['JobTitle'].nunique()

# ** What are the top 5 most common jobs? **

sal['JobTitle'].value_counts().head().sort_values(ascending=False)  # head(n=5) by default, 
                                                                    # descending order is default as well


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

JT2013_1 = sal[sal['Year'] == 2013]['JobTitle'].value_counts()
JT2013_1[JT2013_1 == 1].count() # we could also sum all '.value_counts() == 1'


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

## Below there are several different approaches to solve this task. Neither of them leads to the expected (given) 
##  result (477), even the given solution. I explain it with difference in datasets (it might be the case that 
##  solutions were based on old dataset), the most recent dataset from Kaggle yields different result in the end.

## It is not comletely cleare as well should we be case sensitive in while solving this task or not. Thus below one may
##  see result for both cases.

# First approach (case insensitive)
jt = sal['JobTitle']
len([ el for el in jt.values if ('chief' in el.lower()) ])

# Given Solution:
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

sum(sal['JobTitle'].apply(lambda x: chief_string(x)))

# First approach (Case sensitive)
jt = sal['JobTitle']
len([ el for el in jt.values if ('Chief' in el) ])

# Second approach (Case sensitive)
df = sal['JobTitle'].value_counts()
chief_df = [el for el in df.keys() if ('Chief' in el)]
sum(df[chief_df])

# Third approach (Case sensitive)
def my_func(title):
    if 'Chief' in title:
        title = 'UGALUGA'
    return title


df = sal['JobTitle'].apply(my_func)
df[df == 'UGALUGA'].count()


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# Create two series from required columns of'sal' dataframe  
title_len = pd.Series(sal['JobTitle'].apply(len), name = 'title_len')
TotalPayBenefits = pd.Series(sal['TotalPayBenefits'])

# Concatenate both series into the dataframe (in columns 'axis=1'), then compute pairwise correlation 
pd.concat([title_len, TotalPayBenefits], axis=1).corr()

