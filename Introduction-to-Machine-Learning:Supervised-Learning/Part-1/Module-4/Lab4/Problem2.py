#Separate features X and target y.

# Grade Cell: Question 2
#
# Task: Prepare the data for modeling.
#
# Instructions:
# 1. Create the feature matrix `X` with all columns except `target`.
# 2. Create the target vector `y` from the `target` column.

df = pd.read_csv("diabetes.csv")

X = df.drop(columns=["target"])
y = df["target"]
print("Data preparation successful!")
