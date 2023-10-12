import pandas as pd
import numpy as np

print("data with 3 columns and 50 rows\n")
np.random.seed(42)
data=np.random.rand(50,3)
df=pd.DataFrame(data,columns=['column1','column2','column3'])
print(df)
print("\n")

print("replaceed 10% values with NaN\n")
null_indexes =np.random.choice([True,False],size=(50,3),p=[0.10,0.90])
df.iloc[null_indexes]=np.nan
print(df)
print("\n")

print("(a)missing values in a dataframe \n")
missing_value_count=df.isnull().sum().sum()
print(missing_value_count)
print("\n")

print(" b. Drop the column having more than 5 null values\n")
df=df.dropna(thresh=5,axis=1)
print(df)
print("\n")

print(" c. Identify the row label having maximum of the sum of all values in a row and drop that row. \n")
max_sum_rows_label=df.sum(axis=1).idxmax()
df=df.drop(max_sum_rows_label)
print(df)
print("\n")

print(" d. Sort the dataframe on the basis of the first column\n")
df=df.sort_values(by='column1')
print(df)
print("\n")

print(". e. Remove all duplicates from the first column\n")
df=df.drop_duplicates(subset='column1')
print(df)
print("\n")

print("f. Find the correlation between first and second column and covariance between second and third column\n")
corr=df['column1'].corr(df['column2'])
cova=df['column2'].cov(df['column3'])
print("correlation :", corr)
print("covarience :" ,cova)
print("\n")



print("g. Detect the outliers and remove the rows having outliers\n")
outliner_mask=pd.Series(data=False,index=df.index)

for col in df.columns :
    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    iqr=q3-q1
    uf=q3+(1.5*iqr)
    lf=q1-(1.5*iqr)
    outliner_mask |= (df[col] < lf) | (df[col]>uf)
df=df[~outliner_mask]
print(df)
print("\n")


print(". h. Discretize second column and create 5 bins\n")  
df['c2_bins']=pd.cut(df['column2'],bins=5)
print(df)
print("\n")
