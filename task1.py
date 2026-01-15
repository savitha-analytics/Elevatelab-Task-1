

import pandas as pd

import numpy as np

df = pd.read_csv("Titanic-Dataset.csv")
df.info

df.head()

df.tail()

df.shape

df.columns

df.describe()

# Numerical columns
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
numerical_cols

# Categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
categorical_cols

for col in categorical_cols:
    print(f"\nUnique values in {col}:")
    print(df[col].unique())

df.isnull().sum()

target_variable = "Survived"
input_features = df.drop(columns=[target_variable]).columns

target_variable, input_features

df['Survived'].value_counts()
df['Survived'].value_counts(normalize=True)

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])
