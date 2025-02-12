import pandas as pd


a_series = pd.Series([23,5,6,7,8,9])
print("Series: ", a_series)

data = {
    'Name': ['Abhi', 'Kiran', 'Roy', 'Somu', 'Indu'],
    'Marks': [45, 70, 81, 99, 97],
    'Grade': ['5th', '6th', '5th', '9th', '10th']
}
df = pd.DataFrame(data)

print("\nFiltering (Marks > 80):\n", df[df['Marks'] > 80])
print(df.sort_values(by='Marks', ascending=False))
df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x > 70 else 'Fail')
print(df)
print("Average Marks:", df['Marks'].mean())
print("Max Marks:", df['Marks'].max())
print("Min Marks:", df['Marks'].min())
print("Sum of Marks:", df['Marks'].sum())
print("Median Marks:", df['Marks'].median())
print("Standard Deviation of Marks:", df['Marks'].std())
print("Variance of Marks:", df['Marks'].var())
print("Count of Marks:", df['Marks'].count())
print("Describe Marks:", df['Marks'].describe())
print("Unique Marks:", df['Marks'].unique())
print("Unique Marks Count:", df['Marks'].nunique())
print("Value Counts:", df['Marks'].value_counts())
print("Column Names:", df.columns)
print("Index:", df.index)
print("Shape:", df.shape)
df.loc[6] = ['John', None, '8th']  # Add missing marks
print(df)

# Fill missing values with the average marks
df['Marks'].fillna(df['Marks'].mean(), inplace=True)
print(df)


