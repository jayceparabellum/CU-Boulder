# Grade Cell: Question 5
#
# Task: Implement Manhattan distance function
#
# Instructions:
# 1. Implement the manhattan_distance function using the formula above
# 2. Use np.sum() and np.abs() for the calculation
# 3. Round the result to 3 decimal places
# 4. Compute distance between Alabama and Alaska

def manhattan_distance(x, y) -> float:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    return round(float(np.sum(np.abs(x - y))), 3)

q5_manhattan_al_ak: float = manhattan_distance(df.iloc[0], df.iloc[1])

print(f"Test Manhattan distance [1,2,3] to [4,5,6]: {test_manhattan}")
print(f"Manhattan distance Alabama to Alaska: {q5_manhattan_al_ak}")
