# Fit ordinary least-squares linear regression
linreg = LinearRegression()
linreg.fit(X_train, y_train)

# Predict on the test set
y_pred = linreg.predict(X_test)

# Test RMSE, rounded to 3 decimals
q6_linreg_rmse: float = round(np.sqrt(mean_squared_error(y_test, y_pred)), 3)

print(f"LinearRegression test RMSE: {q6_linreg_rmse}")
