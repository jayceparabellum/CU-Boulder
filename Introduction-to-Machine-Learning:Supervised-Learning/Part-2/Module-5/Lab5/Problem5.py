5. SVD-based Matrix Reconstruction (10 points)
Now let's use Singular Value Decomposition (SVD) to create a low-rank approximation of the imputed matrix. The truncated SVD gives us:

𝐗≈𝐔𝑀𝚺𝑀𝐕𝑇𝑀
 

where we keep only the top  𝑀
  singular values.

Implement a function that computes a rank- 𝑀
  approximation of a matrix using SVD, then use it to reconstruct the mean-imputed matrix.

Store the results as:

q5_reconstruct_matrix: A function that takes (matrix, rank) and returns the reconstruction
q5_reconstructed: The rank-5 reconstruction of q4_mean_imputed
q5_reconstruction_error: RMSE between original and reconstructed (rounded to 4 decimals)
# Grade Cell: Question 5
#
# Task: Implement SVD-based matrix reconstruction
#
# Instructions:
# 1. Use np.linalg.svd to decompose the matrix
# 2. Keep only the top M singular values and corresponding vectors
# 3. Reconstruct using U_M @ diag(S_M) @ V_M^T
# 4. Compute RMSE as sqrt(mean((original - reconstructed)^2))


def q5_reconstruct_matrix(matrix, rank: int):
    """Return the rank-M approximation of `matrix` via truncated SVD."""
    U, s, Vt = svd(matrix, full_matrices=False)

    U_m = U[:, :rank]
    s_m = s[:rank]
    Vt_m = Vt[:rank, :]

    return U_m @ np.diag(s_m) @ Vt_m

q5_reconstructed = q5_reconstruct_matrix(q4_mean_imputed, 5)

q5_reconstruction_error: float = round(
    float(np.sqrt(np.mean((q4_mean_imputed - q5_reconstructed) ** 2))), 4
)

print(f"Reconstructed matrix shape: {q5_reconstructed.shape}")
print(f"Reconstruction RMSE: {q5_reconstruction_error}")
