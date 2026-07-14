# Grade Cell: Question 8
#
# Task: Build distance matrix on standardized data
#
# Instructions:
# 1. Compute pairwise Euclidean distances on q7_scaled_data
# 2. Extract the distance between Alabama and Alaska

n = q7_scaled_data.shape[0]
q8_scaled_dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        d = euclidean_distance(q7_scaled_data.iloc[i], q7_scaled_data.iloc[j])
        q8_scaled_dist_matrix[i, j] = d
        q8_scaled_dist_matrix[j, i] = d
        
q8_al_ak_scaled: float = euclidean_distance(q7_scaled_data.iloc[0], q7_scaled_data.iloc[1])
    
print(f"Unstandardized Alabama-Alaska distance: {q4_distance_al_ak}")
print(f"Standardized Alabama-Alaska distance: {q8_al_ak_scaled}")
print(f"Ratio (unstandardized / standardized): {q4_distance_al_ak / q8_al_ak_scaled:.2f}")
