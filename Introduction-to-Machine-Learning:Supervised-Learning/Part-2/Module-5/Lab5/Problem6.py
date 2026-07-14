6. Iterative Matrix Completion Algorithm (15 points)
Mean imputation ignores the correlation structure in the data. A better approach is the iterative matrix completion algorithm:

Initialize: Fill missing values with column means (done in Q4)
Repeat until convergence:
Compute rank- 𝑀
  SVD of the current filled matrix
Update missing entries with values from the low-rank reconstruction
Keep observed entries unchanged
Return the completed matrix
This algorithm iteratively refines the imputed values using the low-rank structure discovered by SVD.

Store the results as:

q6_complete_matrix: A function implementing the iterative algorithm
q6_completed: The completed matrix using rank=5 and max_iter=20
q6_final_error: Final reconstruction error (RMSE on observed entries)
# Grade Cell: Question 6
#
# Task: Implement the iterative matrix completion algorithm
#
# Instructions:
# 1. Start with mean-imputed matrix
# 2. Create a mask for observed entries (not NaN in original)
# 3. Iterate: SVD reconstruct, update only missing entries
# 4. Track convergence by monitoring change in imputed values


def q6_complete_matrix(centered_matrix, rank: int = 5, max_iter: int = 20, tol: float = 1e-6):
    """Iteratively complete a matrix with NaNs via repeated low-rank SVD reconstruction."""
    observed_mask = ~np.isnan(centered_matrix)
    X = np.nan_to_num(centered_matrix, nan=0.0)

    errors = []
    for _ in range(max_iter):
        X_old = X.copy()

        X_hat = q5_reconstruct_matrix(X, rank)
        X = np.where(observed_mask, X, X_hat)

        change = np.sqrt(np.mean((X - X_old) ** 2))
        errors.append(float(change))

        if change < tol:
            break

    return X, errors

q6_completed, q6_errors = q6_complete_matrix(q3_centered_matrix, rank=5, max_iter=20)

observed_mask = ~np.isnan(q3_centered_matrix)
reconstruction = q5_reconstruct_matrix(q6_completed, 5)

q6_final_error: float = round(
    float(np.sqrt(np.mean((q3_centered_matrix[observed_mask] - reconstruction[observed_mask]) ** 2))), 4
)

print(f"Completed matrix shape: {q6_completed.shape}")
print(f"Number of iterations: {len(q6_errors)}")
print(f"Final RMSE on observed: {q6_final_error}")
