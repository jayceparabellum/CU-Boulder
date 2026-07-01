####Estimate performance uncertainty using bootstrap out-of-bag RMSE on the training set.


# Grade Cell: Question 10
#
# Task: Implement Bootstrap OOB RMSE for OLS.
#
# Instructions:
# - Implement `bootstrap_oob_rmse_ols` that returns (rmse_oob_mean, rmse_oob_ci95)
# - Use B=200, RANDOM_STATE


B = 1000
n_train = X_train_scaled.shape[0]

rng = np.random.default_rng(RANDOM_STATE)
y_train_arr = np.asarray(y_train)

oob_rmse_scores = []

for b in range(B):
    idx = rng.integers(0, n_train, size=n_train)

    oob_mask = np.ones(n_train, dtype=bool)
    oob_mask[idx] = False

    if not oob_mask.any():
        continue

    ols_b = LinearRegression()
    ols_b.fit(X_train_scaled[idx], y_train_arr[idx])

    y_oob_pred = ols_b.predict(X_train_scaled[oob_mask])
    rmse_b = np.sqrt(mean_squared_error(y_train_arr[oob_mask], y_oob_pred))
    oob_rmse_scores.append(rmse_b)

oob_rmse_scores = np.array(oob_rmse_scores)

rmse_oob_mean = float(oob_rmse_scores.mean())

ci_low, ci_high = np.percentile(oob_rmse_scores, [2.5, 97.5])
rmse_oob_ci95 = (float(ci_low), float(ci_high))   # tuple of two floats

print(
    f"OOB RMSE mean: {rmse_oob_mean:.3f}, 95% CI: [{rmse_oob_ci95[0]:.3f}, {rmse_oob_ci95[1]:.3f}]"
)

