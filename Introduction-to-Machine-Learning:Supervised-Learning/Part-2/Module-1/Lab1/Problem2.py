# Grade Cell: Question 2
#
# Task: Compute summary statistics for each feature
#
# Instructions:
# 1. Calculate the mean of each column
# 2. Calculate the standard deviation of each column (use ddof=0)
# 3. Round values to 2 decimal places
# 4. Store as dictionaries with column names as keys

q2_means: Dict[str, float] = {
    col: round(float(df[col].mean()), 2) for col in df.columns
}
q2_stds: Dict[str, float] = {
    col: round(float(df[col].std(ddof=0)), 2) for col in df.columns
}

print("Means:", q2_means)
print("Stds: ", q2_stds)
