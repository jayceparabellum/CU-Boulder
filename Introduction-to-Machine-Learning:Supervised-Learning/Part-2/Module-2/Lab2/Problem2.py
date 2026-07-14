2. Compute Summary Statistics (10 points)
Before applying PCA, it's important to understand the scale of each feature. Features with vastly different scales will dominate PCA if we don't standardize.

Compute the mean, standard deviation, and range (max - min) for each feature.

Store the results as:

q2_means: A dictionary mapping feature names to their mean values (rounded to 2 decimals)
q2_stds: A dictionary mapping feature names to their standard deviation values (rounded to 2 decimals, use ddof=0)
q2_max_range_feature: The name of the feature with the largest range (string)


# Grade Cell: Question 2
#
# Task: Compute summary statistics for each feature
#
# Instructions:
# 1. Calculate the mean of each column and round to 2 decimals
# 2. Calculate the standard deviation of each column (use ddof=0) and round to 2 decimals
# 3. Calculate the range (max - min) for each column
# 4. Find the feature with the largest range

q2_means: Dict[str, float] = {
    col: round(float(df[col].mean()), 2) for col in df.columns
}
q2_stds: Dict[str, float] = {
    col: round(float(df[col].std(ddof=0)), 2) for col in df.columns
}

ranges = {col: float(df[col].max() - df[col].min()) for col in df.columns}
q2_max_range_feature: str = max(ranges, key=ranges.get)

print(f"Feature means: {q2_means}")
print(f"Feature stds: {q2_stds}")
print(f"Feature with largest range: {q2_max_range_feature}")
