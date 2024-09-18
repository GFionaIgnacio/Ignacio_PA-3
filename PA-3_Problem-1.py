#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd

#Load the 'cars.csv' file into a DataFrame named 'cars'
cars = pd.read_csv('cars.csv')

# Show the combined first 5 rows (head) and last 5 rows (tail) of the DataFrame
# 'cars.head()' retrieves the first five rows, while 'cars.tail()' retrieves the last five rows
pd.concat([cars.head(), cars.tail()])


# In[ ]:




