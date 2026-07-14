3. Compute Linkage Matrix (10 points)
The first step in hierarchical clustering is computing the linkage matrix. This matrix encodes the merge history: which clusters were merged at each step and the distance at which they merged.

Use scipy's linkage() function with complete linkage (also called "furthest neighbor" linkage), which defines the distance between two clusters as the maximum distance between any pair of their members.

Store the results as:

q3_linkage_matrix: The linkage matrix (numpy array) from scipy
q3_n_merges: The number of merges performed (integer)
q3_max_distance: The maximum merge distance (float, rounded to 2 decimals)
# Grade Cell: Question 3
#
# Task: Compute the linkage matrix using complete linkage
#
# Instructions:
# 1. Use scipy.cluster.hierarchy.linkage() with method='complete'
# 2. The number of merges equals n_samples - 1
# 3. The maximum distance is in the last row, third column of the linkage matrix
​
q3_linkage_matrix = linkage(q2_scaled_data, method="complete")
​
q3_n_merges: int = q3_linkage_matrix.shape[0]
​
q3_max_distance: float = round(float(q3_linkage_matrix[-1, 2]), 2)
​
print(f"Linkage matrix shape: {q3_linkage_matrix.shape}")
print(f"Number of merges: {q3_n_merges}")
print(f"Maximum merge distance: {q3_max_distance}")
