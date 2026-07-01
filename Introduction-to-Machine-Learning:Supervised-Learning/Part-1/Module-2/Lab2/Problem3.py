X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE
)

q3_split_counts: Tuple[int, int] = (X_train.shape[0], X_test.shape[0])
print(f"Train/test split: {q3_split_counts}")  # (313, 79)print(f"Train rows: {train_rows}, Test rows: {test_rows}")
