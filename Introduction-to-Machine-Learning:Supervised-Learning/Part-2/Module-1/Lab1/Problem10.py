# Grade Cell: Question 10
#
# Task: Implement k-nearest neighbors lookup
#
# Instructions:
# 1. Get the row of distances for the given state
# 2. Sort indices by distance (excluding the state itself)
# 3. Return the top k state names

def find_k_nearest(state_name: str, k: int) -> List[str]:
    """Return the k nearest states to `state_name` by standardized Euclidean distance."""
    state_names = list(q7_scaled_data.index)
    anchor_idx = state_names.index(state_name)

    distances = q8_scaled_dist_matrix[anchor_idx].copy()

    distances[anchor_idx] = np.inf

    nearest_idx = np.argsort(distances)[:k]

    return [state_names[i] for i in nearest_idx]

q10_ca_neighbors: List[str] = find_k_nearest("California", 3)

print(f"California's 3 nearest neighbors: {q10_ca_neighbors}")
print(f"Texas's 2 nearest neighbors: {test_neighbors}")
