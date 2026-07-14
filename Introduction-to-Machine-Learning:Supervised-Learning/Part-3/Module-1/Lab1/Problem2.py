2. Prepare Features and Target (10 points)
Separate the dataset into:

X: A DataFrame containing all feature columns (everything except target)
y: A Series containing the target column
Store the number of features in q2_n_features (an integer).

df = load_data()

# your code here
raise NotImplementedError
df = load_data()
​
X = df.drop(columns=["target"])
y = df["target"]
​
q2_n_features: int = X.shape[1]
​
print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
print(f"Number of features: {q2_n_features}")
