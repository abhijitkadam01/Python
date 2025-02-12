import pandas as pd

# Creating a Series
data_series = pd.Series([10, 20, 30, 40, 50])
print("Pandas Series:\n", data_series)

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Berlin']
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)

# Basic Operations
print("\nColumn Selection (Age):\n", df['Age'])
print("\nFiltering (Age > 30):\n", df[df['Age'] >= 30])
