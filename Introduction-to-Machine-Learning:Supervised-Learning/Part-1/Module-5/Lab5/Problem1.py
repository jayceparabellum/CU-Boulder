####Datasets (already generated to CSV by the downloader script):

Regression: Diabetes (quantitative target target)
Classification: Breast Cancer (binary target: 0=malignant, 1=benign)

# Grade Cell: Question 1
#
# Task: Load the datasets and show a preview.
#
# Instructions:
# 1. Load the 'diabetes_regression.csv' into DataFrame `df_reg`.
# 2. Load the 'breast_cancer_classification.csv' into DataFrame `df_cls`.
# 3. Display the first 5 rows of each.

from sklearn.datasets import load_diabetes, load_breast_cancer

load_diabetes(as_frame=True).frame.to_csv("diabetes.csv", index=False)
load_breast_cancer(as_frame=True).frame.to_csv("breast_cancer.csv", index=False)

df_reg = pd.read_csv("diabetes.csv")
df_cls = pd.read_csv("breast_cancer.csv")

print(f"df_reg shape: {df_reg.shape}")
print(f"df_cls shape: {df_cls.shape}")
df_reg.head()
df_cls.head()
