####Use cost-complexity pruning with cross-validation to choose the pruning strength and evaluate the pruned tree.


# Grade Cell: Question 4
#
# Task: Prune via cost-complexity path and CV.
#
# Instructions:
# 1. Fit an unpruned tree on training data and obtain `ccp_alphas` via `cost_complexity_pruning_path` on the TRAIN split only.
# 2. Subsample up to 20 unique alphas, evenly spaced.
# 3. For each alpha, perform 5-fold CV on the TRAIN split to estimate MSE.
# 4. Choose `alpha_hat` with minimal CV MSE; fit `tree_pruned` with that alpha and evaluate `mse_pruned` and `r2_pruned` on TEST.

base = DecisionTreeRegressor(random_state=RANDOM_STATE)
path = base.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas
ccp_alphas = ccp_alphas[ccp_alphas >= 0]
alphas_sorted = np.sort(ccp_alphas)

kf = KFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
mean_cv_mse: List[float] = []

for alpha in ccp_alphas:
    fold_mses = []
    for train_idx, val_idx in kf.split(X_train):
        X_tr, X_val = X_train.iloc[train_idx], X_train.iloc[val_idx]
        y_tr, y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]
        t = DecisionTreeRegressor(random_state=RANDOM_STATE, ccp_alpha=alpha)
        t.fit(X_tr, y_tr)
        fold_mses.append(mean_squared_error(y_val, t.predict(X_val)))
    mean_cv_mse.append(np.mean(fold_mses))

best_idx = int(np.argmin(mean_cv_mse))
alpha_hat = float(ccp_alphas[best_idx])

tree_pruned = DecisionTreeRegressor(random_state=RANDOM_STATE, ccp_alpha=alpha_hat)
tree_pruned.fit(X_train, y_train)

mse_pruned = mean_squared_error(y_test, tree_pruned.predict(X_test))
r2_pruned = r2_score(y_test, tree_pruned.predict(X_test))

print(
    f"alpha_hat={alpha_hat:.2e}, Pruned Test MSE={mse_pruned:.2f}, R2={r2_pruned:.3f}"
)
