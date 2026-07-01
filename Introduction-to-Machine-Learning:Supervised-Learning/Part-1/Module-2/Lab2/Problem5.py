y_pred = model.predict(X_test)

q5_mse: float = round(mean_squared_error(y_test, y_pred), 3)
print(f"Test R²: {q6_r2:.3f}")
