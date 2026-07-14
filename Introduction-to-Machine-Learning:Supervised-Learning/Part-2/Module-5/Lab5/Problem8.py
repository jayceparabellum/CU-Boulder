8. Evaluate Imputation Quality (10 points)
Now let's evaluate how well our matrix completion recovers the missing values. We have access to the ground truth ratings (before masking) stored in ratings_ground_truth.csv.

Compare the imputed values against the true values for entries that were originally missing.

Store the results as:

q8_ground_truth: The ground truth rating matrix (loaded from CSV)
q8_imputed_missing: Array of imputed values for originally missing entries
q8_true_missing: Array of true values for those same entries
q8_correlation: Pearson correlation between imputed and true (rounded to 3 decimals)
q8_rmse: RMSE between imputed and true (rounded to 3 decimals)
# Grade Cell: Question 8
#
# Task: Evaluate imputation quality against ground truth
#
# Instructions:
# 1. Load the ground truth matrix
# 2. Center it using the same movie means from Q3
# 3. Extract imputed and true values for originally missing entries
# 4. Compute correlation and RMSE




q8_ground_truth = pd.read_csv("ratings_ground_truth.csv").values

gt_centered = q8_ground_truth - q3_movie_means

missing_mask = np.isnan(q3_centered_matrix)

q8_imputed_missing = q6_completed[missing_mask]
q8_true_missing = gt_centered[missing_mask]

q8_correlation: float = round(
    float(np.corrcoef(q8_imputed_missing, q8_true_missing)[0, 1]), 3
)
q8_rmse: float = round(
    float(np.sqrt(np.mean((q8_imputed_missing - q8_true_missing) ** 2))), 3
)


print(f"Number of missing entries evaluated: {len(q8_imputed_missing)}")
print(f"Correlation (imputed vs true): {q8_correlation}")
print(f"RMSE (imputed vs true): {q8_rmse}")
