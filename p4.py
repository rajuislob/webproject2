import pandas as pd

# Load data from the two Excel files
df1 = pd.read_excel('file1.xlsx')
df2 = pd.read_excel('file2.xlsx')

# a. Perform merging to find the names of students who attended the workshop on both days.
common_attendance = df1.merge(df2, on='Name', how='inner')
print("a. Names of students who attended the workshop on both days:")
print(common_attendance['Name'])

# b. Find names of all students who attended the workshop on either of the days.
unique_in_df1 = df1[~df1['Name'].isin(df2['Name'])]
unique_in_df2 = df2[~df2['Name'].isin(df1['Name'])]
unique_values = pd.concat([unique_in_df1, unique_in_df2])
print("b. Names of students who attended the workshop on either day:")
print(unique_values)

# c. Merge two dataframes row-wise and find the total number of records in the dataframe.
merged_rowwise = pd.concat([df1, df2])
total_records = len(merged_rowwise)
print(f"c. Total number of records in the merged dataframe: {total_records}")

# d. Merge two dataframes and use two columns, 'Name' and 'Duration', as multi-row indexes. Generate descriptive statistics.
# Merge the dataframes on 'name'
merged_df = pd.concat([df1,df2])
merged_df.set_index(['Name','Duration'],inplace=True)
statistics = merged_df.describe()
print("Merged DataFrame with Multi-Row Index:")
print(merged_df)

print("\nDescriptive Statistics:")
print(statistics)
