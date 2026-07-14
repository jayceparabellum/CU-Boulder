1. Load the Dataset (10 points)
Load the Iris dataset from iris.csv into a pandas DataFrame.

This is the same Iris dataset you used in Week 3 for K-Means clustering. Using the same data allows us to directly compare hierarchical clustering results with K-Means results.

Store the following in the required variables:

q1_shape: A tuple containing the shape of the DataFrame (n_samples, n_features)
q1_columns: A list of all column names (feature names)
q1_n_samples: An integer representing the number of samples
# Grade Cell: Question 1
#
# Task: Load the Iris dataset and explore its structure
#
# Instructions:
# 1. Read the CSV file using pd.read_csv()
# 2. Store the shape as a tuple in q1_shape
# 3. Store the column names as a list in q1_columns
# 4. Store the number of samples (rows) as an integer in q1_n_samples
​
def load_iris_data() -> pd.DataFrame:
    return pd.read_csv(_DATA_PATH)
​
df = load_iris_data()
​
q1_shape: Tuple[int, int] = df.shape
q1_columns: List[str] = df.columns.tolist()
q1_n_samples: int = df.shape[0]
​
print(f"Dataset shape: {q1_shape}")
print(f"Number of samples: {q1_n_samples}")
print(f"Features: {q1_columns}")
