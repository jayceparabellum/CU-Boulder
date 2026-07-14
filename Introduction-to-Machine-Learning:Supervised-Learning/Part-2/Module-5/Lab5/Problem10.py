10. Reusable Matrix Completion Pipeline (5 points)
Finally, create a complete pipeline function that takes a sparse rating matrix and returns predictions. This encapsulates all the steps we've learned.

Store the results as:

q10_matrix_completion_pipeline: The pipeline function
q10_pipeline_result: Result of running pipeline on our data
q10_result_keys: List of keys in the result dictionary
# Grade Cell: Question 10
#
# Task: Create a complete matrix completion pipeline
#
# Instructions:
# 1. Combine centering, completion, and un-centering into one function
# 2. Return a dictionary with completed matrix, movie means, and metadata




def q10_matrix_completion_pipeline(rating_matrix, rank: int = 5, max_iter: int = 20) -> Dict:
    """End-to-end: center, complete via iterative SVD, un-center, clip to valid range."""
    movie_means = np.nanmean(rating_matrix, axis=0)
    centered = rating_matrix - movie_means

    completed_centered, errors = q6_complete_matrix(centered, rank=rank, max_iter=max_iter)

    # Un-center back to the original scale, then clip to the valid 1-5 rating range
    completed = completed_centered + movie_means
    completed = np.clip(completed, 1.0, 5.0)

    observed_mask = ~np.isnan(rating_matrix)

    return {
        "completed_matrix": completed,
        "completed_centered": completed_centered,
        "movie_means": movie_means,
        "rank": rank,
        "n_iterations": len(errors),
        "convergence_errors": errors,
        "n_observed": int(observed_mask.sum()),
        "n_missing": int((~observed_mask).sum()),
        "sparsity": round(float((~observed_mask).sum() / rating_matrix.size), 3),
    }

q10_pipeline_result: Dict = q10_matrix_completion_pipeline(q2_rating_matrix, rank=5, max_iter=20)

q10_result_keys: List[str] = list(q10_pipeline_result.keys())

completed = q10_pipeline_result["completed_matrix"]

print(f"Pipeline result keys: {q10_result_keys}")
print(f"Completed matrix shape: {completed.shape}")
print(f"Number of imputed entries: {q10_pipeline_result['n_missing']}")
print(f"Rank used: {q10_pipeline_result['rank']}")
