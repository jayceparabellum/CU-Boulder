4. Mean Imputation Baseline (10 points)
The simplest imputation strategy is mean imputation: replace each missing value with the mean of its column (movie mean).

Since we've already centered the data, mean imputation simply replaces NaN values with 0 (the centered mean).

Store the results as:

q4_mean_imputed: The centered matrix with NaN replaced by 0
q4_has_nan: Boolean indicating if any NaN values remain (should be False)
q4_imputed_range: Tuple of (min, max) values in the imputed matrix
# Grade Cell: Question 4
#
# Task: Perform mean imputation on the centered matrix
#
# Instructions:
# 1. Replace all NaN values with 0 (since data is centered)
# 2. Verify no NaN values remain
# 3. Compute the range of values in the imputed matrix




q4_mean_imputed = np.nan_to_num(q3_centered_matrix, nan=0.0)

q4_has_nan: bool = bool(np.isnan(q4_mean_imputed).any())

q4_imputed_range: Tuple[float, float] = (
    float(q4_mean_imputed.min()),
    float(q4_mean_imputed.max()),
)

print(f"Imputed matrix shape: {q4_mean_imputed.shape}")
print(f"Contains NaN: {q4_has_nan}")
print(f"Value range: {q4_imputed_range}")
