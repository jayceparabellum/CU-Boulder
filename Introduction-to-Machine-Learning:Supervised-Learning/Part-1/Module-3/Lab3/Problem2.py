####Before training a model, the data needs to be preprocessed. This involves encoding the target variable to a numerical format, dropping unnecessary columns, and separating features from the target.


# Grade Cell: Question 2
#
# Task: Prepare the data for modeling.
#
# Instructions:
# 1. Map the 'diagnosis' column to binary values: 'M' (malignant) to 1 and 'B' (benign) to 0.
# 2. Create the feature matrix `X` by dropping the 'diagnosis' column.
# 3. Create the target vector `y` from the now-encoded 'diagnosis' column.

df["diagnosis"] = df["diagnosis"].map({"M": 1, "B": 0})

df = df.drop(columns=["id", "Unnamed: 32"], errors="ignore")

X = df.drop(columns=["diagnosis"])
y = df["diagnosis"]

print("Data preparation successful!")
