####Evaluate train/test MSE across a range of max_depth values and pick the depth with the best test MSE.


# Grade Cell: Question 3
#
# Task: Depth sweep on regression tree.
#
# Instructions:
# 1. For `depths = [1, 2, 3, 4, 5, 6, 8, 10, None]`, fit a tree for each depth.
# 2. Record train/test MSE in lists `train_mse_per_depth` and `test_mse_per_depth` aligned with `depths`.
# 3. Compute `best_depth` as the depth (value from the list) with minimal test MSE.

depths = list(range(1, 21))

train_mse_per_depth: List[float] = []
test_mse_per_depth: List[float] = []

for d in depths:
    tree = DecisionTreeRegressor(max_depth=d, random_state=RANDOM_STATE)
    tree.fit(X_train, y_train)
    train_mse_per_depth.append(mean_squared_error(y_train, tree.predict(X_train)))
    test_mse_per_depth.append(mean_squared_error(y_test, tree.predict(X_test)))

best_idx = int(np.argmin(test_mse_per_depth))
best_depth = int(depths[best_idx])

print("Depths:", depths)
print("Test MSE per depth:", [round(v, 2) for v in test_mse_per_depth])
print("Best depth:", best_depth)
