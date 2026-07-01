#Use K-fold cross-validation on the training set to estimate OLS generalization error.

# Grade Cell: Question 5
#
# Task: Compute CV RMSE mean and std for OLS on the training split.
#
# Instructions:
# - Use `cross_val_score` with `scoring='neg_mean_squared_error'` and `KFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)`.
# - Store `rmse_ols_cv_mean` and `rmse_ols_cv_std` (floats).

kf = KFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

ols_cv = LinearRegression()

neg_mse_scores = cross_val_score(
    ols_cv, X_train_scaled, y_train,
    cv=kf, scoring="neg_mean_squared_error"
)

rmse_cv_scores = np.sqrt(-neg_mse_scores)
rmse_ols_cv_mean = float(rmse_cv_scores.mean())
rmse_ols_cv_std = float(rmse_cv_scores.std())

print(f"OLS CV RMSE mean: {rmse_ols_cv_mean:.3f}, std: {rmse_ols_cv_std:.3f}")
