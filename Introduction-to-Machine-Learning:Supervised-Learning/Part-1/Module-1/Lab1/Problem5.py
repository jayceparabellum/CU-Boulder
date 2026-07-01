def knn_rmse(k: int) -> float:
    """Train a KNeighborsRegressor with the given k and return its test RMSE.

    Parameters
    ----------
    k : int
        Number of neighbors for the regressor.

    Returns
    -------
    float
        Test RMSE rounded to three decimals.
    """
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return round(np.sqrt(mean_squared_error(y_test, y_pred)), 3)
