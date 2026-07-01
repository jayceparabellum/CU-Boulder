####Train a baseline DecisionTreeRegressor on the diabetes dataset and evaluate on a held-out test set.

# Grade Cell: Question 2
#
# Task: Train a baseline regression tree and compute metrics.
#
# Instructions:
# 1. Split df_reg into features X_reg and target y_reg; then into train/test with test_size=0.25 and random_state=RANDOM_STATE.
# 2. Fit DecisionTreeRegressor(random_state=RANDOM_STATE) as tree_reg.
# 3. Compute train and test metrics: MSE, MAE, and R^2.


X_reg = df_reg.drop(columns=["target"])
y_reg = df_reg["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=RANDOM_STATE
)

tree_reg = DecisionTreeRegressor(random_state=RANDOM_STATE)
tree_reg.fit(X_train, y_train)

y_train_pred = tree_reg.predict(X_train)
y_test_pred = tree_reg.predict(X_test)

mse_tree_train = mean_squared_error(y_train, y_train_pred)
mse_tree_test = mean_squared_error(y_test, y_test_pred)
mae_tree_test = mean_absolute_error(y_test, y_test_pred)
r2_tree_test = r2_score(y_test, y_test_pred)

print(
    f"Train MSE: {mse_tree_train:.2f}, Test MSE: {mse_tree_test:.2f}, "
    f"Test MAE: {mae_tree_test:.2f}, Test R2: {r2_tree_test:.3f}"
)
