# Run 5-fold CV across all candidate k values
k_values = [1, 3, 5, 7, 9, 15, 25]
cv_results = cross_val_knn(k_values)

# Pick the k with the lowest cross-validated RMSE
q8_best_k: int = min(cv_results, key=cv_results.get)

# Compute the test RMSE for that best k
q8_test_rmse: float = knn_rmse(q8_best_k)

print(f"CV results: {cv_results}")
print(f"Best k: {q8_best_k}")
print(f"Test RMSE at best k: {q8_test_rmse}")
