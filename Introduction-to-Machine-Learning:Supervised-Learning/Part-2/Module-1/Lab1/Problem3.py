# Grade Cell: Question 3
#
# Task: Compute the range (max - min) for each feature
#
# Instructions:
# 1. For each column, compute max() - min()
# 2. Round to 2 decimal places
# 3. Store as a dictionary

q3_ranges: Dict[str, float] = {
    col: round(float(df[col].max() - df[col].min()), 2) for col in df.columns
}
max_range_feature = max(q3_ranges, key=q3_ranges.get)

print(f"Feature ranges: {q3_ranges}")
print(f"Feature with largest range: {max_range_feature}")
