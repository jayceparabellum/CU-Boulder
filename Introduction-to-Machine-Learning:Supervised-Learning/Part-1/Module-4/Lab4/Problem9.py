####Use bootstrap on the training set to estimate uncertainty of OLS coefficients. Return the bootstrap distribution (B x p) and 95% CIs.

# Grade Cell: Question 9
#
# Task: Implement a bootstrap procedure for OLS coefficients.
#
# Use bootstrap on the training set to estimate uncertainty of OLS coefficients. Return the bootstrap distribution (B x p) and 95% CIs.

def bootstrap_ols_coefficients(X_scaled, y, feature_names, B=200, random_state=RANDOM_STATE):
    """Bootstrap OLS coefficients.
    Draws B resamples (with replacement), fits OLS on each, collects coefficients.
    Returns (coef_bootstrap_df, coef_ci_95).
    """
    n = X_scaled.shape[0]
    p = X_scaled.shape[1]
    rng = np.random.default_rng(random_state)
    y_arr = np.asarray(y)

    boot_coefs = np.empty((B, p))
    for b in range(B):
        idx = rng.integers(0, n, size=n)
        ols_b = LinearRegression()
        ols_b.fit(X_scaled[idx], y_arr[idx])
        boot_coefs[b] = ols_b.coef_

    coef_bootstrap_df = pd.DataFrame(boot_coefs, columns=feature_names)

    ci_lower = coef_bootstrap_df.quantile(0.025)
    ci_upper = coef_bootstrap_df.quantile(0.975)
    coef_ci_95 = pd.DataFrame({"lower": ci_lower, "upper": ci_upper})

    return coef_bootstrap_df, coef_ci_95


feature_names = list(X.columns)

coef_bootstrap_df, coef_ci_95 = bootstrap_ols_coefficients(
    X_train_scaled, y_train, feature_names, B=200, random_state=RANDOM_STATE
)

print(f"Bootstrap shape: {coef_bootstrap_df.shape}")
print(coef_ci_95.round(3))
