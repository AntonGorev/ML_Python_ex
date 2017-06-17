# # Ecommerce Purchases Exercise

import numpy as np
import pandas as pd

# read data from csv
ecom = pd.read_csv('datasets/Ecommerce Purchases.csv')

ecom.info()                # check what I've actually read
ecom.head()                # check the head of the DataFrame


# ** What is the average Purchase Price? **

# In[7]:

ecom['Purchase Price'].mean()


# ** What were the highest and lowest purchase prices? **

# In[8]:

ecom['Purchase Price'].max()


# In[9]:

ecom['Purchase Price'].min()


# ** How many people have English 'en' as their Language of choice on the website? **

# In[19]:

# first approach (count entries of each column, while 'language' == 'en')
ecom[ecom['Language'] == 'en'].count()


# In[18]:

# second approach (see number of entries)
ecom[ecom['Language'] == 'en'].info() 


# ** How many people have the job title of "Lawyer" ? **
# 

# In[21]:

ecom[ecom['Job'] == 'Lawyer'].info()


# In[20]:

# similiar to previous question
ecom[ecom['Job'] == 'Lawyer'].count()


# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# 
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

# In[27]:

ecom['AM or PM'].value_counts()


# In[26]:

ecom.groupby('AM or PM')['AM or PM'].count() # second approach (not very ellegant)


# ** What are the 5 most common Job Titles? **

# In[97]:

ecom['Job'].value_counts().head()      # first approach (5 by default)


# In[43]:

# second approach (a bit stupid though)
ecom.groupby('Job')['Job'].count().sort_values(ascending=False).head()


# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[7]:

ecom[ecom['Lot'] == '90 WT']['Purchase Price']


# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[8]:

ecom[ecom['Credit Card'] == 4926535242672853]['Email']


# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[15]:

ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()


# ** Hard: How many people have a credit card that expires in 2025? **

# In[102]:

# create series with only Expiration Years (take Exp Date column, split each value by '/'
# and take the second part)
ccExpYear = pd.Series([int(el.split('/')[1]) for el in ecom['CC Exp Date'] ])  

(ccExpYear == 25).value_counts()[1]   # first approach


# In[47]:

(ccExpYear == 25).sum()   # second approach


# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[56]:

# create series with domains
emailProvider = pd.Series(el.split('@')[1] for el in ecom['Email'])

# count appearence of each unique domain in the series and output five most popular 
# (sorting descending by default)
emailProvider.value_counts().head()


# # Great Job!
