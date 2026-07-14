1. Load and Explore the Dataset (10 points)
Write a function load_data() that reads breast_cancer_nn.csv into a pandas.DataFrame. Store the shape of the DataFrame in a variable called q1_shape.

The dataset contains 30 features computed from digitized images of breast mass fine needle aspirates, plus a target column (0 = malignant, 1 = benign).



def load_data() -> pd.DataFrame:
    """Load the Breast Cancer Wisconsin dataset from CSV.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the 30 features plus the target column.
    """
    return pd.read_csv(_DATA_PATH)


q1_shape: Tuple[int, int] = load_data().shape

print(f"Dataset shape: {q1_shape}")


def load_data() -> pd.DataFrame:
    """Load the Breast Cancer Wisconsin dataset from CSV.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the 30 features plus the target column.
    """
    return pd.read_csv(_DATA_PATH)


q1_shape: Tuple[int, int] = load_data().shape

print(f"Dataset shape: {q1_shape}")
