## 6. Build a Distance Matrix *(15 points)*

##A distance matrix shows the pairwise distances between all observations. This is
##fundamental to many clustering algorithms.

##Build a **Euclidean distance matrix** for all 50 states using the **unstandardized**
##(original) data.

##Store the result as:
##- **`q6_dist_matrix`**: A 2D numpy array of shape (50, 50) containing pairwise distances

##he diagonal should be 0 (distance from a state to itself), and the matrix should
##be symmetric (distance from A to B equals distance from B to A).

##**Hint:** You can use nested loops, or use `scipy.spatial.distance.pdist` and
##`squareform` for efficiency.



from scipy.spatial.distance import pdist, squareform

q6_dist_matrix = squareform(pdist(df.values, metric="euclidean"))

print(f"Shape: {q6_dist_matrix.shape}")
print(f"Diagonal zero: {np.allclose(np.diag(q6_dist_matrix), 0)}")
print(f"Symmetric: {np.allclose(q6_dist_matrix, q6_dist_matrix.T)}")
