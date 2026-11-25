# GroupBy and Aggregations

# 7. What is GroupBy? 

# GroupBy is used to group records based on a particular column. 
# For example, we can group employees by department and calculate the total salary for each department. 

# Why do we use it?
# - To group similar records.
# - To analyze department-wise data.
# - To calculate group-wise totals and averages.
# - To compare different categories. 

import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Ravi"],
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "Salary": [30000, 25000, 35000, 28000, 40000]
}

df = pd.DataFrame(data)

# Grouping employees by department
grouped = df.groupby("Department")

print(grouped["Salary"].sum()) 


# 8. What is Aggregation? 

# Aggregation means performing calculations on grouped data to get a summary, 
# such as sum, mean, count, minimum, or maximum. 

# To summarize large amounts of data and understand the results easily. 

import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Ravi"],
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "Salary": [30000, 25000, 35000, 28000, 40000]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "count", "min", "max"]
)

print(result)