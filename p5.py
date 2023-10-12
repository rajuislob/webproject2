import pandas as pd
import matplotlib.pyplot as plt

# Define the column names
column_names = ["sepal_length_cm", "sepal_width_cm", "petal_length_cm", "petal_width_cm", "class"]

# Specify the path to the iris.data file
file_path = "iris.data"

# Read the data into a DataFrame
df = pd.read_csv(file_path, names=column_names)

# Print the DataFrame
print(df)


# Task (a) - Bar chart for class label frequency
class_counts = df['class'].value_counts()
classes = class_counts.index
frequency = class_counts.values

plt.figure(figsize=(16, 12))
plt.bar(classes, frequency)
plt.title('Class Label Frequency')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.show()

# Task (b) - Scatter plot for Petal width vs Sepal width
plt.figure(figsize=(16, 12))
classes = df['class'].unique()
for cls in classes:
    data = df[df['class'] == cls]
    plt.scatter(data['petal_width_cm'], data['sepal_width_cm'], label=cls)

plt.title('Petal width vs Sepal width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()


# Task (c) - Density distribution for Petal length
plt.figure(figsize=(16, 12))
plt.hist(df['petal_length_cm'], bins=20, density=True, alpha=0.6, color='b')
plt.title('Density Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Density')
plt.show()


# Task (d) - Pair plot for pairwise bivariate distribution
from pandas.plotting import scatter_matrix

scatter_matrix(df, alpha=0.8, figsize=(12, 12), diagonal='hist')
plt.show()
