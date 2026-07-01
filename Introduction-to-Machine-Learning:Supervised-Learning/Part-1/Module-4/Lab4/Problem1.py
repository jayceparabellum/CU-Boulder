####The dataset contains 10 standardized features and a continuous target. The CSV should be available as diabetes.csv in this folder. If it's missing, run the downloader script for this module.


# Grade Cell: Question 1
#
# Task: Load the dataset and display its first 5 rows.
#
# Instructions:
# 1. Load the 'diabetes.csv' file into a pandas DataFrame called `df`.
# 2. Use the `.head()` method to display the first 5 rows.

df = pd.read_csv("diabetes.csv")
df.head()
print("DataFrame loaded successfully!")
df.head()
