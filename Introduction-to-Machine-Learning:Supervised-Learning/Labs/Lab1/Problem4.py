# Train KNN with k=5
knn5 = KNeighborsRegressor(n_neighbors=5)
knn5.fit(X_train, y_train)

# Predict on the test set
y_pred = knn5.predict(X_test)

# Test RMSE, rounded to 3 decimals
q4_knn5_rmse: float = round(np.sqrt(mean_squared_error(y_test, y_pred)), 3)

print(f"KNN (k=5) test RMSE: {q4_knn5_rmse}")
