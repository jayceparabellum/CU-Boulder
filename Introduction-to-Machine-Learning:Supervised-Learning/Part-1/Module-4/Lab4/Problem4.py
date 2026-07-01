#Train a LinearRegression model and evaluate on the test set using RMSE and R^2.

# Grade Cell: Question 4
#
# Task: Train a baseline OLS model and compute metrics.
#
# Instructions:
# 1. Fit `LinearRegression` using `X_train_scaled`, `y_train`.
# 2. Compute test RMSE (`rmse_ols_test`) and R^2 (`r2_ols_test`).

lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train)

y_pred = lin_reg.predict(X_test_scaled)

rmse_ols_test = float(np.sqrt(mean_squared_error(y_test, y_pred)))
r2_ols_test = float(r2_score(y_test, y_pred))

print(f"OLS RMSE: {rmse_ols_test:.3f}, R^2: {r2_ols_test:.3f}")
