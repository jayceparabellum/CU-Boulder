# Grade Cell: Question 1
#
# Task: Load the USArrests dataset and explore its structure
#
# Instructions:
# 1. Read the CSV file using pd.read_csv() with index_col=0 to use state names as index
# 2. Store the shape as a tuple in q1_shape
# 3. Store the column names as a list in q1_columns

def load_arrests() -> pd.DataFrame:
    return pd.read_csv(_DATA_PATH, index_col=0)

df = load_arrests()
q1_shape: Tuple[int, int] = df.shape
q1_columns: List[str] = df.columns.tolist()

print(f"Dataset shape: {q1_shape}")
print(f"Columns: {q1_columns}")
