# PA3 - Python Data Analysis (PANDAS)
##### This repository features Python scripts designed to solve two programming problems, labeled as Problem 1 and Problem 2. Both problems require the use of PANDAS for data analysis tasks.

##### You can find a code preview below, and a Jupyter notebook is also available in the files section for further exploration.

### Problem 1: 
### Overview:
###### This programming assignment focuses on working with the Cars Dataset using the pandas library in Python. The task involves loading a CSV file, manipulating the data, and extracting specific rows and columns as outlined in the problem.
### What to do?
###### 1) Load the 'cars.csv' file into a pandas DataFrame.
###### 2) Display the first and last five rows of the DataFrame to inspect the dataset.

### Code Implementation
``` python
import pandas as pd

# Load the 'cars.csv' file into a DataFrame named 'cars'
cars = pd.read_csv('cars.csv')

# Show the combined first 5 rows (head) and last 5 rows (tail) of the DataFrame
# 'cars.head()' retrieves the first five rows, while 'cars.tail()' retrieves the last five rows
pd.concat([cars.head(), cars.tail()])
```
### Input: 
* A .csv file named cars.csv.
### Output: 
* The first five rows and the last five rows of the data sheets. 

### Sample Output: 
<img width="599" alt="Screenshot 2024-09-19 at 2 45 58 AM" src="https://github.com/user-attachments/assets/448fe393-cf63-4727-bc98-df1c662a1975">

### Problem 2: 
### Overview: 
###### This problem builds on the Cars Dataset introduced in Problem 1. It involves data extraction from Pandas by using subsetting, slicing, and indexing. 
### What to do? 
###### 1) Display the first five rows but only the columns that have odd-numbered positions.
###### 2) Extract the row that contains the model 'Mazda RX4'.
###### 3) Find out how many cylinders the 'Camaro Z28' model has.
###### 4) Identify the number of cylinders and gear type for the car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.

### Code Implementation 
``` python
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
```
### Input: 
* A .csv file named cars.csv.
### Output:  
* First five rows with odd-numbered columns:
* Row with 'Mazda RX4':
* Number of cylinders ('cyl') for 'Camaro Z28':
* Number of cylinders ('cyl') and gear type ('gear') for specific car models:

### Sample Output: 
<img width="598" alt="Screenshot 2024-09-19 at 2 59 15 AM" src="https://github.com/user-attachments/assets/3ac4e85c-c642-426f-ba30-5bc529e67062">


## Author 
### Ginger Fiona R. Ignacio
### 2ECE-B



