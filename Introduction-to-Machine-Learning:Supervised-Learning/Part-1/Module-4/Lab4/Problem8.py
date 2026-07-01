####expose arrays for plotting CV error vs alpha. Plots are optional and not graded.

# Grade Cell: Question 8
#
# Task: Expose arrays for CV curves.
#
# Instructions:
# - For Ridge: use `ridge_alphas` and compute mean MSE over folds from `ridge_cv.cv_values_` (if available).
# - For Lasso: use `lasso_alphas` and `lasso_cv.mse_path_` (mean across folds).

# Grade Cell: Question 8
#
# Task: Expose arrays for CV curves.
#
# Instructions:
# - For Ridge: use `ridge_alphas` and compute mean MSE over folds from `ridge_cv.cv_values_` (if available).
# - For Lasso: use `lasso_alphas` and `lasso_cv.mse_path_` (mean across folds).

from sklearn.linear_model import Ridge

lasso_alphas = lasso_cv.alphas_
lasso_cv_mse_mean = lasso_cv.mse_path_.mean(axis=1)

ridge_alphas = np.logspace(-3, 3, 100)
ridge_cv_mse_mean = np.array([
    -cross_val_score(
        Ridge(alpha=a), X_train_scaled, y_train,
        cv=kf, scoring="neg_mean_squared_error"
    ).mean()
    for a in ridge_alphas
])

print(f"Ridge CV MSE array length: {len(ridge_cv_mse_mean)}")
print(f"Lasso CV MSE array length: {len(lasso_cv_mse_mean)}")
print("CV curve arrays prepared.")
