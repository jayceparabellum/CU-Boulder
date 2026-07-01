Use RidgeCV over a log-spaced grid to select the best alpha, then evaluate on the test set.

# Use the exact grid specified in the instructions
ridge_alphas = np.logspace(-3, 3, 50)

ridge_cv = RidgeCV(alphas=ridge_alphas, scoring="neg_mean_squared_error", cv=kf)
ridge_cv.fit(X_train_scaled, y_train)

ridge_best_alpha = float(ridge_cv.alpha_)

y_pred_ridge = ridge_cv.predict(X_test_scaled)
rmse_ridge_test = float(np.sqrt(mean_squared_error(y_test, y_pred_ridge)))
r2_ridge_test = float(r2_score(y_test, y_pred_ridge))

print(f"Ridge best alpha: {ridge_best_alpha:.5f}")
print(f"Ridge RMSE:       {rmse_ridge_test:.4f}")
print(f"Ridge R²:         {r2_ridge_test:.4f}")
