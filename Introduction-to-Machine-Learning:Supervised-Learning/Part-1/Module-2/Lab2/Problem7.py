def evaluate_model(
    model: LinearRegression,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> Tuple[float, float]:
    """Evaluate a fitted model on test data.
    Parameters
    ----------
    model : LinearRegression
        A trained regression model.
    X_test : pd.DataFrame
        Test feature matrix.
    y_test : pd.Series
        True target values for the test set.
    Returns
    -------
    Tuple[float, float]
        The (MSE, R²) scores, each rounded to three decimals.
    """
    y_pred = model.predict(X_test)
    mse = round(mean_squared_error(y_test, y_pred), 3)
    r2 = round(r2_score(y_test, y_pred), 3)
    return (mse, r2)
print(f"Function returned MSE: {test_mse:.3f}, R²: {test_r2:.3f}")
