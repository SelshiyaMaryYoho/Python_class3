# Merging Datasets 

# 9. What is Merging? 

# Merging is the process of combining two or more DataFrames using a common column or key. 

# Why do we use it?
# - To combine information from different datasets.
# - To connect related records.
# - To create a complete dataset.
# - To prepare data for analysis and Machine Learning. 

import pandas as pd

# First DataFrame
students = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Arun", "Priya", "Kumar"]
})

# Second DataFrame
marks = pd.DataFrame({
    "Student_ID": [1, 2, 4],
    "Marks": [85, 90, 75]
})

print("Students Data:")
print(students)

print("Marks Data:")
print(marks)

# 10. Inner Join 
# Inner join returns only the records that have matching values in both DataFrames.
# To retrieve only matching records from both datasets. 

# on and how are parameters of the Pandas merge function. 
# The on parameter specifies the common column, and 
# the how parameter specifies the type of merging, such as inner, left, right, or outer.

inner_result = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="inner"
)
print("Inner Join Result:")
print(inner_result) 


# 11.left join

# Left join returns all records from the left DataFrame and matching records from the right DataFrame. If there is no match, missing values are displayed. 
# To keep all records from the main or left dataset, even if matching records are missing from the other dataset. 
left_result = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="left"
)
print("Left Join:")
print(left_result) 

# 12. Outer Join 
# Outer join combines all records from both DataFrames.
#  It includes matching and non-matching records. Missing matching values are represented as NaN. 
# To combine all available records from both datasets. 


outer_result = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="outer"
)

print("Outer Join:")
print(outer_result)