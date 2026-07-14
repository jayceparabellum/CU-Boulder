3. Train/Validation/Test Split with Scaling (10 points)
Neural networks perform better when features are standardized (zero mean, unit variance).

Split the data into training (60%), validation (20%), and test (20%) sets. Use random_state=RANDOM_STATE.
Fit a StandardScaler on the training data only, then transform all three sets.
Store the row counts as a tuple q3_split_counts = (n_train, n_val, n_test).

Hint: First split into train+val (80%) and test (20%), then split train+val into train (75%) and val (25%).

X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE
)

X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=RANDOM_STATE
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

q3_split_counts: Tuple[int, int, int] = (
    X_train_scaled.shape[0],
    X_val_scaled.shape[0],
    X_test_scaled.shape[0],
)

print(f"Split counts (train, val, test): {q3_split_counts}")
