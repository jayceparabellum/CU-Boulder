# Grade Cell: Question 4
#
# Task: Implement Euclidean distance function
#
# Instructions:
# 1. Implement the euclidean_distance function using the formula above
# 2. Use np.sqrt() and np.sum() for the calculation
# 3. Round the result to 3 decimal places
# 4. Compute distance between Alabama and Alaska

def euclidean_distance(x, y) -> float:
    """Euclidean distance between two equal-length vectors, rounded to 3 decimals."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    return round(float(np.sqrt(np.sum((x - y) **2))), 3)

alabama = df.iloc[0]
alaska = df.iloc[1]

q4_distance_al_ak: float = euclidean_distance(alabama, alaska)
    
print(f"Test distance [1,2,3] to [4,5,6]: {test_dist}")
print(f"Distance Alabama to Alaska: {q4_distance_al_ak}")
