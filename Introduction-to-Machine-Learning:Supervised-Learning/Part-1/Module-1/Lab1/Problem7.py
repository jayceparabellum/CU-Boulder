def cross_val_knn(k_values: List[int]) -> Dict[int, float]:
    """Run 5-fold CV on the training split for each k and return mean CV RMSE.

    Parameters
    ----------
    k_values : List[int]
        The neighbor counts to evaluate.

    Returns
    -------
    Dict[int, float]
        Maps each k to its mean cross-validated RMSE, rounded to three decimals.
    """
    kf = KFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    results: Dict[int, float] = {}

    for k in k_values:
        knn = KNeighborsRegressor(n_neighbors=k)
        scores = cross_val_score(
            knn, X_train, y_train,
            cv=kf,
            scoring="neg_root_mean_squared_error",
        )
        # scores are negative RMSE per fold; negate and average
        results[k] = round(-scores.mean(), 3)

    return results
print(cross_val_knn([3, 5, 7]))
