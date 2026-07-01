#The dataset for this lab is the Wisconsin Breast Cancer dataset. The features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image. The target column, diagnosis, indicates whether a tumor is M (malignant) or B (benign).

# Grade Cell: Question 1
#
# Task: Load the dataset and display its first 5 rows.
#
# Instructions:
# 1. Load the 'wisconsin_breast_cancer.csv' file into a pandas DataFrame called `df`.
# 2. Use the `.head()` method to display the first 5 rows.

df = pd.read_csv("wisconsin_breast_cancer.csv")
display(df.head())
print("DataFrame loaded successfully!")
