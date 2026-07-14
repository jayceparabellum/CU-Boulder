7. Select Optimal Rank via Validation (10 points)
How do we choose the rank  𝑀
  for matrix completion? We use validation by masking: hide some observed entries, run completion, and measure how well we recover them.

Implement a validation procedure:

Randomly mask 20% of observed entries (pretend they're missing)
Run matrix completion for different ranks M = 1, 2, 3, 5, 10
Measure recovery error on the masked entries
Select the rank with lowest validation error
Store the results as:

q7_validation_errors: A dictionary mapping rank to validation RMSE
q7_best_rank: The rank with lowest validation error
q7_best_error: The lowest validation error
# Grade Cell: Question 7
#
# Task: Select optimal rank using validation by masking
#
# Instructions:
# 1. Create a validation mask: randomly hide 20% of observed entries
# 2. For each candidate rank, run completion and measure recovery on masked entries
# 3. Find the rank with lowest validation error



                                      
candidate_ranks = [1, 2, 3, 5, 10]

rng = np.random.RandomState(RANDOM_STATE)
observed_idx = np.argwhere(~np.isnan(q3_centered_matrix))
n_val = int(0.2 * len(observed_idx))
val_positions = observed_idx[rng.choice(len(observed_idx), size=n_val, replace=False)]
val_rows, val_cols = val_positions[:, 0], val_positions[:, 1]
val_truth = q3_centered_matrix[val_rows, val_cols].copy()
train_matrix = q3_centered_matrix.copy()
train_matrix[val_rows, val_cols] = np.nan

q7_validation_errors: Dict[int, float] = {}
for rank in candidate_ranks:
    completed, _ = q6_complete_matrix(train_matrix, rank=rank, max_iter=20)
    predictions = completed[val_rows, val_cols]
    rmse = np.sqrt(np.mean((val_truth - predictions) ** 2))
    q7_validation_errors[rank] = round(float(rmse), 4)

q7_best_rank: int = int(min(q7_validation_errors, key=q7_validation_errors.get))
q7_best_error: float = q7_validation_errors[q7_best_rank]

print("Validation errors by rank:")
for rank in sorted(q7_validation_errors.keys()):
    marker = " <-- best" if rank == q7_best_rank else ""
    print(f"  Rank {rank}: {q7_validation_errors[rank]:.4f}{marker}")
print(f"\nBest rank: {q7_best_rank} with error: {q7_best_error:.4f}")
