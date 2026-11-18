# What is Data Cleaning?
# Data cleaning is the process of identifying and correcting missing values, duplicate records, incorrect data types, and other errors in a dataset.
# Why do we use it?
# - To remove incorrect data.
# - To handle missing values.
# - To remove duplicate records.
# - To correct data types.
# - To improve data quality before analysis or Machine Learning.


# 2. isna()
# The isna() function is used to identify missing values in a DataFrame. It returns True for missing values and False for available values.
# To identify missing values in a dataset
import pandas as pd

df = pd.read_csv("students.csv")

print("2.isna():")
print(df.isna())


# 3. dropna()
# The dropna() function removes rows containing missing values. 
# It helps us remove incomplete records from a dataset.


import pandas as pd

df = pd.read_csv("students.csv")

cleaned_data = df.dropna()

print("3.dropna():")
print(cleaned_data)


# 4. fillna()
# fillna() is used to replace missing values with a specified value.
# To handle missing values without removing entire rows

import pandas as pd

df = pd.read_csv("students.csv")

df["Marks"] = df["Marks"].fillna(0)

print("4.fillna():")
print(df)


# 5. Duplicates
# Duplicate records are repeated rows in a dataset. Pandas provides duplicated() to identify them and drop_duplicates() to remove them.
# To avoid repeated records and maintain accurate data.
import pandas as pd

df = pd.read_csv("students.csv")

print("5.Duplicate Records:")
print(df[df.duplicated()])

df = df.drop_duplicates()

print("After Removing Duplicates:")
print(df)


# 6. Data Types 
# Data types define the kind of values stored in each column, such as integer, float, string, or date. 
# To ensure that data is stored in the correct format and calculations work correctly.

import pandas as pd

df = pd.read_csv("students.csv")

print(df.dtypes)

# Changing data types
# Suppose Age should be an integer column. 

df["Age"] = df["Age"].fillna(0).astype(int)

print("6. Data Types:")
print(df.dtypes)