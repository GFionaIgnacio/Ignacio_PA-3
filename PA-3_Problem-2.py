#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# Load the 'cars.csv' file into a DataFrame named 'cars'. 
cars = pd.read_csv('cars.csv')

# a. Display the first five rows with odd-numbered columns (1, 3, 5, 7...)
# Select the first 5 rows and every other column starting from index 1.
print("First five rows with odd-numbered columns:")
print(cars.iloc[:5, 1::2])

# b. Display the row where the 'Model' is 'Mazda RX4'
# Filter the DataFrame to get the row where the 'Model' column equals 'Mazda RX4'.
print("\nRow with Model 'Mazda RX4':")
print(cars[cars['Model'] == 'Mazda RX4'])

# c. Find out how many cylinders ('cyl') the 'Camaro Z28' model has
# Use .loc to filter the row where 'Model' is 'Camaro Z28' and retrieve the 'cyl' column.
# Since the output is a Series, apply .iloc[0] to extract the scalar value for the number of cylinders.
print(f"\nCylinders in 'Camaro Z28':")
print(f"{cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].iloc[0]} cylinders")

# d. Identify the number of cylinders ('cyl') and the gear type ('gear') for the models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.
# Use .isin() to filter the rows where the 'Model' matches any of the specified car models
# Select the 'Model', 'cyl', and 'gear' columns for display.
print("\nCylinders and gear type for selected models:")
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars[cars['Model'].isin(models)][['Model', 'cyl', 'gear']])


# In[ ]:




