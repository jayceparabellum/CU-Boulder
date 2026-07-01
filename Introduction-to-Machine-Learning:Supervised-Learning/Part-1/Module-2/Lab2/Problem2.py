df = load_auto_data()

FEATURE_COLUMNS: List[str] = ["displacement", "horsepower", "weight", "acceleration"]

X: pd.DataFrame = df[FEATURE_COLUMNS]
y: pd.Series = df["mpg"]

q2_num_features: int = X.shape[1]
print(f"Number of features: {q2_num_features}")`
