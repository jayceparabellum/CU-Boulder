####Use LassoCV to select alpha and evaluate on the test set. Also count non-zero coefficients.

# Grade Cell: Question 7
#
# Task: Train LassoCV and compute metrics.
#
# Instructions:
# - Use `lasso_alphas = np.logspace(-3, 1, 50)`, `cv=5`, `random_state=RANDOM_STATE`, `max_iter=10000`
# - Store `lasso_best_alpha`, `rmse_lasso_test`, `r2_lasso_test`, `n_nonzero_lasso`

# Use the exact parameters specified in the instructions
lasso_alphas = np.logspace(-3, 1, 50)

lasso_cv = LassoCV(
    alphas=lasso_alphas,
    cv=5,
    max_iter=10000,
    random_state=RANDOM_STATE,
)
lasso_cv.fit(X_train_scaled, y_train)

lasso_best_alpha = float(lasso_cv.alpha_)

y_pred_lasso = lasso_cv.predict(X_test_scaled)
rmse_lasso_test = float(np.sqrt(mean_squared_error(y_test, y_pred_lasso)))
r2_lasso_test = float(r2_score(y_test, y_pred_lasso))

n_nonzero_lasso = int(np.sum(lasso_cv.coef_ != 0))

print(f"Lasso best alpha: {lasso_best_alpha:.5f}")
print(f"Lasso RMSE:       {rmse_lasso_test:.4f}")
print(f"Lasso R²:         {r2_lasso_test:.4f}")
print(f"Non-zero coefs:   {n_nonzero_lasso}")
