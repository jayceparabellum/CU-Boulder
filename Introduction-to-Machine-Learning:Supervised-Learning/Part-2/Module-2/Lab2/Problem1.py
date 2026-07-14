1. Load the Dataset (10 points)
Load the Wine dataset from wine.csv into a pandas DataFrame.

The Wine dataset contains chemical measurements from wines produced by three different Italian cultivars. Each row represents a wine sample, and each column represents a chemical property (e.g., alcohol content, malic acid, color intensity).

Store the following in the required variables:

q1_shape: A tuple containing the shape of the DataFrame (n_samples, n_features)
q1_columns: A list of all column names (feature names)
q1_n_features: An integer representing the number of features


# Grade Cell: Question 1
#
# Task: Load the Wine dataset and explore its structure
#
# Instructions:
# 1. Read the CSV file using pd.read_csv()
# 2. Store the shape as a tuple in q1_shape
# 3. Store the column names as a list in q1_columns
# 4. Store the number of features (columns) as an integer in q1_n_features

def load_wine_data() -> pd.DataFrame:
    return pd.read_csv(_DATA_PATH)

df = load_wine_data()

q1_shape: Tuple[int, int] = df.shape
q1_columns: List[str] = df.columns.tolist()
q1_n_features: int = df.shape[1]

print(f"Dataset shape: {q1_shape}")
print(f"Columns: {q1_columns}")
print(f"Number of features: {q1_n_features}")
