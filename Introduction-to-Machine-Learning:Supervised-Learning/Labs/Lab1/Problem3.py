####Personal code starts here####
df = loaddf = load_housing()

# Predictors: everything except the target. Target: just MedHouseVal.
X = df.drop(columns=["MedHouseVal"])
y = df["MedHouseVal"]

# 80/20 split with the global seed
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE
)

# Row counts of each split
q3_split_counts: Tuple[int, int] = (X_train.shape[0], X_test.shape[0])

print(f"Split counts: {q3_split_counts}")
####Personal code ends here####
raise NotImplementedError
