# Grade Cell: Question 9
#
# Task: Find the two most similar states based on standardized distances
#
# Instructions:
# 1. Copy the distance matrix and set diagonal to infinity
# 2. Find the indices of the minimum value
# 3. Get the state names corresponding to those indices

dist = q8_scaled_dist_matrix.copy()

np.fill_diagonal(dist, np.inf)

i, j = np.unravel_index(np.argmin(dist), dist.shape)

state_names = q7_scaled_data.index

q9_most_similar_pair: Tuple[str, str] = (state_names[i], state_names[j])
q9_min_distance: float = round(float(dist[i, j]), 3)

print(f"Most similar states: {q9_most_similar_pair}")
print(f"Distance between them: {q9_min_distance}")
